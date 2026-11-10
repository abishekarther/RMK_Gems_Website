from typing import Optional, List
from pydantic import BaseModel, ConfigDict

class ShopSettingsPublic(BaseModel):
    shop_name: str
    phone: str
    whatsapp_number: str
    address: str
    city: str
    state: str
    postal_code: str
    delivery_description: str
    map_url: str
    directions_url: str
    about_description: str

    model_config = ConfigDict(from_attributes=True)

class OpeningHourPublic(BaseModel):
    id: str
    day_of_week: str
    period_number: int
    opening_time: Optional[str] = None
    closing_time: Optional[str] = None
    is_closed: bool
    is_confirmed: bool
    display_order: int

    model_config = ConfigDict(from_attributes=True)

