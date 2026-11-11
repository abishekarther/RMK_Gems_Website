export const SHOP_CONFIG = {
  shopName: "RMK Gems",
  phoneDisplay: "+91 93857 06450",
  phoneRaw: "9385706450",
  phoneTel: "+919385706450",
  whatsappNumber: "919385706450",
  address: "No. 12, Arafath Complex, Keela Avani Moola Veethi, Near Theppakulam, Tenkasi – 627811, Tamil Nadu, India.",
  city: "Tenkasi",
  state: "Tamil Nadu",
  postalCode: "627811",
  deliveryStatement: "All-India delivery is offered on all gemstones.",
  aboutDescription: "RMK Gems specializes in sourcing, crafting and delivering gemstones, with a focus on quality, authenticity and natural beauty.",
  
  // Verified Google Maps coordinates (https://maps.app.goo.gl/8FnGYe95aAVwfCVJA)
  latitude: 8.9576002,
  longitude: 77.3094673,

  // Confirmed Google Maps links for external navigation
  mapSearchUrl: "https://maps.app.goo.gl/8FnGYe95aAVwfCVJA",
  directionsUrl: "https://www.google.com/maps/dir/?api=1&destination=8.9576002,77.3094673",
};

/**
 * Creates the exact WhatsApp enquiry URL as specified in Section 10.
 * Pre-filled message asks for available types, sizes, weight, quality, price and availability.
 */
export function createWhatsAppEnquiry(gemstoneName: string, phone: string = SHOP_CONFIG.whatsappNumber): string {
  const message = [
    "Hello RMK Gems,",
    `I am interested in ${gemstoneName}.`,
    "Please share its available types, sizes, weight, quality, price and availability.",
    "Thank you."
  ].join("\n");

  return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

/**
 * Creates a general WhatsApp enquiry link for general customer enquiries.
 */
export function createGeneralWhatsAppEnquiry(phone: string = SHOP_CONFIG.whatsappNumber): string {
  const message = [
    "Hello RMK Gems,",
    "I would like to enquire about your precious and semi-precious gemstone collection.",
    "Thank you."
  ].join("\n");

  return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

