export interface GemstoneMedia {
  id: string;
  media_type: 'image' | 'model_3d' | 'preview';
  file_url: string;
  thumbnail_url?: string;
  alt_text: string;
  display_order: number;
  is_primary: boolean;
}

export interface GemstoneItem {
  id: string;
  category_id: string;
  category_slug?: string;
  name: string;
  slug: string;
  short_description?: string | null;
  material_type?: string | null;
  colour?: string | null;
  hardness_min?: number | null;
  hardness_max?: number | null;
  availability: 'available' | 'on_request' | 'unconfirmed';
  is_featured: boolean;
  display_order: number;
  media: GemstoneMedia[];
  // Cut representation for 3D engine
  cut_style?: 'brilliant' | 'oval' | 'emerald' | 'cushion' | 'cabochon' | 'pearl';
  color_hex?: string;
}

export interface GemstoneDetail extends GemstoneItem {
  category_name?: string;
  full_description?: string | null;
  chemical_composition?: string | null;
  crystal_system?: string | null;
  origin?: string | null;
  formation?: string | null;
  history_notes?: string | null;
  treatments?: string | null;
  care_instructions?: string | null;
  created_at?: string;
  updated_at?: string;
}

export interface PaginatedGemstones {
  items: GemstoneItem[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export interface HomepageSlide {
  id: string;
  title: string;
  subtitle: string;
  image_url: string;
  image_alt_text: string;
  image_credit?: string;
  button_text: string;
  button_link: string;
  display_order: number;
}

export interface ShopSettings {
  shop_name: string;
  phone: string;
  whatsapp_number: string;
  address: string;
  city: string;
  state: string;
  postal_code: string;
  delivery_description: string;
  map_url: string;
  directions_url: string;
  about_description: string;
}

export interface OpeningHour {
  id: string;
  day_of_week: string;
  period_number: number;
  opening_time?: string;
  closing_time?: string;
  is_closed: boolean;
  is_confirmed: boolean;
  display_order: number;
}
