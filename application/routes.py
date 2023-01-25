from application import app
from flask import render_template, session, redirect, url_for
import plotly.graph_objs as go
import plotly.io as pio
from application import graph_calculations
from application.forms import NameForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/graph', methods=['GET', 'POST'])
def graph():

    name_form = NameForm()
    genders = ["M", "F"]
    graphJSON = None

    if name_form.validate_on_submit():
        name = name_form.name.data
        gender = name_form.gender.data
        df = graph_calculations.create_base_df()

        # @ToDo - Male & Female combined and Male & Female Separated
        # @ToDo - Names with similar popularity
        # @ToDo - Top Names of Last Year - Past 5/10/25/50/100 years
        # @ToDo - Random Name Generator
        # @ToDo - What year was 'x' name the most popular
        # @ToDo - Find all similar names to a name graph and table

        df = df[(df['name'] == name) & (df['gender'] == gender)]
        data = [go.Scatter(x=df['year'], y=df['count'])]
        layout = go.Layout(title=f"Births per year with name: {name} gender: {gender}")
        fig = go.Figure(data=data, layout=layout)
        graphJSON = pio.to_json(fig)
        session['graphJSON'] = graphJSON
        return redirect(url_for('graph'))

    return render_template('graph.html', graphJSON=session.get('graphJSON'), form=name_form, genders=genders)


@app.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    # @ToDo - How to update this yearly or manually?
    df = graph_calculations.create_base_df().head(100)
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
