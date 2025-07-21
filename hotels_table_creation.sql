-- Create hotels table with comprehensive hotel information
CREATE TABLE IF NOT EXISTS hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    hotel_code VARCHAR(10) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    star_rating INTEGER CHECK (star_rating >= 1 AND star_rating <= 7),
    hotel_type VARCHAR(50) NOT NULL,
    chain VARCHAR(100),
    address TEXT NOT NULL,
    description TEXT,
    amenities TEXT,
    room_count INTEGER,
    base_price_per_night DECIMAL(10,2) NOT NULL,
    check_in_time VARCHAR(10),
    check_out_time VARCHAR(10),
    phone VARCHAR(50),
    email VARCHAR(200),
    website VARCHAR(300),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    rating_score DECIMAL(2,1) CHECK (rating_score >= 1.0 AND rating_score <= 5.0),
    total_reviews INTEGER DEFAULT 0,
    active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_hotels_city ON hotels(city);
CREATE INDEX IF NOT EXISTS idx_hotels_country ON hotels(country);
CREATE INDEX IF NOT EXISTS idx_hotels_star_rating ON hotels(star_rating);
CREATE INDEX IF NOT EXISTS idx_hotels_hotel_type ON hotels(hotel_type);
CREATE INDEX IF NOT EXISTS idx_hotels_chain ON hotels(chain);
CREATE INDEX IF NOT EXISTS idx_hotels_price ON hotels(base_price_per_night);
CREATE INDEX IF NOT EXISTS idx_hotels_rating ON hotels(rating_score);
CREATE INDEX IF NOT EXISTS idx_hotels_location ON hotels(latitude, longitude);

-- Insert comprehensive hotels data
INSERT INTO hotels (
    name, hotel_code, city, country, star_rating, hotel_type, chain,
    address, description, amenities, room_count, base_price_per_night,
    check_in_time, check_out_time, phone, email, website,
    latitude, longitude, rating_score, total_reviews
) VALUES 

-- LUXURY HOTELS - MIDDLE EAST
('Burj Al Arab Jumeirah', 'BAJ', 'Dubai', 'United Arab Emirates', 7, 'Luxury Resort', 'Jumeirah',
 'Jumeirah St, Dubai', 'World''s most luxurious hotel with iconic sail-shaped architecture',
 'Private beach, Spa, Multiple restaurants, Butler service, Helicopter pad', 202, 1500.00,
 '15:00', '12:00', '+971 4 301 7777', 'baj@jumeirah.com', 'https://www.jumeirah.com/burj-al-arab',
 25.14130000, 55.18530000, 4.8, 12500),

('The Ritz-Carlton Doha', 'RCD', 'Doha', 'Qatar', 5, 'Luxury Hotel', 'Ritz-Carlton',
 'West Bay, Doha', 'Elegant luxury hotel in the heart of Doha''s business district',
 'Spa, Pool, Business center, Multiple dining, Concierge', 374, 450.00,
 '15:00', '12:00', '+974 4484 8000', 'doha@ritzcarlton.com', 'https://www.ritzcarlton.com/doha',
 25.35480000, 51.53100000, 4.6, 8900),

-- LUXURY HOTELS - EUROPE
('The Savoy London', 'SAV', 'London', 'United Kingdom', 5, 'Luxury Hotel', 'Fairmont',
 'Strand, Covent Garden, London WC2R 0EZ', 'Iconic luxury hotel in the heart of London with rich history',
 'Thames views, Spa, Fine dining, Butler service, Theater district location', 267, 800.00,
 '15:00', '11:00', '+44 20 7836 4343', 'savoy@fairmont.com', 'https://www.thesavoylondon.com',
 51.51010000, -0.12040000, 4.7, 15600),

