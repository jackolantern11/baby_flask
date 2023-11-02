import pandas as pd
from . import common
from . import decorators


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
