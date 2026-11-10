from fastapi import APIRouter
from backend.app.api.v1.categories import router as categories_router
from backend.app.api.v1.gemstones import router as gemstones_router
from backend.app.api.v1.slides import router as slides_router
from backend.app.api.v1.shop import router as shop_router

api_router = APIRouter()
api_router.include_router(categories_router)
api_router.include_router(gemstones_router)
api_router.include_router(slides_router)
api_router.include_router(shop_router)

