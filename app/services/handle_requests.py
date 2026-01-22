from fastapi import UploadFile
import pandas as pd


from services.data_transform import DataTransformer
from services.storage import StorageService


class HandleRequests:
    def __init__(self, cursor):
        self.cursor = cursor


    def handle_upload(self, file: UploadFile):

        df: pd.DataFrame = DataTransformer.transform(file)

        columns = [
            'weapon_id',
            'weapon_name',
            'weapon_type',
            'range_km',
            'weight_kg',
            'manufacturer',
            'origin_country',
            'storage_location',
            'year_estimated',
        ]

        records = [
            tuple(record.get(col, None) for col in columns)
            for record in df.to_dict(orient='records')
        ]

        return StorageService(self.cursor).crate_records(records)







