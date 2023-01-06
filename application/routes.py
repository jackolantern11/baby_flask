from application import app
from flask import render_template
import pandas as pd

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    df = pd.read_csv("data.csv")
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
