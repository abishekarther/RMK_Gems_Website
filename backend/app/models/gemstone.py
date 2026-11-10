import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Gemstone(Base):
    __tablename__ = "gemstones"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    category_id = Column(String(36), ForeignKey("gemstone_categories.id"), nullable=False, index=True)
    name = Column(String(150), nullable=False, index=True)
    slug = Column(String(150), unique=True, nullable=False, index=True)
    short_description = Column(Text, nullable=True)
    full_description = Column(Text, nullable=True)
    material_type = Column(String(50), nullable=True)  # natural, synthetic, imitation, treated, unconfirmed
    colour = Column(String(100), nullable=True)
    hardness_min = Column(Float, nullable=True)
    hardness_max = Column(Float, nullable=True)
    chemical_composition = Column(String(200), nullable=True)
    crystal_system = Column(String(100), nullable=True)
    origin = Column(Text, nullable=True)
    formation = Column(Text, nullable=True)
    history_notes = Column(Text, nullable=True)
    treatments = Column(Text, nullable=True)
    care_instructions = Column(Text, nullable=True)
    
    # Internal fields — never exposed in public schemas
    source_notes = Column(Text, nullable=True)
    needs_client_confirmation = Column(Boolean, default=False)
    
    availability = Column(String(50), default="available")  # available, on_request, unconfirmed
    is_featured = Column(Boolean, default=False)
    display_order = Column(Integer, default=0)
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("GemstoneCategory", back_populates="gemstones")
    media = relationship("GemstoneMedia", back_populates="gemstone", cascade="all, delete-orphan", order_by="GemstoneMedia.display_order")

