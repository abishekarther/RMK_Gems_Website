import React, { useEffect } from 'react';

export interface SEOProps {
  title?: string;
  description?: string;
  canonical?: string;
  ogImage?: string;
  ogType?: 'website' | 'article' | 'product';
  schema?: Record<string, any>;
}

const DEFAULT_TITLE = 'RMK Gems — Fine Gemstone Catalogue & WhatsApp Enquiry | Tenkasi, Tamil Nadu';
const DEFAULT_DESCRIPTION = 'Discover natural and fine precious & semi-precious gemstones at RMK Gems, Tenkasi. Explore authentic polished gemstones and enquire directly via WhatsApp. All-India delivery available.';
const BASE_URL = 'https://rmkgems.com';
const DEFAULT_IMAGE = `${BASE_URL}/images/slides/slide-1.jpg`;

export const SEO: React.FC<SEOProps> = ({
  title,
  description,
  canonical,
  ogImage,
  ogType = 'website',
  schema,
}) => {
  const fullTitle = title
    ? `${title} | RMK Gems Tenkasi`
    : DEFAULT_TITLE;
  const metaDescription = description || DEFAULT_DESCRIPTION;
  const fullCanonical = canonical
    ? (canonical.startsWith('http') ? canonical : `${BASE_URL}${canonical}`)
    : BASE_URL;
  const fullImage = ogImage
    ? (ogImage.startsWith('http') ? ogImage : `${BASE_URL}${ogImage}`)
    : DEFAULT_IMAGE;

  useEffect(() => {
    // 1. Page Title
    document.title = fullTitle;

    // Helper to set or create meta tag
    const setMeta = (attr: 'name' | 'property', key: string, value: string) => {
      let element = document.querySelector(`meta[${attr}="${key}"]`) as HTMLMetaElement | null;
      if (!element) {
        element = document.createElement('meta');
        element.setAttribute(attr, key);
        document.head.appendChild(element);
      }
      element.setAttribute('content', value);
    };

    // 2. Standard Meta Tags
    setMeta('name', 'description', metaDescription);
    setMeta('name', 'robots', 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1');

    // 3. Canonical Link Tag
    let canonicalEl = document.querySelector('link[rel="canonical"]') as HTMLLinkElement | null;
    if (!canonicalEl) {
      canonicalEl = document.createElement('link');
      canonicalEl.setAttribute('rel', 'canonical');
      document.head.appendChild(canonicalEl);
    }
    canonicalEl.setAttribute('href', fullCanonical);

    // 4. Open Graph Tags
    setMeta('property', 'og:title', fullTitle);
    setMeta('property', 'og:description', metaDescription);
    setMeta('property', 'og:url', fullCanonical);
    setMeta('property', 'og:image', fullImage);
    setMeta('property', 'og:type', ogType);
    setMeta('property', 'og:site_name', 'RMK Gems');
    setMeta('property', 'og:locale', 'en_IN');

    // 5. Twitter Card Tags
    setMeta('name', 'twitter:card', 'summary_large_image');
    setMeta('name', 'twitter:title', fullTitle);
    setMeta('name', 'twitter:description', metaDescription);
    setMeta('name', 'twitter:image', fullImage);

    // 6. JSON-LD Page Schema
    const scriptId = 'page-json-ld';
    let scriptEl = document.getElementById(scriptId) as HTMLScriptElement | null;
    if (schema) {
      if (!scriptEl) {
        scriptEl = document.createElement('script');
        scriptEl.id = scriptId;
        scriptEl.type = 'application/ld+json';
        document.head.appendChild(scriptEl);
      }
      scriptEl.textContent = JSON.stringify(schema);
    } else if (scriptEl) {
      scriptEl.remove();
    }
  }, [fullTitle, metaDescription, fullCanonical, fullImage, ogType, schema]);

  return null;
};

