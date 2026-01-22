from io import StringIO
from fastapi import UploadFile
import pandas as pd


class DataTransformer:

    @staticmethod
    def convert_to_df(file: UploadFile) -> pd.DataFrame:

        contents = file.file.read().decode("utf-8")
        return pd.read_csv(StringIO(contents))

    @staticmethod
    def _crate_level_risk(df: pd.DataFrame) -> None:

        max_val = df['km_range'].max()
        min_val = df['km_range'].min() - 1

        bins = [min_val, 20, 100, 300, max_val] 
        lab = ['Low', 'medium', 'High', 'extreme']
        
        df['level_risk'] = pd.cut(df['km_range'], bins=bins, labels=lab)


    @staticmethod
    def _fillna_manufacturer(df: pd.DataFrame) -> None:

        df['manufacturer'].fillna('Unknown', inplace = True)


    def transform(file: UploadFile) -> pd.DataFrame:
        df = DataTransformer.convert_to_df(file)
        DataTransformer._crate_level_risk(df)
        DataTransformer._fillna_manufacturer(df)

        return df







        