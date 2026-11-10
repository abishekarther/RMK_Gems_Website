# RMK Gems — Official Website & Gemstone Catalogue

Premium, responsive gemstone catalogue and WhatsApp enquiry website for **RMK Gems**, located in Tenkasi, Tamil Nadu, India. Built to specification v1.1 and refined to client preferences.

---

## 💎 Features & System Architecture

### 1. Light-Luxury Brand & Visual Identity
- **Palette**: Warm ivory / soft white (`#FAF8F5`), champagne gold (`#997A48`, `#C5A880`), deep charcoal typography (`#1E1E1E`). Meets WCAG AA contrast standards.
- **Typography**: Serif headlines (*Playfair Display* & *Cormorant Garamond*) paired with modern sans-serif body (*Plus Jakarta Sans*).
- **Brand Statement**: Styled in Cormorant Garamond luxury serif italics with All-India delivery reassurance.

### 2. Authentic Gemstone Photography (GIA Reference)
- High-resolution cut and polished gemstone photography sourced directly from the **GIA Gem Encyclopedia** (`https://www.gia.edu/gem-encyclopedia`).
- **Minimalist Stone Cards**: Clean, modern cards displaying **strictly the authentic stone photo and its name** — all badges, cut tags (`OVAL CUT • NATURAL`), and unwanted buttons have been removed for an uncluttered luxury feel.
- **Factual Gemological Properties**: Accurate Mohs hardness, chemical composition, crystal system, colour range, and care guidelines on every detail page.

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

### 5. Verified Shop Information & Visiting Hours
- **Address**: No. 12, Arafath Complex, Keela Avani Moola Veethi, Near Theppakulam, Tenkasi – 627811, Tamil Nadu, India.
- **Visiting Hours Schedule**:
  | Day | Timings |
  |---|---|
  | **Monday – Thursday, Saturday** | 10:30 AM – 9:00 PM |
  | **Friday** | 10:30 AM – 12:30 PM, 4:00 PM – 9:00 PM |
  | **Sunday** | Closed |
- **Dedicated Shop Visit Page (`/contact`)**: Centralizes the full physical address, confirmed schedule table, street-level Google Maps embed (`z=18`), directions, and direct customer care pillars.
- **Content Deduplication**: The shop address, timetable, and map grid were removed from the homepage to eliminate repetition; the homepage links seamlessly to the Shop Visit page.
- **Conditional Footer**: The universal footer is shown on the Homepage and Detail pages, and is cleanly hidden on the Precious Gemstones, Semi-Precious Gemstones, and Contact pages.

### 6. Strict Scope & Privacy Safeguards
- **No Admin Dashboard**: Explicitly excluded; no `/admin` routes or interfaces.
- **No Public Price Display**: Prices are kept private and provided on WhatsApp enquiry.
- **No Tamil Names / No "Why Choose" Sections**: Kept concise, factual, and gemologically verified.
- **Internal Gemological Notes**: Source notes and verification flags (`needs_client_confirmation`) are strictly excluded from all public API outputs.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS v4, React Router v7, Lucide Icons |
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
│   ├── tests/               # Pytest suite (11 passing tests)
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
├── frontend/
│   ├── public/              # Favicon, robots.txt, sitemap.xml, GIA gemstone photography
│   ├── src/
│   │   ├── app/             # App root, router, and conditional footer layout
│   │   ├── components/      # Header, Footer, GemstoneCard, ScrollToTop
│   │   ├── config/          # Central shop settings & WhatsApp builders
│   │   ├── data/            # Resilient offline/fallback dataset & GIA photos mapping
│   │   ├── pages/           # Home, Precious, Semi-Precious, Detail, Contact, 404
│   │   ├── sections/        # Hero carousel, categories, location/brand statement
│   │   ├── services/        # Central API client
│   │   └── types/           # TypeScript definitions
│   ├── package.json
│   └── vite.config.ts
└── package.json             # Root runner scripts
```
