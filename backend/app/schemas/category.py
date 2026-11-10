from typing import Optional
from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    display_order: int = 0
    is_active: bool = True

class CategoryPublic(CategoryBase):
    id: str

    model_config = ConfigDict(from_attributes=True)

