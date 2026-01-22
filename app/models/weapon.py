from pydantic import BaseModel, field_validator
from typing import Optional
import math

class Weapon(BaseModel):
    weapon_id: str
    weapon_name: str
    weapon_type: str
    range_km: int
    weight_kg: float
    manufacturer: Optional[str] = None
    origin_country: str
    storage_location: str
    year_estimated: int


    @field_validator("manufacturer", mode="before")
    @classmethod
    def nan_to_none(cls, v):
        if v is None:
            return None
        if isinstance(v, float) and math.isnan(v):
            return None
        return v