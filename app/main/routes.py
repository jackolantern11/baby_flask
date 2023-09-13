from . import main

from flask import render_template, session, redirect, url_for
import plotly.graph_objs as go
import plotly.io as pio
from . import graph_calculations
from .forms import NameForm


@main.route('/')
@main.route('/index')
def index():
    session.pop('graphJSON', None)
    return render_template("index.html")


@main.route('/graph', methods=['GET', 'POST'])
def graph():
    name_form = NameForm()
    genders = ["M", "F"]
    graphJSON = None

    if name_form.validate_on_submit():
        name = name_form.name.data
        # gender = name_form.gender.data
        df = graph_calculations.create_base_df(name=name)

        # @ToDo - Male & Female combined and Male & Female Separated
        # @ToDo - Names with similar popularity
        # @ToDo - Top Names of Last Year - Past 5/10/25/50/100 years
        # @ToDo - Random Name Generator
        # @ToDo - What year was 'x' name the most popular
        # @ToDo - Find all similar names to a name graph and table
        # @ToDo - compare in all lowercase

        df = df[(df['name'] == name)]
        male_df = df[(df['gender'] == "M")]
        female_df = df[(df['gender'] == "F")]

        data = [go.Scatter(x=male_df['year'], y=male_df['count']),
                go.Scatter(x=female_df['year'], y=female_df['count'])]

        layout = go.Layout(title=f"Births per year with name: {name}")
        fig = go.Figure(data=data, layout=layout)
        graphJSON = pio.to_json(fig)

        # lastTen = df[(df['year'].astype(int) > (int(datetime.now().year) - 10))]

        session['graphJSON'] = graphJSON
        # session['lastTenYearsTable'] = lastTen

        return redirect(url_for('.graph'))

    return render_template('graph.html', graphJSON=session.get('graphJSON'), form=name_form, genders=genders)


@main.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    # @ToDo - How to update this yearly or manually?
    session.pop('graphJSON', None)
    df = graph_calculations.create_base_df().head(100)
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
