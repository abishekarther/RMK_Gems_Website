import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.core.database import Base, engine
from backend.app.seed.seed_data import seed_database

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    seed_database()

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_list_categories():
    response = client.get("/api/v1/categories")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) >= 2
    slugs = [c["slug"] for c in categories]
    assert "precious" in slugs
    assert "semi-precious" in slugs

def test_list_gemstones():
    response = client.get("/api/v1/gemstones?page_size=100")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert data["total"] > 0
    
    # Internal fields must NOT be in public response
    for item in data["items"]:
        assert "source_notes" not in item
        assert "needs_client_confirmation" not in item
        assert "name" in item
        assert "slug" in item

def test_filter_by_category():
    # Test precious gemstones filter
    response = client.get("/api/v1/gemstones?category=precious&page_size=50")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 9  # All 9 precious stones
    for item in data["items"]:
        assert item["category_slug"] == "precious"

def test_search_gemstones():
    response = client.get("/api/v1/gemstones?search=ruby")
    assert response.status_code == 200
    data = response.json()
    assert any("Ruby" in item["name"] for item in data["items"])

def test_get_gemstone_detail_ruby():
    response = client.get("/api/v1/gemstones/ruby")
    assert response.status_code == 200
    gem = response.json()
    assert gem["name"] == "Ruby"
    assert gem["category_slug"] == "precious"
    assert gem["hardness_min"] == 9.0
    assert "Al2O3" in gem["chemical_composition"]
    # Check that internal fields are excluded
    assert "source_notes" not in gem
    assert "needs_client_confirmation" not in gem

def test_get_gemstone_detail_404_for_unknown():
    response = client.get("/api/v1/gemstones/non-existent-gemstone-slug-xyz")
    assert response.status_code == 404

def test_get_gemstone_detail_404_for_unpublished():
    # Goldstone sandstone blue has needs_client_confirmation=True, is_published=False
    response = client.get("/api/v1/gemstones/goldstone-sandstone-blue")
    assert response.status_code == 404

def test_homepage_slides():
    response = client.get("/api/v1/home/slides")
    assert response.status_code == 200
    slides = response.json()
    assert len(slides) == 5
    # Verify titles and 5-slide images
    titles = [s["title"] for s in slides]
    assert "RMK Gems Collection" in titles
    assert "Ruby — The King of Gemstones" in titles
    assert "Emerald — Nature's Green Treasure" in titles
    assert "Blue Sapphire — The Stone of Royalty" in titles
    assert "The Journey of a Gemstone" in titles
    assert [s["image_url"] for s in slides] == [
        "/images/slides/slide-1.jpg",
        "/images/slides/slide-2.jpg",
        "/images/slides/slide-3.jpg",
        "/images/slides/slide-4.jpg",
        "/images/slides/slide-5.jpg",
    ]

def test_shop_settings():
    response = client.get("/api/v1/shop")
    assert response.status_code == 200
    shop = response.json()
    assert shop["shop_name"] == "RMK Gems"
    assert shop["phone"] == "+91 93857 06450"
    assert shop["whatsapp_number"] == "919385706450"
    assert "Tenkasi" in shop["city"]
    assert "All-India delivery" in shop["delivery_description"]
    assert "specializes in sourcing, crafting and delivering gemstones" in shop["about_description"]

def test_opening_hours():
    response = client.get("/api/v1/shop/hours")
    assert response.status_code == 200
    hours = response.json()
    assert len(hours) >= 7

    # Check Tuesday is confirmed with client-provided hours
    tuesday = next(h for h in hours if h["day_of_week"] == "Tuesday")
    assert tuesday["is_confirmed"] is True
    assert tuesday["opening_time"] == "10:30"
    assert tuesday["closing_time"] == "21:00"

    # Check Friday has 2 intervals
    friday_intervals = [h for h in hours if h["day_of_week"] == "Friday"]
    assert len(friday_intervals) == 2
    assert friday_intervals[0]["opening_time"] == "10:30"
    assert friday_intervals[0]["closing_time"] == "12:30"
    assert friday_intervals[1]["opening_time"] == "16:00"
    assert friday_intervals[1]["closing_time"] == "21:00"

    # Check Sunday is closed
    sunday = next(h for h in hours if h["day_of_week"] == "Sunday")
    assert sunday["is_closed"] is True

