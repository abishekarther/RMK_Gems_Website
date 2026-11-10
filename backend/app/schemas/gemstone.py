from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from backend.app.schemas.media import GemstoneMediaPublic

class GemstoneListPublic(BaseModel):
    id: str
    category_id: str
    category_slug: Optional[str] = None
    name: str
    slug: str
    short_description: Optional[str] = None
    material_type: Optional[str] = None
    colour: Optional[str] = None
    hardness_min: Optional[float] = None
    hardness_max: Optional[float] = None
    availability: str
    is_featured: bool
    display_order: int
    media: List[GemstoneMediaPublic] = []

    model_config = ConfigDict(from_attributes=True)

class GemstoneDetailPublic(BaseModel):
    id: str
    category_id: str
    category_slug: Optional[str] = None
    category_name: Optional[str] = None
    name: str
    slug: str
    short_description: Optional[str] = None
    full_description: Optional[str] = None
    material_type: Optional[str] = None
    colour: Optional[str] = None
    hardness_min: Optional[float] = None
    hardness_max: Optional[float] = None
    chemical_composition: Optional[str] = None
    crystal_system: Optional[str] = None
    origin: Optional[str] = None
    formation: Optional[str] = None
    history_notes: Optional[str] = None
    treatments: Optional[str] = None
    care_instructions: Optional[str] = None
    availability: str
    is_featured: bool
    display_order: int
    created_at: datetime
    updated_at: datetime
    media: List[GemstoneMediaPublic] = []

    model_config = ConfigDict(from_attributes=True)

class PaginatedGemstonesPublic(BaseModel):
    items: List[GemstoneListPublic]
    total: int
    page: int
    page_size: int
    total_pages: int

