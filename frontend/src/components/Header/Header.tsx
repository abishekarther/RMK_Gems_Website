import React, { useState } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Menu, X } from 'lucide-react';

export const Header: React.FC = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Precious Gemstones', path: '/precious-gemstones' },
    { name: 'Semi-Precious Gemstones', path: '/semi-precious-gemstones' },
    { name: 'Contact', path: '/contact' },
  ];

  return (
    <header className="sticky top-0 z-40 bg-[#FAF8F5]/90 backdrop-blur-md border-b border-[#E8E2D9]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          
          {/* Brand Wordmark (Section 4) */}
          <Link
            to="/"
            className="flex flex-col group focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48] rounded-sm py-1"
            aria-label="RMK Gems Home"
          >
            <span className="font-serif text-2xl sm:text-3xl font-bold tracking-wider text-[#1E1E1E] group-hover:text-[#997A48] transition-colors">
              RMK GEMS
            </span>
            <span className="text-[10px] uppercase tracking-[0.25em] text-[#717171] -mt-1 font-sans">
              Tenkasi • Fine Gemstones
            </span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8" aria-label="Main Navigation">
            {navLinks.map((link) => (
              <NavLink
                key={link.path}
                to={link.path}
                className={({ isActive }) =>
                  `text-sm font-medium tracking-wide transition-colors duration-200 relative py-1 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48] rounded ${
                    isActive
                      ? 'text-[#997A48] font-semibold after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-[#997A48]'
                      : 'text-[#4A4A4A] hover:text-[#1E1E1E]'
                  }`
                }
              >
                {link.name}
              </NavLink>
            ))}
          </nav>

          {/* Mobile Menu Button */}
          <div className="flex md:hidden items-center">
            <button
              type="button"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 text-[#4A4A4A] hover:text-[#1E1E1E] focus:outline-none focus:ring-2 focus:ring-[#997A48] rounded-md"
              aria-label="Toggle Navigation Menu"
              aria-expanded={mobileMenuOpen}
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="md:hidden bg-[#FAF8F5] border-b border-[#E8E2D9] px-4 pt-2 pb-6 space-y-3">
          {navLinks.map((link) => (
            <NavLink
              key={link.path}
              to={link.path}
              onClick={() => setMobileMenuOpen(false)}
              className={({ isActive }) =>
                `block px-3 py-2 text-base font-medium rounded-md transition-colors ${
                  isActive
                    ? 'text-[#997A48] bg-[#F4EFE6] font-semibold'
                    : 'text-[#4A4A4A] hover:text-[#1E1E1E] hover:bg-[#F4EFE6]/50'
                }`
              }
            >
              {link.name}
            </NavLink>
          ))}
        </div>
      )}
    </header>
  );
};
