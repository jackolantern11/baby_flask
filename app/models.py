from datetime import datetime
from app import db
import pandas as pd


# Class for federal data
class Federal_Data(db.Model):

    __tablename__ = 'federal_data'
    _id = db.Column(db.Integer, primary_key=True, unique=True)
    year = db.Column(db.Integer)
    name = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    count = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def transform_objects_to_df(object_list: list) -> pd.DataFrame:

        if len(object_list) > 0:
            print("transform to datafame...")


        else:
            print("Creating empty dataframe...")

        return pd.DataFrame()

    # create init / static method to load data in for development?
    @staticmethod
    def gen_fed_data():
        return None

    def __repr__(self):
        return '<_id %r>' % self._id

# Class for state data

# Class for territory data
