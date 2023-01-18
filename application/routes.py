from application import app
from flask import render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/generate_png')
def generate_png():

    df = pd.read_csv("data.csv").head(25)
    plt.plot(df['year'], df['name'])
    plt.xlabel('Year')
    plt.ylabel('Name')
    plt.title('My First Flask Graph')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')


@app.route('/data_summary')
def data_summary():
    # page to display a dataframe as a table
    # @ToDo - How to update this yearly or manually?
    df = pd.read_csv("data.csv")
    return render_template("data_summary.html", data={'year_min': df['year'].min(),
                                                      'year_max': df['year'].max()}, df=df)
