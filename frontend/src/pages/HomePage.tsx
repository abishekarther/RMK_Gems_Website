import React from 'react';
import { HeroCarousel } from '../sections/HeroCarousel/HeroCarousel';
import { CategorySelection } from '../sections/CategorySelection/CategorySelection';
import { LocationSection } from '../sections/LocationSection/LocationSection';
import { SEO } from '../components/SEO';

const homeSchema = {
  "@context": "https://schema.org",
  "@type": "JewelryStore",
  "name": "RMK Gems",
  "url": "https://rmkgems.in",
  "logo": "https://rmkgems.in/gem-icon.svg",
  "image": "https://rmkgems.in/images/slides/slide-1.jpg",
  "description": "RMK Gems specializes in sourcing, crafting, and delivering authentic natural precious and semi-precious gemstones in Tenkasi, Tamil Nadu with all-India shipping.",
  "telephone": "+919385706450",
  "priceRange": "$$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "No. 12, Arafath Complex, Keela Avani Moola Veethi, Near Theppakulam",
    "addressLocality": "Tenkasi",
    "addressRegion": "Tamil Nadu",
    "postalCode": "627811",
    "addressCountry": "IN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 8.9593,
    "longitude": 77.3152
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday"],
      "opens": "10:30",
      "closes": "21:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "10:30",
      "closes": "12:30"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "16:00",
      "closes": "21:00"
    }
  ]
};

export const HomePage: React.FC = () => {
  return (
    <>
      <SEO
        title="RMK Gems — Natural Precious & Semi-Precious Gemstones in Tenkasi"
        description="Explore authentic precious and semi-precious gemstones at RMK Gems, Tenkasi. Fine Ruby, Emerald, Sapphire, Moonstone, and 50+ mineral varieties with pan-India delivery."
        canonical="/"
        ogImage="/images/slides/slide-1.jpg"
        schema={homeSchema}
      />
      <main>
        {/* 1. Five-Slide Gemstone History Carousel */}
        <HeroCarousel />

        {/* 2. Brand Statement & Values */}
        <LocationSection />

        {/* 3. Curated Gemstone Galleries (Precious & Semi-Precious) */}
        <CategorySelection />
      </main>
    </>
  );
};
