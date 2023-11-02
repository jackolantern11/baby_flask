import pandas as pd


def tbl_obj_list_to_df(obj_list: list) -> pd.DataFrame:
    """
    Function to convert object list to dataframe for manipulation
    :param obj_list:
    :return: df - dataframe of objects
    """
    df = pd.DataFrame([obj.__dict__ for obj in obj_list])
    return df