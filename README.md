# RMK Gems — Official Website & Gemstone Catalogue

Premium, responsive gemstone catalogue and WhatsApp enquiry website for **RMK Gems**, located in Tenkasi, Tamil Nadu, India.

---

## 💎 Features & System Architecture

### 1. Light-Luxury Brand & Visual Identity
- **Palette**: Warm ivory / soft white (`#FAF8F5`), champagne gold (`#997A48`, `#C5A880`), deep charcoal typography (`#1E1E1E`). Meets WCAG AA contrast standards.
- **Typography**: Serif headlines (*Playfair Display* & *Cormorant Garamond*) paired with modern sans-serif body (*Plus Jakarta Sans*).
- **Brand Statement**: Styled in Cormorant Garamond luxury serif italics with All-India delivery reassurance.

### 2. Curated Gemstone Photography
- **All 68 Gemstones**: Complete coverage across 9 precious gemstones and 59 semi-precious gemstones.
- **Unified Location**: All photography resides centrally in `frontend/public/images/stones/<slug>.png`. Sourcing, provenance, and curatorial standards are documented in `frontend/public/images/stones/CREDITS.md`.
- **Minimalist Stone Cards**: Clean, modern cards displaying strictly the stone photograph and its name.
- **Factual Gemological Properties**: Accurate Mohs hardness, chemical composition, crystal system, colour range, and care guidelines on every detail page.

### 3. Five-Slide Gemstone History Carousel
- Editorial sequence focused entirely on **gemstone historical significance**:
  1. *The Story of Gemstones*
  2. *Treasured Through Time*
  3. *The Legacy of Ruby and Sapphire*
  4. *Emeralds, Diamonds and Royal Heritage*
  5. *Discover the Gemstone World*
- Autoplay with accessible pause/play toggle, slide indicators, keyboard navigation, and `prefers-reduced-motion` support. Located in `frontend/public/images/slides/`.

### 4. Direct WhatsApp Click-to-Chat Integration
- Instant WhatsApp link pre-filled with the exact required enquiry template:
  ```text
  Hello RMK Gems,
  I am interested in [GEMSTONE NAME].
  Please share its available types, sizes, weight, quality, price and availability.
  Thank you.
  ```
- Uses verified international number: `+91 93857 06450` (`wa.me/919385706450`).

### 5. Verified Shop Information & Visiting Hours
- **Address**: No. 12, Arafath Complex, Keela Avani Moola Veethi, Near Theppakulam, Tenkasi – 627811, Tamil Nadu, India.
- **Visiting Hours Schedule**:
  | Day | Timings |
  |---|---|
  | **Monday – Thursday, Saturday** | 10:30 AM – 9:00 PM |
  | **Friday** | 10:30 AM – 12:30 PM, 4:00 PM – 9:00 PM |
  | **Sunday** | Closed |
- **Dedicated Shop Visit Page (`/contact`)**: Centralizes the full physical address, confirmed schedule table, interactive Leaflet.js map with verified coordinates (`8.9576, 77.3095`), directions, and direct customer care pillars.
- **Conditional Footer**: Displayed on the Homepage and Detail pages, cleanly hidden on catalogue list pages and Contact page.

### 6. Strict Scope & Privacy Safeguards
- **No Admin Dashboard**: Explicitly excluded; no `/admin` routes or interfaces.
- **No Public Price Display**: Prices are kept private and provided on WhatsApp enquiry.
- **No Tamil Names / No "Why Choose" Sections**: Kept concise, factual, and gemologically verified.
- **Internal Gemological Notes**: Source notes and verification flags (`needs_client_confirmation`) are strictly excluded from all public API outputs.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS v4, React Router v7, Lucide Icons, Leaflet |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy, Pydantic v2, SQLite (zero-config local) / PostgreSQL compatible |
| **Testing & Quality** | Pytest, HTTPX, TypeScript (`tsc -b`), Oxlint, Vite Build |

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
│   │   ├── models/          # SQLAlchemy ORM models (Category, Gemstone, Media, Slide, Shop)
│   │   ├── schemas/         # Pydantic validation schemas (internal fields withheld)
│   │   ├── seed/            # Seed data (68 gemstones: 9 precious + 59 semi-precious)
│   │   └── main.py          # FastAPI application & lifecycle management
│   ├── tests/               # Pytest suite (11 passing tests)
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   ├── public/
│   │   ├── images/
│   │   │   ├── slides/      # 5 homepage hero carousel slides
│   │   │   └── stones/      # All 68 gemstone images (<slug>.png) & CREDITS.md
│   │   ├── favicon.svg      # Favicon
│   │   ├── robots.txt       # Search engine crawler instructions
│   │   └── sitemap.xml      # XML sitemap
│   ├── src/
│   │   ├── app/             # App root, router, and layout
│   │   ├── components/      # Header, Footer, GemstoneCard, LeafletMap, ScrollToTop
│   │   ├── config/          # Central shop settings & WhatsApp builders
│   │   ├── data/            # Resilient fallback dataset & gemstone photo registry
│   │   ├── pages/           # Home, Precious, Semi-Precious, Detail, Contact, 404
│   │   ├── sections/        # Hero carousel, categories, location/brand statement
│   │   ├── services/        # Central API client
│   │   └── types/           # TypeScript definitions
│   ├── package.json         # Frontend dependencies (React, Vite, Tailwind, Leaflet)
│   └── vite.config.ts       # Vite build configuration
├── rmk_gems.db              # SQLite development database
├── .gitignore               # Comprehensive Git ignore rules
└── package.json             # Root runner scripts
```
