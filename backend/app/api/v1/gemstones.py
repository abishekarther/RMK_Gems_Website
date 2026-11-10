import math
from typing import Optional, List
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from backend.app.core.database import get_db
from backend.app.models.gemstone import Gemstone
from backend.app.models.category import GemstoneCategory
from backend.app.schemas.gemstone import (
    GemstoneListPublic,
    GemstoneDetailPublic,
    PaginatedGemstonesPublic,
)

router = APIRouter(prefix="/gemstones", tags=["Gemstones"])

@router.get("", response_model=PaginatedGemstonesPublic)
def list_gemstones(
    category: Optional[str] = Query(None, description="Category slug: precious or semi-precious"),
    search: Optional[str] = Query(None, description="Search gemstone name"),
    availability: Optional[str] = Query(None, description="Filter by availability status"),
    is_featured: Optional[bool] = Query(None, description="Filter featured gemstones"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(24, ge=1, le=100, description="Page size (capped at 100)"),
    db: Session = Depends(get_db),
):
    """List published gemstones with filtering and pagination."""
    query = db.query(Gemstone).filter(Gemstone.is_published == True)

    if category:
        cat = db.query(GemstoneCategory).filter(GemstoneCategory.slug == category).first()
        if cat:
            query = query.filter(Gemstone.category_id == cat.id)
        else:
            return PaginatedGemstonesPublic(items=[], total=0, page=page, page_size=page_size, total_pages=0)

    if search:
        query = query.filter(Gemstone.name.ilike(f"%{search.strip()}%"))

    if availability:
        query = query.filter(Gemstone.availability == availability)

    if is_featured is not None:
        query = query.filter(Gemstone.is_featured == is_featured)

    total = query.count()
    total_pages = math.ceil(total / page_size) if total > 0 else 0

    items_db = (
        query.order_by(Gemstone.display_order.asc(), Gemstone.name.asc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    items = []
    for g in items_db:
        cat_slug = g.category.slug if g.category else None
        item_data = GemstoneListPublic(
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
        items.append(item_data)

    return PaginatedGemstonesPublic(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )

@router.get("/{slug}", response_model=GemstoneDetailPublic)
def get_gemstone(slug: str, db: Session = Depends(get_db)):
    """Get single published gemstone by slug. Returns 404 for unknown or unpublished stones."""
    gemstone = (
        db.query(Gemstone)
        .filter(Gemstone.slug == slug, Gemstone.is_published == True)
        .first()
    )

    if not gemstone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Gemstone with slug '{slug}' not found or is currently not published.",
        )

    cat_slug = gemstone.category.slug if gemstone.category else None
    cat_name = gemstone.category.name if gemstone.category else None

    return GemstoneDetailPublic(
        id=gemstone.id,
        category_id=gemstone.category_id,
        category_slug=cat_slug,
        category_name=cat_name,
        name=gemstone.name,
        slug=gemstone.slug,
        short_description=gemstone.short_description,
        full_description=gemstone.full_description,
        material_type=gemstone.material_type,
        colour=gemstone.colour,
        hardness_min=gemstone.hardness_min,
        hardness_max=gemstone.hardness_max,
        chemical_composition=gemstone.chemical_composition,
        crystal_system=gemstone.crystal_system,
        origin=gemstone.origin,
        formation=gemstone.formation,
        history_notes=gemstone.history_notes,
        treatments=gemstone.treatments,
        care_instructions=gemstone.care_instructions,
        availability=gemstone.availability,
        is_featured=gemstone.is_featured,
        display_order=gemstone.display_order,
        created_at=gemstone.created_at,
        updated_at=gemstone.updated_at,
        media=[m for m in gemstone.media],
    )

