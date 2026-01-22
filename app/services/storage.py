class StorageService:

    def __init__(self, cursor):
        self.cursor = cursor

    
    def crate_records(self, records):

        query = """
                    INSERT INTO weapons
                    (
                        weapon_id,
                        weapon_name,
                        weapon_type,
                        range_km,
                        weight_kg,
                        manufacturer,
                        origin_country,
                        storage_location,
                        year_estimated
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

        self.cursor.executemany(query, records)

        return self.cursor.rowcount
