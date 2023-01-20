from application import app
from flask import render_template
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/graph')
def graph():

    df = pd.read_csv("data.csv").head(100)
    data = [go.Scatter(x=df['year'], y=df['name'])]
    layout = go.Layout(title='My Graph')
    fig = go.Figure(data=data, layout=layout)
    graphJSON = pio.to_json(fig)

    return render_template('graph.html', graphJSON=graphJSON)

@app.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    # @ToDo - How to update this yearly or manually?
    df = pd.read_csv("data.csv").head(25)
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
