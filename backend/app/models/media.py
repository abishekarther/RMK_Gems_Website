import uuid
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class GemstoneMedia(Base):
    __tablename__ = "gemstone_media"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    gemstone_id = Column(String(36), ForeignKey("gemstones.id"), nullable=False, index=True)
    media_type = Column(String(50), nullable=False)  # image, model_3d, preview
    file_url = Column(String(500), nullable=False)
    thumbnail_url = Column(String(500), nullable=True)
    alt_text = Column(String(255), nullable=False)
    display_order = Column(Integer, default=0)
    is_primary = Column(Boolean, default=False)

    gemstone = relationship("Gemstone", back_populates="media")

