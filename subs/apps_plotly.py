from flask import render_template, session
from classes.airline import Airline
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    
    engine = create_engine('sqlite:///' + filename + 'Airport airlines.db')
    df_voo = pd.read_sql('Voo', con=engine)

    result = df_voo.groupby('airline_id')['ticket_cost'].mean()

    a_ids = result.index
    a_names = []
    for a_id in a_ids:
        a_obj = Airline.obj[a_id]
        a_names.append(a_obj.denomination)
    costs = result.values


    fig = px.bar(x=a_names, y=costs, labels={'x': 'Airline', 'y': 'Avg Ticket Cost'}, title='Average ticket cost by airline')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))