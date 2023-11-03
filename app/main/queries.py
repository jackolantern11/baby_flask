import pandas as pd
from . import common
from .. import db
from . import decorators
from sqlalchemy.orm import Session
from sqlalchemy import text, func, over


@decorators.timer
def query_for_single_name_to_df(name: str, model) -> pd.DataFrame:
    """
    Query to return all data corresponding to a single name
    :param name: name to query
    :param model: table to query (model)
    :return: dataframe of data with the name
    """
    name_specific_data_objects = model.query.filter_by(name=name).all()
    df = common.tbl_obj_list_to_df(name_specific_data_objects)
    return df


@decorators.timer
def query_for_all_federal_data(model) -> pd.DataFrame:

    # Query for all data is very slow! - Paginate, or add filters to increase speed
    # What do we want to accomplish
    all_federal_data_objects = model.query.filter(model.year>2020).all()
    # df = common.tbl_obj_list_to_df(all_federal_data_objects)

    # df = df.merge(
    #     df.groupby(["year"], as_index=False)["count"].sum().rename(columns={"count": "year_total"}),
    #     how="left",
    #     on=["year"],
    # )
    #
    # df = df.merge(
    #     df.groupby(["year", "gender"], as_index=False)["count"].sum().rename(columns={"count": "year_gender_total"}),
    #     how="left",
    #     on=["year", "gender"],
    # )
    #
    # print(f"df: {df.head()}")


    # query_txt = f'''select fd._id, fd.year, fd.name, fd.gender, fd.count,
    #        sum(fd.count) OVER (PARTITION BY fd.year) AS year_total,
    #        sum(fd.count) OVER (PARTITION BY fd.year, fd.gender) AS year_gender_total
    #        from federal_data fd;'''

    # partitioned_data_objects = db.session.query(
    #     model.name,
    #     model.gender,
    #     model.year,
    #     model.count,
    #     func.sum(model.count).over(partition_by=model.year).label('year_total'),
    #     func.sum(model.count).over(partition_by=[model.year, model.gender]).label('year_gender_total')
    # ).all()

    # with Session(db.engine) as session:
    #     df = pd.DataFrame(session.execute(text(query_txt)))
    #     # print(f"df: \n {df.head().to_string()}")


    # i = 10
    # for thing in partitioned_data_objects:
    #     if i > 1:
    #         print(thing)
    #     else:
    #         break
    #
    #     i -= 1

    # df = common.tbl_obj_list_to_df(partitioned_data_objects)
    # print(f"df: \n {df.head().to_string()}")
    # return df
