from typing import Optional
from pydantic import BaseModel, ConfigDict

class HomepageSlidePublic(BaseModel):
    id: str
    title: str
    subtitle: str
    image_url: str
    image_alt_text: str
    image_credit: Optional[str] = None
    button_text: str
    button_link: str
    display_order: int

    model_config = ConfigDict(from_attributes=True)

