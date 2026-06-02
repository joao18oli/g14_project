from flask import render_template, session
from classes.airline import Airline
from classes.airport import Airport
from datafile import filename
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
from flask import request

def apps_plotly():
    engine = create_engine('sqlite:///' + filename + 'Airport airlines.db')
    df_voo = pd.read_sql('Voo', con=engine)
    df_terminal = pd.read_sql('Terminal', con=engine)
    
    stats = {
    'flights': len(df_voo),
    'airports': len(Airport.obj),
    'airlines': len(Airline.obj),
    'terminals': len(df_terminal),
    }
    
    # Gráfico 1 — Custo médio por companhia aérea
    result1 = df_voo.groupby('airline_id')['ticket_cost'].mean()
    a_names = [Airline.obj[a_id].denomination for a_id in result1.index]
    
    fig1 = px.bar(x=a_names, y=result1.values,
                  labels={'x': 'Airline', 'y': 'Avg Ticket Cost'},
                  title='Average ticket cost by airline')
    
    fig1.update_yaxes(range=[2100, max(result1.values)])
    fig1.update_layout(xaxis={'categoryorder': 'total ascending', 'tickangle': -45})

    # Gráfico 2 — Número de voos por aeroporto
    result2 = df_voo.groupby('airport_id')['id'].count()
    ap_names = [Airport.obj[ap_id].name if ap_id in Airport.obj else str(ap_id) for ap_id in result2.index]
    fig2 = px.bar(x=ap_names, y=result2.values,
                  labels={'x': 'Airport', 'y': 'Number of Flights'},
                  title='Number of flights by airport')
    fig2.update_layout(xaxis_tickangle=-45)

    # Gráfico 3 — Número de voos por mês
    df_voo['flight_date'] = pd.to_datetime(df_voo['flight_date'])
    df_voo['month'] = df_voo['flight_date'].dt.to_period('M').astype(str)
    result3 = df_voo.groupby('month')['id'].count().reset_index()
    result3.columns = ['Month', 'Flights']
    fig3 = px.line(result3, x='Month', y='Flights',
                   title='Number of flights per month',
                   markers=True)
    fig3.update_layout(xaxis_tickangle=-45)

    # Gráfico 4 — Número de terminais por aeroporto
    result4 = df_terminal.groupby('airport_id')['id'].count()
    ap_names4 = [Airport.obj[ap_id].name if ap_id in Airport.obj else str(ap_id) for ap_id in result4.index]
    fig4 = px.bar(x=ap_names4, y=result4.values,
                  labels={'x': 'Airport', 'y': 'Number of Terminals'},
                  title='Number of terminals by airport')
                  
    fig4.update_layout(xaxis_tickangle=-45)

    plots = [
        fig1.to_html(full_html=False, div_id='plot1'),
        fig2.to_html(full_html=False, div_id='plot2'),
        fig3.to_html(full_html=False, div_id='plot3'),
        fig4.to_html(full_html=False, div_id='plot4'),
    ]

    return render_template("plotly.html", plots=plots, stats=stats, ulogin=session.get("user"))


