import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
from backend.app.core.database import Base, engine
from backend.app.api.v1.router import api_router
from backend.app.seed.seed_data import seed_database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rmk_gems")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure tables and initial data exist
    logger.info("Initializing database tables and seed data...")
    Base.metadata.create_all(bind=engine)
    try:
        seed_database()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
    yield
    logger.info("Shutting down RMK Gems API.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for RMK Gems — Fine Gemstone Catalogue & WhatsApp Enquiry",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,  # No extra admin/dashboard docs needed
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.DEBUG else settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  # Read-only public API; no unapproved write methods
    allow_headers=["*"],
)

# Include v1 API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/api/v1/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)

