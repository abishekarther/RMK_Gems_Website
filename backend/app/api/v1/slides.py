from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.slide import HomepageSlide
from backend.app.models.gemstone import Gemstone
from backend.app.schemas.slide import HomepageSlidePublic
from backend.app.schemas.gemstone import GemstoneListPublic

router = APIRouter(prefix="/home", tags=["Homepage"])

@router.get("/slides", response_model=List[HomepageSlidePublic])
def get_homepage_slides(db: Session = Depends(get_db)):
    """Get active homepage slides focusing on gemstone history."""
    slides = (
        db.query(HomepageSlide)
        .filter(HomepageSlide.is_active == True)
        .order_by(HomepageSlide.display_order.asc())
        .all()
    )
    return slides

@router.get("/featured", response_model=List[GemstoneListPublic])
def get_featured_gemstones(db: Session = Depends(get_db)):
    """Get curated featured published gemstones."""
    featured = (
        db.query(Gemstone)
        .filter(Gemstone.is_published == True, Gemstone.is_featured == True)
        .order_by(Gemstone.display_order.asc())
        .limit(8)
        .all()
    )

    items = []
    for g in featured:
        cat_slug = g.category.slug if g.category else None
        items.append(
            GemstoneListPublic(
                id=g.id,
                category_id=g.category_id,
                category_slug=cat_slug,
                name=g.name,
                slug=g.slug,
                short_description=g.short_description,
                material_type=g.material_type,
                colour=g.colour,
                hardness_min=g.hardness_min,
                hardness_max=g.hardness_max,
                availability=g.availability,
                is_featured=g.is_featured,
                display_order=g.display_order,
                media=[m for m in g.media],
            )
        )
    return items