def compare():
    engine = create_engine('sqlite:///' + filename + 'Airport airlines.db')
    df_voo = pd.read_sql('Voo', con=engine)
    df_terminal = pd.read_sql('Terminal', con=engine)

    airports = {ap.id: ap.name for ap in Airport.obj.values()}
    airlines = {al.id: al.denomination for al in Airline.obj.values()}

    # Flags para saber o que o user selecionou
    has_airports = 'a1' in request.args and request.args.get('a1') not in (None, '')
    has_airlines = 'al1' in request.args and request.args.get('al1') not in (None, '')

    # Se não escolheu nada → página vazia
    if not has_airports and not has_airlines:
        return render_template("compare.html",
                               airports=airports,
                               airlines=airlines,
                               plots=None,
                               result=None,
                               stats=None,
                               plots_airlines=None,
                               stats_airlines=None,
                               result_airlines=None,
                               result_cost_airlines=None,
                               result_airports_airlines=None,
                               ulogin=session.get("user"))

    # ============================
    # AIRPORTS SECTION
    # ============================
    if has_airports:
        a1 = int(request.args['a1'])
        a2 = int(request.args['a2'])

        # Estatísticas
        count1 = df_voo[df_voo['airport_id'] == a1].shape[0]
        count2 = df_voo[df_voo['airport_id'] == a2].shape[0]

        avg1 = df_voo[df_voo['airport_id'] == a1]['ticket_cost'].mean()
        avg2 = df_voo[df_voo['airport_id'] == a2]['ticket_cost'].mean()

        term1 = df_terminal[df_terminal['airport_id'] == a1].shape[0]
        term2 = df_terminal[df_terminal['airport_id'] == a2].shape[0]

        # Gráficos
        fig_flights = px.bar(
            x=[airports[a1], airports[a2]],
            y=[count1, count2],
            labels={'x': 'Airport', 'y': 'Number of Flights'},
            title='Flights'
        )
        fig_flights.update_layout(height=220, width=260, autosize=False)

        fig_cost = px.bar(
            x=[airports[a1], airports[a2]],
            y=[avg1, avg2],
            labels={'x': 'Airport', 'y': 'Avg Ticket Cost'},
            title='Avg Ticket Cost'
        )
        fig_cost.update_layout(height=220, width=260, autosize=False)

        fig_terminals = px.bar(
            x=[airports[a1], airports[a2]],
            y=[term1, term2],
            labels={'x': 'Airport', 'y': 'Terminals'},
            title='Terminals'
        )
        fig_terminals.update_layout(height=220, width=260, autosize=False)

        plots = {
            'flights': fig_flights.to_html(full_html=False),
            'cost': fig_cost.to_html(full_html=False),
            'terminals': fig_terminals.to_html(full_html=False)
        }

        # Resultados textuais
        if count1 > count2:
            result = f"{airports[a1]} has more flights ({count1} vs {count2})"
        elif count2 > count1:
            result = f"{airports[a2]} has more flights ({count2} vs {count1})"
        else:
            result = "Both airports have the same number of flights"

        if avg1 > avg2:
            result_cost = f"{airports[a1]} has higher average ticket prices ({avg1:.2f} vs {avg2:.2f})."
        elif avg2 > avg1:
            result_cost = f"{airports[a2]} has higher average ticket prices ({avg2:.2f} vs {avg1:.2f})."
        else:
            result_cost = "Both airports have the same average ticket price."

        if term1 > term2:
            result_term = f"{airports[a1]} has more terminals ({term1} vs {term2})."
        elif term2 > term1:
            result_term = f"{airports[a2]} has more terminals ({term2} vs {term1})."
        else:
            result_term = "Both airports have the same number of terminals."

        stats = {
            'a1_name': airports[a1],
            'a2_name': airports[a2],
            'flights': (count1, count2),
            'avg_cost': (avg1, avg2),
            'terminals': (term1, term2)
        }

    else:
        plots = None
        result = None
        result_cost = None
        result_term = None
        stats = None

    # ============================
    # AIRLINES SECTION
    # ============================
    if has_airlines:
        al1 = int(request.args['al1'])
        al2 = int(request.args['al2'])

        flights1_al = df_voo[df_voo['airline_id'] == al1].shape[0]
        flights2_al = df_voo[df_voo['airline_id'] == al2].shape[0]

        avg1_al = df_voo[df_voo['airline_id'] == al1]['ticket_cost'].mean()
        avg2_al = df_voo[df_voo['airline_id'] == al2]['ticket_cost'].mean()

        airports1_al = df_voo[df_voo['airline_id'] == al1]['airport_id'].nunique()
        airports2_al = df_voo[df_voo['airline_id'] == al2]['airport_id'].nunique()

        fig_cost_al = px.bar(
            x=[airlines[al1], airlines[al2]],
            y=[avg1_al, avg2_al],
            labels={'x': 'Airline', 'y': 'Avg Ticket Cost'},
            title='Avg Ticket Cost'
        )
        fig_cost_al.update_layout(height=220, width=260, autosize=False)

        fig_flights_al = px.bar(
            x=[airlines[al1], airlines[al2]],
            y=[flights1_al, flights2_al],
            labels={'x': 'Airline', 'y': 'Number of Flights'},
            title='Flights'
        )
        fig_flights_al.update_layout(height=220, width=260, autosize=False)

        fig_airports_al = px.bar(
            x=[airlines[al1], airlines[al2]],
            y=[airports1_al, airports2_al],
            labels={'x': 'Airline', 'y': 'Airports Served'},
            title='Airports Served'
        )
        fig_airports_al.update_layout(height=220, width=260, autosize=False)

        plots_airlines = {
            'cost': fig_cost_al.to_html(full_html=False),
            'flights': fig_flights_al.to_html(full_html=False),
            'airports': fig_airports_al.to_html(full_html=False)
        }

        if flights1_al > flights2_al:
            result_airlines = f"{airlines[al1]} operates more flights ({flights1_al} vs {flights2_al})."
        elif flights2_al > flights1_al:
            result_airlines = f"{airlines[al2]} operates more flights ({flights2_al} vs {flights1_al})."
        else:
            result_airlines = "Both airlines operate the same number of flights."

        if avg1_al > avg2_al:
            result_cost_airlines = f"{airlines[al1]} has higher average ticket prices ({avg1_al:.2f} vs {avg2_al:.2f})."
        elif avg2_al > avg1_al:
            result_cost_airlines = f"{airlines[al2]} has higher average ticket prices ({avg2_al:.2f} vs {avg1_al:.2f})."
        else:
            result_cost_airlines = "Both airlines have the same average ticket price."

        if airports1_al > airports2_al:
            result_airports_airlines = f"{airlines[al1]} serves more airports ({airports1_al} vs {airports2_al})."
        elif airports2_al > airports1_al:
            result_airports_airlines = f"{airlines[al2]} serves more airports ({airports2_al} vs {airports1_al})."
        else:
            result_airports_airlines = "Both airlines serve the same number of airports."

        stats_airlines = {
            'al1_name': airlines[al1],
            'al2_name': airlines[al2],
            'flights': (flights1_al, flights2_al),
            'avg_cost': (avg1_al, avg2_al),
            'airports': (airports1_al, airports2_al)
        }

    else:
        plots_airlines = None
        stats_airlines = None
        result_airlines = None
        result_cost_airlines = None
        result_airports_airlines = None

    return render_template("compare.html",
                           airports=airports,
                           plots=plots,
                           result_cost=result_cost,          
                           result=result,                    
                           result_term=result_term,          
                           stats=stats,
                           airlines=airlines,
                           plots_airlines=plots_airlines,
                           stats_airlines=stats_airlines,
                           result_cost_airlines=result_cost_airlines,         
                           result_airlines=result_airlines,                   
                           result_airports_airlines=result_airports_airlines, 
                           ulogin=session.get("user"))

