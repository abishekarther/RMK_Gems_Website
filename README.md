# RMK Gems — Official Website & 3D Gemstone Catalogue

Premium, responsive catalogue and WhatsApp enquiry website for **RMK Gems**, located in Tenkasi, Tamil Nadu, India. Built to specification v1.1.

---

## 💎 Features & System Architecture

### 1. Light-Luxury Brand & Visual Identity
- **Palette**: Warm ivory / soft white (`#FAF8F5`), champagne gold (`#997A48`, `#C5A880`), deep charcoal typography (`#1E1E1E`), subtle gemstone accents. Meets WCAG AA contrast standards.
- **Typography**: Serif headlines (*Playfair Display* & *Cormorant Garamond*) paired with modern sans-serif body (*Plus Jakarta Sans*).
- **All-India Delivery**: Statement featured prominently across header, contact, detail pages, and footer.

### 2. 3D Gemstone Discovery Experience
- Built with **Three.js**, **React Three Fiber**, and **@react-three/drei**.
- Authentic multi-faceted procedural gemstone geometries:
  - **Round Brilliant Cut** (Diamond, White Topaz, Rock Crystal)
  - **Emerald Step Cut** (Emerald, Green Tourmaline)
  - **Oval Cut** (Ruby, Blue Sapphire, Almandine Garnet, Amethyst)
  - **Cushion Cut** (Yellow Sapphire, Hessonite Garnet, Rose Quartz, Citrine, Smoky Quartz)
  - **Cabochon** (Cat's Eye Chrysoberyl, Red Coral, Lapis, Turquoise, Moonstone, Malachite, Tiger Eye)
  - **Pearl** (Iridescent nacre sphere)
- **Continuous slow idle rotation** with hover/touch illumination and gemstone name reveal.
- **Detail Page Studio**: Interactive 3D viewer with 360-degree drag rotation, zoom controls, and pause/play toggle.
- **WebGL Context Limit Safe**: Uses in-viewport lazy rendering with IntersectionObserver so large galleries (up to 59+ items) never exceed mobile or browser WebGL context limits.
- **Representative Model Notice**: Discreetly displayed per specification ("Representative 3D model; actual natural gemstones vary in colour and cut").

### 3. Five-Slide Gemstone History Carousel
- Editorial sequence focused entirely on **gemstone historical significance** (not shop history):
  1. *The Story of Gemstones*
  2. *Treasured Through Time*
  3. *The Legacy of Ruby and Sapphire*
  4. *Emeralds, Diamonds and Royal Heritage*
  5. *Discover the Gemstone World*
- Autoplay with accessible pause/play toggle, slide indicators, keyboard navigation, and `prefers-reduced-motion` support.

### 4. Direct WhatsApp Click-to-Chat Integration
- Instant WhatsApp link pre-filled with the exact required enquiry template:
  ```text
  Hello RMK Gems,
  I am interested in [GEMSTONE NAME].
  Please share its available types, sizes, weight, quality, price and availability.
  Thank you.
  ```
- Uses verified international number: `+91 93857 06450` (`wa.me/919385706450`).

### 5. Verified Shop Information & Opening Hours
- **Address**: No. 12, Arafath Complex, Keela Avani Moola Veethi, Near Theppakulam, Tenkasi – 627811, Tamil Nadu, India.
- **Opening Hours**:
  - Monday, Wednesday, Thursday, Saturday: 10:30 AM – 9:00 PM
  - Tuesday: Displayed clearly as *"Please contact the shop to confirm"* (`is_confirmed: false`)
  - Friday: Two distinct operating periods: 10:30 AM – 12:30 PM and 4:00 PM – 9:00 PM
  - Sunday: Closed
- **Directions & Map**: Google Maps directions link, search link, and lazy-loaded interactive embedded map.

### 6. Strict Scope & Privacy Safeguards
- **No Admin Dashboard**: Explicitly excluded; no `/admin` routes or interfaces.
- **No Public Price Display**: Prices are kept private and provided on WhatsApp enquiry.
- **No Tamil Names / No "Why Choose" Sections**: Kept concise, factual, and gemologically verified.
- **Internal Gemological Notes**: Source notes and verification flags (`needs_client_confirmation`) are strictly excluded from all public API outputs.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS v4, React Router v7, Three.js, React Three Fiber, Drei, Lucide Icons |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy, Pydantic v2, SQLite (zero-config local) / PostgreSQL compatible |
| **Testing** | Pytest, HTTPX, TypeScript (`tsc -b`), Vite Build |

---

## 🚀 Quick Start Guide

### 1. Run the Backend API
```bash
# Activate virtual environment
backend\venv\Scripts\activate

# Run FastAPI server (defaults to port 8000 with auto-seeding)
python -m uvicorn backend.app.main:app --reload --port 8000
```
- API Docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/api/v1/health`

### 2. Run the Frontend Development Server
```bash
cd frontend
npm install
npm run dev
```
- Frontend application runs at: `http://localhost:5173`

### 3. Run Automated Tests
```bash
# Run backend pytest suite (11 test cases)
backend\venv\Scripts\python -m pytest backend/tests/test_api.py -v

# Run frontend TypeScript & production build check
cd frontend
npm run build
```

---

## 📁 Project Structure

```text
RMK_Gems_Website/
├── backend/
│   ├── app/
│   │   ├── api/v1/          # Categories, Gemstones, Slides, Shop endpoints
│   │   ├── core/            # App settings, database configuration
│   │   ├── models/          # SQLAlchemy ORM models
│   │   ├── schemas/         # Pydantic validation schemas (internal fields withheld)
│   │   ├── seed/            # GIA/Mindat researched seed data (68 gemstones)
│   │   └── main.py          # FastAPI application & lifecycle management
│   ├── tests/               # Pytest suite
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   ├── public/              # Favicon, robots.txt, sitemap.xml
│   ├── src/
│   │   ├── app/             # App root and router configuration
│   │   ├── components/      # Header, Footer, 3D Canvas, ScrollToTop
│   │   │   └── Gemstone3D/  # Three.js geometries, shaders & interactive viewer
│   │   ├── config/          # Central shop settings & WhatsApp builders
│   │   ├── data/            # Resilient offline/fallback dataset
│   │   ├── pages/           # Home, Precious, Semi-Precious, Detail, Contact, 404
│   │   ├── sections/        # Hero carousel, categories, featured, location
│   │   ├── services/        # Central API client
│   │   └── types/           # TypeScript definitions
│   ├── package.json
│   └── vite.config.ts
└── package.json             # Root runner scripts
```

---

## 📋 Client Confirmations Checklist (Section 14)

The website is fully functional with realistic 3D representations, research-backed gemological data, and labelled placeholders where appropriate. The following items remain open for final client sign-off:

1. [ ] **Official Logo**: Text wordmark "RMK Gems" is implemented. Can be swapped with custom vector emblem if provided.
2. [ ] **Tuesday Opening Hours**: Displayed as *"Please contact the shop to confirm"*.
3. [ ] **WhatsApp Number Activation**: Confirmed active on `+91 9385706450`.
4. [ ] **Google Maps Verified Pin**: Address search coordinates currently used; exact Google Place ID can be plugged in when verified.
5. [ ] **Catalogue Overlaps Sign-off**: 9 precious stones and 50 confirmed semi-precious stones are published; 9 ambiguous trade entries (`Goldstone`, `Ruby Markara`, duplicate `Hessonite`, etc.) are flagged with `needs_client_confirmation` and safely unlisted until confirmed.