('Hotel de Crillon', 'CRI', 'Paris', 'France', 5, 'Luxury Hotel', 'Rosewood',
 '10 Place de la Concorde, 75008 Paris', 'Historic palace hotel overlooking Place de la Concorde',
 'Michelin-starred restaurant, Spa, Concierge, Historic architecture', 124, 1200.00,
 '15:00', '12:00', '+33 1 44 71 15 00', 'reservations.crillon@rosewoodhotels.com', 'https://www.rosewoodhotels.com/crillon',
 48.86560000, 2.32120000, 4.8, 9200),

('Hotel Vier Jahreszeiten Kempinski', 'VJK', 'Munich', 'Germany', 5, 'Luxury Hotel', 'Kempinski',
 'Maximilianstrasse 17, 80539 Munich', 'Grand luxury hotel on Munich''s prestigious shopping street',
 'Rooftop terrace, Spa, Fine dining, Shopping location, Business facilities', 305, 650.00,
 '15:00', '12:00', '+49 89 2125 0', 'reservation.muenchen@kempinski.com', 'https://www.kempinski.com/munich',
 48.13510000, 11.58200000, 4.6, 7800),

-- LUXURY HOTELS - ASIA PACIFIC
('Marina Bay Sands', 'MBS', 'Singapore', 'Singapore', 5, 'Luxury Resort', 'Independent',
 '10 Bayfront Ave, Singapore 018956', 'Iconic resort with infinity pool and integrated entertainment complex',
 'Infinity pool, Casino, Shopping mall, Multiple restaurants, Observation deck', 2561, 400.00,
 '15:00', '11:00', '+65 6688 8868', 'enquiry@marinabaysands.com', 'https://www.marinabaysands.com',
 1.28340000, 103.86070000, 4.5, 28000),

('Park Hyatt Tokyo', 'PHT', 'Tokyo', 'Japan', 5, 'Luxury Hotel', 'Hyatt',
 '3-7-1-2 Nishi Shinjuku, Shinjuku City, Tokyo 163-1055', 'Sophisticated luxury hotel in Tokyo''s skyscraper district',
 'City views, Spa, Fine dining, Business facilities, Art collection', 177, 800.00,
 '15:00', '12:00', '+81 3 5322 1234', 'tokyo.park@hyatt.com', 'https://www.hyatt.com/tokyo',
 35.68700000, 139.69280000, 4.7, 11200),

('The Peninsula Hong Kong', 'PHK', 'Hong Kong', 'Hong Kong', 5, 'Luxury Hotel', 'Peninsula Hotels',
 'Salisbury Rd, Tsim Sha Tsui, Kowloon, Hong Kong', 'Historic luxury hotel with legendary service and Rolls-Royce fleet',
 'Spa, Helicopter pad, Fine dining, Shopping access, Harbor views', 300, 600.00,
 '14:00', '12:00', '+852 2920 2888', 'phk@peninsula.com', 'https://www.peninsula.com/hongkong',
 22.29400000, 114.17220000, 4.8, 16800),

-- LUXURY HOTELS - AMERICAS
('The Plaza New York', 'PLZ', 'New York', 'United States', 5, 'Luxury Hotel', 'Independent',
 '768 5th Ave, New York, NY 10019', 'Iconic luxury hotel overlooking Central Park',
 'Central Park views, Spa, Fine dining, Shopping, Historic architecture', 282, 900.00,
 '15:00', '12:00', '+1 212 759 3000', 'info@theplazany.com', 'https://www.theplazany.com',
 40.76480000, -73.97540000, 4.4, 22000),

('Four Seasons Miami', 'FSM', 'Miami', 'United States', 5, 'Luxury Hotel', 'Four Seasons',
 '1435 Brickell Ave, Miami, FL 33131', 'Sophisticated urban luxury with bay and city views',
 'Spa, Pool, Fine dining, Business center, Bay views', 221, 650.00,
 '15:00', '12:00', '+1 305 358 3535', 'reservations.miami@fourseasons.com', 'https://www.fourseasons.com/miami',
 25.76170000, -80.19180000, 4.6, 8900),

