import uuid
from sqlalchemy import Column, String, Integer, Boolean, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class GemstoneCategory(Base):
    __tablename__ = "gemstone_categories"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

    gemstones = relationship("Gemstone", back_populates="category", cascade="all, delete-orphan")

