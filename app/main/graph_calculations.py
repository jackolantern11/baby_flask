import pandas as pd

def create_base_df():

    # @ToDo - Move data input to MongoDB for faster reads
    # Read Data from input source
    df = pd.read_csv("./data/data.csv")

    # Calculate and Merge in Total Births for Each Year, then Total per Gender per Year
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

    # @ToDo - Move data input to MongoDB for faster reads
    # Read Data from input source
    df = pd.read_csv("./data/data.csv")

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

    pop_total_name_df = df.merge(popular_years.rename(columns={"year_pop": "year"}), how='inner', on=['name', 'gender', 'year'])

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