from flask import render_template, session
from classes.airline import Airline
from classes.airport import Airport
from datafile import filename
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

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
    fig1.update_layout(xaxis_tickangle=-45)

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