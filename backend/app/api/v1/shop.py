from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.shop import ShopSettings, OpeningHours
from backend.app.schemas.shop import ShopSettingsPublic, OpeningHourPublic

router = APIRouter(prefix="/shop", tags=["Shop"])

@router.get("", response_model=ShopSettingsPublic)
def get_shop_settings(db: Session = Depends(get_db)):
    """Get official RMK Gems business details, contact information, and map links."""
    shop = db.query(ShopSettings).first()
    if not shop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shop settings have not been configured.",
        )
    return shop

@router.get("/hours", response_model=List[OpeningHourPublic])
def get_opening_hours(db: Session = Depends(get_db)):
    """Get weekly opening hours, including dual Friday intervals and Tuesday unconfirmed flag."""
    hours = (
        db.query(OpeningHours)
        .order_by(OpeningHours.display_order.asc(), OpeningHours.period_number.asc())
        .all()
    )
    return hours

