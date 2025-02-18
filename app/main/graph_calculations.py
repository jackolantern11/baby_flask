import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio


def generate_base_name_graph(df: pd.DataFrame, name: str) -> object:
    """
    Function to generate plotly graph for male/female split based on dataframe
    :param df:
    :param name:
    :return:
    """

    if 'gender' in df.columns:
        male_df = df[(df['gender'] == "M")]
        female_df = df[(df['gender'] == "F")]

    else:
        # fill with dummy data
        male_df = pd.DataFrame({"year": [0], "count": [0]})
        female_df = male_df

    data = [go.Scatter(x=male_df['year'], y=male_df['count'], name='Male'), go.Scatter(x=female_df['year'], y=female_df['count'], name='Female')]

    layout = go.Layout(title=f"Births per year with name: {name}", showlegend=True)
    fig = go.Figure(data=data, layout=layout)
    graphJSON = pio.to_json(fig)

    return graphJSON


# def name_popular_year_dfs():
#     df = pd.DataFrame()
#     # df = read_mongo(db='baby_data', collection='federal_baby_name')
#
#     # Determine Most Popular Year for Each Name by Total Names Given
#     popular_years = (
#         df.merge(
#             df.groupby(["name", "gender"], as_index=False)["count"].max(),
#             how="inner",
#             on=["name", "gender", "count"],
#         )
#         .groupby(["name", "gender"], as_index=False)["year"]
#         .max()
#         .rename(columns={"year": "year_pop"}, inplace=False)
#     )
#
#     pop_total_name_df = df.merge(popular_years.rename(columns={"year_pop": "year"}), how='inner',
#                                  on=['name', 'gender', 'year'])
#
#     popular_proportion_years = (
#         df.merge(
#             df.groupby(["name", "gender"], as_index=False)["total_proportion"].max(),
#             how="inner",
#             on=["name", "gender", "total_proportion"],
#         )
#         .groupby(["name", "gender"], as_index=False)["year"]
#         .max()
#         .rename(columns={"year": "year_pop"}, inplace=False)
#     )
#
#     pop_proportion_name_df = df.merge(popular_proportion_years.rename(columns={"year_pop": "year"}), how='inner',
#                                       on=['name', 'gender', 'year'])
#
#     return pop_total_name_df, pop_proportion_name_df
