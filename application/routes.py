from application import app
from flask import render_template
import plotly.graph_objs as go
import plotly.io as pio
from application import graph_calculations

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/graph')
def graph():

    # @ToDo - Create user input box for name:
    name = 'Raya'

    df = graph_calculations.create_base_df()
    df = df[df['name'] == name]
    data = [go.Scatter(x=df['year'], y=df['count'])]
    layout = go.Layout(title=f"Births per year with name: {name}")
    fig = go.Figure(data=data, layout=layout)
    graphJSON = pio.to_json(fig)

    return render_template('graph.html', graphJSON=graphJSON)

@app.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    # @ToDo - How to update this yearly or manually?
    df = graph_calculations.create_base_df().head(100)
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
