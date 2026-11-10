import React from 'react';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { Header } from '../components/Header/Header';
import { Footer } from '../components/Footer/Footer';
import { ScrollToTop } from '../components/ScrollToTop';
import { HomePage } from '../pages/HomePage';
import { PreciousGemstonesPage } from '../pages/PreciousGemstonesPage';
import { SemiPreciousGemstonesPage } from '../pages/SemiPreciousGemstonesPage';
import { GemstoneDetailPage } from '../pages/GemstoneDetailPage';
import { ContactPage } from '../pages/ContactPage';
import { NotFoundPage } from '../pages/NotFoundPage';

const AppContent: React.FC = () => {
  const location = useLocation();

  // Hide footer on: Precious Gemstones, Semi-Precious Gemstones, Contact, and inside every gemstone detail page
  const hideFooterRoutes = [
    '/precious-gemstones',
    '/semi-precious-gemstones',
    '/contact',
  ];

  const shouldHideFooter =
    hideFooterRoutes.includes(location.pathname) ||
    location.pathname.startsWith('/gemstones');

  return (
    <div className="flex flex-col min-h-screen bg-[#FAF8F5] text-[#1E1E1E]">
      <Header />
      <div className="flex-1">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/precious-gemstones" element={<PreciousGemstonesPage />} />
          <Route path="/semi-precious-gemstones" element={<SemiPreciousGemstonesPage />} />
          <Route path="/gemstones/:slug" element={<GemstoneDetailPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </div>
      {!shouldHideFooter && <Footer />}
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <BrowserRouter>
      <ScrollToTop />
      <AppContent />
    </BrowserRouter>
  );
};
