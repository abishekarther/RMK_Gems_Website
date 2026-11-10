from typing import Optional
from pydantic import BaseModel, ConfigDict

class GemstoneMediaPublic(BaseModel):
    id: str
    media_type: str
    file_url: str
    thumbnail_url: Optional[str] = None
    alt_text: str
    display_order: int = 0
    is_primary: bool = False

    model_config = ConfigDict(from_attributes=True)

