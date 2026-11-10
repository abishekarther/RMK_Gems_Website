import type {
  GemstoneItem,
  GemstoneDetail,
  PaginatedGemstones,
  HomepageSlide,
  ShopSettings,
  OpeningHour,
} from '../types/gemstone';
import {
  FALLBACK_SLIDES,
  FALLBACK_HOURS,
  FALLBACK_GEMSTONES,
} from '../data/gemstoneFallbackData';
import { SHOP_CONFIG } from '../config/shop';

const API_BASE = '/api/v1';

export async function fetchCategories(): Promise<{ id: string; name: string; slug: string; description: string }[]> {
  try {
    const res = await fetch(`${API_BASE}/categories`);
    if (!res.ok) throw new Error('Failed to fetch categories');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching categories; using fallback:', err);
    return [
      {
        id: 'cat-precious',
        name: 'Precious Gemstones',
        slug: 'precious',
        description: 'Timeless precious gemstones revered through history for rarity, exceptional brilliance, and enduring cultural prestige.',
      },
      {
        id: 'cat-semi-precious',
        name: 'Semi-Precious Gemstones',
        slug: 'semi-precious',
        description: 'A diverse panorama of fine natural minerals and ornamental gems displaying captivating crystal forms, rich hues, and optical chatoyancy.',
      },
    ];
  }
}

export async function fetchGemstones(params?: {
  category?: string;
  search?: string;
  availability?: string;
  is_featured?: boolean;
  page?: number;
  page_size?: number;
}): Promise<PaginatedGemstones> {
  const query = new URLSearchParams();
  if (params?.category) query.append('category', params.category);
  if (params?.search) query.append('search', params.search);
  if (params?.availability) query.append('availability', params.availability);
  if (params?.is_featured !== undefined) query.append('is_featured', String(params.is_featured));
  if (params?.page) query.append('page', String(params.page));
  if (params?.page_size) query.append('page_size', String(params.page_size));

  try {
    const res = await fetch(`${API_BASE}/gemstones?${query.toString()}`);
    if (!res.ok) throw new Error('Failed to fetch gemstones');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching gemstones; using fallback:', err);
    let filtered = [...FALLBACK_GEMSTONES];

    if (params?.category) {
      filtered = filtered.filter((g) => g.category_slug === params.category);
    }
    if (params?.search) {
      const s = params.search.toLowerCase();
      filtered = filtered.filter((g) => g.name.toLowerCase().includes(s));
    }
    if (params?.is_featured !== undefined) {
      filtered = filtered.filter((g) => g.is_featured === params.is_featured);
    }

    const pageSize = params?.page_size || 24;
    const page = params?.page || 1;
    const total = filtered.length;
    const totalPages = Math.ceil(total / pageSize);
    const start = (page - 1) * pageSize;
    const items = filtered.slice(start, start + pageSize);

    return {
      items,
      total,
      page,
      page_size: pageSize,
      total_pages: totalPages,
    };
  }
}

export async function fetchGemstoneBySlug(slug: string): Promise<GemstoneDetail | null> {
  try {
    const res = await fetch(`${API_BASE}/gemstones/${encodeURIComponent(slug)}`);
    if (res.status === 404) return null;
    if (!res.ok) throw new Error('Failed to fetch gemstone detail');
    return await res.json();
  } catch (err) {
    console.warn(`API error fetching gemstone ${slug}; checking fallback:`, err);
    const found = FALLBACK_GEMSTONES.find((g) => g.slug === slug);
    return found || null;
  }
}

export async function fetchHomepageSlides(): Promise<HomepageSlide[]> {
  try {
    const res = await fetch(`${API_BASE}/home/slides`);
    if (!res.ok) throw new Error('Failed to fetch slides');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching slides; using fallback:', err);
    return FALLBACK_SLIDES;
  }
}

export async function fetchFeaturedGemstones(): Promise<GemstoneItem[]> {
  try {
    const res = await fetch(`${API_BASE}/home/featured`);
    if (!res.ok) throw new Error('Failed to fetch featured gemstones');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching featured; using fallback:', err);
    return FALLBACK_GEMSTONES.filter((g) => g.is_featured);
  }
}

export async function fetchShopSettings(): Promise<ShopSettings> {
  try {
    const res = await fetch(`${API_BASE}/shop`);
    if (!res.ok) throw new Error('Failed to fetch shop settings');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching shop settings; using fallback:', err);
    return {
      shop_name: SHOP_CONFIG.shopName,
      phone: SHOP_CONFIG.phoneDisplay,
      whatsapp_number: SHOP_CONFIG.whatsappNumber,
      address: SHOP_CONFIG.address,
      city: SHOP_CONFIG.city,
      state: SHOP_CONFIG.state,
      postal_code: SHOP_CONFIG.postalCode,
      delivery_description: SHOP_CONFIG.deliveryStatement,
      map_url: SHOP_CONFIG.mapSearchUrl,
      directions_url: SHOP_CONFIG.directionsUrl,
      about_description: SHOP_CONFIG.aboutDescription,
    };
  }
}

export async function fetchOpeningHours(): Promise<OpeningHour[]> {
  try {
    const res = await fetch(`${API_BASE}/shop/hours`);
    if (!res.ok) throw new Error('Failed to fetch opening hours');
    return await res.json();
  } catch (err) {
    console.warn('API error fetching opening hours; using fallback:', err);
    return FALLBACK_HOURS;
  }
}
