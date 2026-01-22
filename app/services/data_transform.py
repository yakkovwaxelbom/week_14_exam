from io import StringIO
from fastapi import UploadFile
import pandas as pd

from models.weapon import Weapon


class DataTransformer:

    @staticmethod
    def convert_to_df(file: UploadFile) -> pd.DataFrame:

        contents = file.file.read().decode("utf-8")
        return pd.read_csv(StringIO(contents))

    @staticmethod
    def _crate_level_risk(df: pd.DataFrame) -> None:

        max_val = df['range_km'].max()
        min_val = df['range_km'].min() - 1

        bins = [min_val, 20, 100, 300, max_val] 
        lab = ['Low', 'medium', 'High', 'extreme']
        
        df['level_risk'] = pd.cut(df['range_km'], bins=bins, labels=lab)


    @staticmethod
    def _fillna_manufacturer(df: pd.DataFrame) -> None:

        df['manufacturer'] = df['manufacturer'].fillna('Unknown')

    @staticmethod
    def _valid_val(df: pd.DataFrame):
        for record in df.to_dict(orient='records'):
            Weapon(**record)


    def transform(file: UploadFile) -> pd.DataFrame:
        df = DataTransformer.convert_to_df(file)
        DataTransformer._valid_val(df)
        DataTransformer._crate_level_risk(df)
        DataTransformer._fillna_manufacturer(df)

        return df







        