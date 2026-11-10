import uuid
from sqlalchemy import Column, String, Integer, Boolean, Text
from backend.app.core.database import Base

class ShopSettings(Base):
    __tablename__ = "shop_settings"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    shop_name = Column(String(100), nullable=False, default="RMK Gems")
    phone = Column(String(50), nullable=False, default="+91 93857 06450")
    whatsapp_number = Column(String(50), nullable=False, default="919385706450")
    address = Column(String(300), nullable=False)
    city = Column(String(100), nullable=False, default="Tenkasi")
    state = Column(String(100), nullable=False, default="Tamil Nadu")
    postal_code = Column(String(20), nullable=False, default="627811")
    delivery_description = Column(String(255), nullable=False, default="All-India delivery is offered on all gemstones.")
    map_url = Column(Text, nullable=False)
    directions_url = Column(Text, nullable=False)
    about_description = Column(Text, nullable=False)

class OpeningHours(Base):
    __tablename__ = "opening_hours"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    day_of_week = Column(String(20), nullable=False)
    period_number = Column(Integer, default=1)
    opening_time = Column(String(10), nullable=True)  # "10:30"
    closing_time = Column(String(10), nullable=True)  # "21:00"
    is_closed = Column(Boolean, default=False)
    is_confirmed = Column(Boolean, default=True)      # False for Tuesday
    display_order = Column(Integer, default=0)