('The Beverly Hills Hotel', 'BHH', 'Los Angeles', 'United States', 5, 'Luxury Hotel', 'Dorchester Collection',
 '9641 Sunset Blvd, Beverly Hills, CA 90210', 'Legendary pink palace of Hollywood glamour',
 'Pool, Spa, Fine dining, Garden setting, Celebrity history', 210, 800.00,
 '15:00', '12:00', '+1 310 276 2251', 'bhh@dorchestercollection.com', 'https://www.dorchestercollection.com/beverly-hills',
 34.09280000, -118.41470000, 4.5, 13500),

-- BUSINESS HOTELS
('Marriott Frankfurt', 'MRF', 'Frankfurt', 'Germany', 4, 'Business Hotel', 'Marriott',
 'Hamburger Allee 2, 60486 Frankfurt', 'Modern business hotel near Frankfurt Airport',
 'Business center, Fitness center, Restaurant, Meeting rooms, Airport shuttle', 588, 200.00,
 '15:00', '12:00', '+49 69 79560', 'mhrs.framc.reservations@marriott.com', 'https://www.marriott.com/frankfurt',
 50.07550000, 8.68420000, 4.2, 9800),

('Hilton London Heathrow', 'HLH', 'London', 'United Kingdom', 4, 'Airport Hotel', 'Hilton',
 'Terminal 4, Heathrow Airport, Hounslow TW6 3AF', 'Convenient airport hotel with direct terminal access',
 'Airport access, Business center, Restaurants, Fitness center, Meeting rooms', 398, 180.00,
 '15:00', '12:00', '+44 20 8759 7755', 'heathrow@hilton.com', 'https://www.hilton.com/heathrow',
 51.45880000, -0.45300000, 4.1, 12000),

-- BOUTIQUE HOTELS
('The Ned London', 'NED', 'London', 'United Kingdom', 5, 'Boutique Hotel', 'Soho House',
 '27 Poultry, London EC2R 8AJ', 'Historic bank building transformed into stylish hotel and club',
 'Multiple restaurants, Spa, Rooftop bar, Members club, Historic design', 252, 500.00,
 '15:00', '11:00', '+44 20 3828 2000', 'reservations@thened.com', 'https://www.thened.com',
 51.51310000, -0.08760000, 4.5, 8700),

-- RESORT HOTELS
('One&Only Royal Mirage', 'OOR', 'Dubai', 'United Arab Emirates', 5, 'Beach Resort', 'One&Only',
 'Al Sufouh Rd, Dubai', 'Exclusive beachfront resort with Arabian palace architecture',
 'Private beach, Spa, Multiple pools, Fine dining, Marina access', 250, 600.00,
 '15:00', '12:00', '+971 4 399 9999', 'reservations@oneandonlyresorts.com', 'https://www.oneandonlyresorts.com/dubai',
 25.10090000, 55.17190000, 4.7, 6800),

-- BUDGET FRIENDLY OPTIONS
('Premier Inn London City', 'PLC', 'London', 'United Kingdom', 3, 'Budget Hotel', 'Premier Inn',
 '1 Kingsway, London WC2B 6XF', 'Comfortable budget accommodation in central London',
 'Restaurant, WiFi, 24-hour reception, Business facilities', 460, 120.00,
 '14:00', '12:00', '+44 871 527 9678', 'londoncity@premierinn.com', 'https://www.premierinn.com/london-city',
 51.51550000, -0.12040000, 4.3, 18500),

('Holiday Inn Express Dubai', 'HID', 'Dubai', 'United Arab Emirates', 3, 'Business Hotel', 'Holiday Inn Express',
 'Internet City, Dubai', 'Modern business hotel with excellent connectivity',
 'Free breakfast, Business center, Fitness center, WiFi, Meeting rooms', 180, 150.00,
 '15:00', '12:00', '+971 4 4381 8888', 'reservations@hiexdubai.com', 'https://www.ihg.com/holidayinnexpress/dubai',
 25.09550000, 55.15610000, 4.2, 5600);
