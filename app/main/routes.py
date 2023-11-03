from . import main

from flask import render_template, session, redirect, url_for
from . import graph_calculations
from .forms import NameForm
from app.models import Federal_Data
from . import queries


@main.route('/')
@main.route('/index')
def index():
    session.pop('graphJSON', None)
    return render_template("index.html")


@main.route('/name_research', methods=['GET', 'POST'])
def name_research():
    name_form = NameForm()
    genders = ["M", "F"]
    graphJSON = None

    if name_form.validate_on_submit():
        name = name_form.name.data
        single_name_df = queries.query_for_single_name_to_df(name, Federal_Data)
        graphJSON = graph_calculations.generate_base_name_graph(single_name_df, name)
        session['graphJSON'] = graphJSON

        # Temp Testing Func
        queries.query_for_all_federal_data(Federal_Data)

        return redirect(url_for('.name_research'))

    return render_template('name_research.html', graphJSON=session.get('graphJSON'), form=name_form, genders=genders)


# @main.route('/data_summary')
# def data_summary():
#     # page to display a dataframe as a table
#     # @ToDo - How to update this yearly or manually?
#     session.pop('graphJSON', None)
#     df = graph_calculations.create_base_df().head(100)
#     return render_template("data_summary.html", data={'year_min': df['year'].min(),
#                                                       'year_max': df['year'].max()}, df=df)
