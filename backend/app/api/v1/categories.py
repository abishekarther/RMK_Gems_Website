from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.category import GemstoneCategory
from backend.app.schemas.category import CategoryPublic

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("", response_model=List[CategoryPublic])
def list_categories(db: Session = Depends(get_db)):
    """List active gemstone categories."""
    categories = db.query(GemstoneCategory).filter(GemstoneCategory.is_active == True).order_by(GemstoneCategory.display_order.asc()).all()
    return categories

