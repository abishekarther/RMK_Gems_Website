import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { SHOP_CONFIG } from '../../config/shop';

interface LeafletMapProps {
  className?: string;
}

export const LeafletMap: React.FC<LeafletMapProps> = ({ className = 'w-full h-full' }) => {
  const mapContainerRef = useRef<HTMLDivElement | null>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);

  useEffect(() => {
    if (!mapContainerRef.current || mapInstanceRef.current) return;

    const lat = SHOP_CONFIG.latitude;
    const lng = SHOP_CONFIG.longitude;

    // Initialize Leaflet map centered exactly at verified shop coordinates
    const map = L.map(mapContainerRef.current, {
      center: [lat, lng],
      zoom: 16,
      zoomControl: true,
      scrollWheelZoom: false, // Prevents map from trapping page scroll
    });

    mapInstanceRef.current = map;

    // High-resolution OpenStreetMap tile layer
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a>',
    }).addTo(map);

    // Custom luxury gold & charcoal jewel pin marker
    const goldMarkerIcon = L.divIcon({
      className: 'custom-rmk-marker',
      html: `
        <div style="position: relative; width: 34px; height: 42px; display: flex; align-items: center; justify-content: center; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.35)); cursor: pointer;">
          <svg width="34" height="42" viewBox="0 0 34 42" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 0C7.61116 0 0 7.61116 0 17C0 27.5 17 42 17 42C17 42 34 27.5 34 17C34 7.61116 26.3888 0 17 0Z" fill="#997A48"/>
            <path d="M17 2C8.71573 2 2 8.71573 2 17C2 26.2 17 39.5 17 39.5C17 39.5 32 26.2 32 17C32 8.71573 25.2843 2 17 2Z" fill="#1E1E1E"/>
            <circle cx="17" cy="16" r="7" fill="#C5A880"/>
            <polygon points="17,12 21,16 17,20 13,16" fill="#1E1E1E"/>
          </svg>
        </div>
      `,
      iconSize: [34, 42],
      iconAnchor: [17, 42],
      popupAnchor: [0, -38],
    });

    const marker = L.marker([lat, lng], { icon: goldMarkerIcon }).addTo(map);

    // Styled popup showing shop details and Google Maps external navigation link
    const popupContent = `
      <div style="font-family: inherit; padding: 4px 2px; min-width: 180px;">
        <div style="font-weight: 700; color: #997A48; font-size: 13px; letter-spacing: 0.05em; text-transform: uppercase;">RMK GEMS</div>
        <div style="font-size: 11px; color: #1E1E1E; font-weight: 500; margin-top: 2px;">No. 12, Arafath Complex</div>
        <div style="font-size: 11px; color: #666; margin-top: 1px;">Keela Avani Moola Veethi, Tenkasi</div>
        <a href="${SHOP_CONFIG.mapSearchUrl}" target="_blank" rel="noopener noreferrer" style="display: inline-block; margin-top: 8px; font-size: 11px; font-weight: 600; color: #997A48; text-decoration: underline;">
          Open in Google Maps &rarr;
        </a>
      </div>
    `;

    marker.bindPopup(popupContent).openPopup();

    // Recalculate size after container layout completes
    const timer = setTimeout(() => {
      map.invalidateSize();
    }, 200);

    return () => {
      clearTimeout(timer);
      map.remove();
      mapInstanceRef.current = null;
    };
  }, []);

  return <div ref={mapContainerRef} className={className} />;
};

