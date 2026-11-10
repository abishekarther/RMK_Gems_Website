import uuid
from sqlalchemy import Column, String, Integer, Boolean, Text
from backend.app.core.database import Base

class HomepageSlide(Base):
    __tablename__ = "homepage_slides"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(200), nullable=False)
    subtitle = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=False)
    image_alt_text = Column(String(255), nullable=False)
    image_credit = Column(String(255), nullable=True)
    button_text = Column(String(100), nullable=False)
    button_link = Column(String(255), nullable=False)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

