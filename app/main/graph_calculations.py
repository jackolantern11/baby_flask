import pandas as pd
from app import db
from app.models import Federal_Data
from flask_sqlalchemy import SQLAlchemy


def create_base_df(name: str) -> pd.DataFrame:

    # Read Data from input source
    name_specific_data_objects = Federal_Data.query.filter_by(name=name).all()
    df = pd.DataFrame([obj.__dict__ for obj in name_specific_data_objects])

    # Calculate and Merge in Total Births for Each Year, then Total per Gender per Year
    # Can this be done with simpler sql queries??
    df = df.merge(
        df.groupby(["year"], as_index=False)["count"].sum().rename(columns={"count": "year_total"}),
        how="left",
        on=["year"],
    )

    df = df.merge(
        df.groupby(["year", "gender"], as_index=False)["count"].sum().rename(columns={"count": "year_gender_total"}),
        how="left",
        on=["year", "gender"],
    )

    # Calculate proportions per total and gender per year
    df['gender_proportion'] = df['count'] / df['year_gender_total']
    df['total_proportion'] = df['count'] / df['year_total']

    return df


def name_popular_year_dfs():

    df = pd.DataFrame()
    # df = read_mongo(db='baby_data', collection='federal_baby_name')

    # Determine Most Popular Year for Each Name by Total Names Given
    popular_years = (
        df.merge(
            df.groupby(["name", "gender"], as_index=False)["count"].max(),
            how="inner",
            on=["name", "gender", "count"],
        )
        .groupby(["name", "gender"], as_index=False)["year"]
        .max()
        .rename(columns={"year": "year_pop"}, inplace=False)
    )

    pop_total_name_df = df.merge(popular_years.rename(columns={"year_pop": "year"}), how='inner',
                                 on=['name', 'gender', 'year'])

    popular_proportion_years = (
        df.merge(
            df.groupby(["name", "gender"], as_index=False)["total_proportion"].max(),
            how="inner",
            on=["name", "gender", "total_proportion"],
        )
        .groupby(["name", "gender"], as_index=False)["year"]
        .max()
        .rename(columns={"year": "year_pop"}, inplace=False)
    )

    pop_proportion_name_df = df.merge(popular_proportion_years.rename(columns={"year_pop": "year"}), how='inner',
                                      on=['name', 'gender', 'year'])

    return pop_total_name_df, pop_proportion_name_df
