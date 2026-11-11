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
  
  // Confirmed Google Maps links
  mapSearchUrl: "https://www.google.com/maps/search/?api=1&query=No.%2012%2C%20Arafath%20Complex%2C%20Keela%20Avani%20Moola%20Veethi%2C%20Near%20Theppakulam%2C%20Tenkasi%20627811%2C%20Tamil%20Nadu%2C%20India",
  directionsUrl: "https://www.google.com/maps/dir/?api=1&destination=No.%2012%2C%20Arafath%20Complex%2C%20Keela%20Avani%20Moola%20Veethi%2C%20Near%20Theppakulam%2C%20Tenkasi%20627811%2C%20Tamil%20Nadu%2C%20India",
  embeddedMapUrl: "https://maps.google.com/maps?q=Keela+Avani+Moola+Veethi,+Tenkasi,+Tamil+Nadu+627811&t=m&z=15&ie=UTF8&output=embed",
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

