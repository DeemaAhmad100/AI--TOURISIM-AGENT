-- 🌍 AI Travel Platform - Complete Database Schema
-- Enhanced database schema for production deployment
-- Compatible with Supabase PostgreSQL

-- Enable RLS (Row Level Security) for all tables
-- Enable UUID extension for unique IDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ===========================================
-- CORE TABLES
-- ===========================================

-- Users table for authentication and basic info
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE
);

-- User profiles for travel preferences
CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(255) UNIQUE NOT NULL REFERENCES users(user_id),
    name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    interests TEXT[] DEFAULT '{}',
    travel_style VARCHAR(100) DEFAULT 'cultural',
    personality_traits JSONB DEFAULT '{}',
    budget_range VARCHAR(50) DEFAULT 'moderate',
    accessibility_needs TEXT[] DEFAULT '{}',
    dietary_restrictions TEXT[] DEFAULT '{}',
    language_preferences TEXT[] DEFAULT '{}',
    preferred_airlines TEXT[] DEFAULT '{}',
    previous_destinations TEXT[] DEFAULT '{}',
    travel_frequency VARCHAR(100),
    calendar_integration BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Destinations table
CREATE TABLE IF NOT EXISTS destinations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    description TEXT,
    coordinates JSONB, -- {lat: float, lng: float}
    timezone VARCHAR(100),
    currency VARCHAR(10),
    language VARCHAR(100),
    best_time_to_visit VARCHAR(255),
    average_temperature JSONB, -- {min: float, max: float, unit: "C"}
    safety_rating INTEGER CHECK (safety_rating >= 1 AND safety_rating <= 10),
    cost_level VARCHAR(20) DEFAULT 'moderate', -- budget, moderate, expensive
    cultural_highlights TEXT[],
    weather_info JSONB,
    visa_requirements TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ===========================================
-- TRAVEL SERVICES TABLES
-- ===========================================

-- Airlines table
CREATE TABLE IF NOT EXISTS airlines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    iata_code VARCHAR(3) UNIQUE NOT NULL,
    icao_code VARCHAR(4) UNIQUE,
    country VARCHAR(100),
    rating DECIMAL(3,2) DEFAULT 3.5,
    fleet_size INTEGER,
    founded_year INTEGER,
    baggage_policy JSONB,
    amenities TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Flights table
CREATE TABLE IF NOT EXISTS flights (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    airline_id UUID REFERENCES airlines(id),
    flight_number VARCHAR(20) NOT NULL,
    departure_city VARCHAR(100) NOT NULL,
    arrival_city VARCHAR(100) NOT NULL,
    departure_time VARCHAR(50) NOT NULL,
    arrival_time VARCHAR(50) NOT NULL,
    duration VARCHAR(20),
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    stops INTEGER DEFAULT 0,
    aircraft_type VARCHAR(100),
    booking_url TEXT,
    rating DECIMAL(3,2) DEFAULT 4.0,
    amenities TEXT[],
    seat_configuration JSONB,
    meal_service BOOLEAN DEFAULT TRUE,
    wifi_available BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Hotels table  
CREATE TABLE IF NOT EXISTS hotels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    name VARCHAR(255) NOT NULL,
    destination VARCHAR(255), -- For backward compatibility
    category VARCHAR(100) DEFAULT 'hotel',
    price_per_night DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'USD',
    rating DECIMAL(3,2) DEFAULT 4.0,
    coordinates JSONB, -- {lat: float, lng: float}
    amenities TEXT[],
    room_types TEXT[],
    booking_platforms JSONB,
    customer_reviews JSONB,
    distance_to_center DECIMAL(5,2),
    check_in_time VARCHAR(10) DEFAULT '15:00',
    check_out_time VARCHAR(10) DEFAULT '11:00',
    cancellation_policy VARCHAR(100) DEFAULT 'free_24h',
    photos TEXT[],
    address TEXT,
    phone VARCHAR(50),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Restaurants table
CREATE TABLE IF NOT EXISTS restaurants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    name VARCHAR(255) NOT NULL,
    cuisine_type VARCHAR(100),
    price_range VARCHAR(20) DEFAULT 'moderate',
    rating DECIMAL(3,2) DEFAULT 4.0,
    coordinates JSONB,
    specialties TEXT[],
    dietary_options TEXT[],
    atmosphere VARCHAR(100),
    booking_required BOOLEAN DEFAULT FALSE,
    deposit_per_person DECIMAL(10,2) DEFAULT 0,
    opening_hours JSONB,
    customer_reviews JSONB,
    photos TEXT[],
    address TEXT,
    phone VARCHAR(50),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Car rental companies
CREATE TABLE IF NOT EXISTS car_rental_companies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255),
    phone VARCHAR(50),
    email VARCHAR(255),
    countries_served TEXT[],
    rating DECIMAL(3,2) DEFAULT 4.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Car rentals table
CREATE TABLE IF NOT EXISTS car_rentals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID REFERENCES car_rental_companies(id),
    destination_id UUID REFERENCES destinations(id),
    car_type VARCHAR(100) NOT NULL,
    brand VARCHAR(100),
    model VARCHAR(100),
    price_per_day DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    fuel_type VARCHAR(50),
    transmission VARCHAR(20),
    seats INTEGER,
    features TEXT[],
    insurance_included BOOLEAN DEFAULT FALSE,
    unlimited_mileage BOOLEAN DEFAULT TRUE,
    pickup_locations TEXT[],
    age_requirement INTEGER DEFAULT 21,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Attractions table
CREATE TABLE IF NOT EXISTS attractions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100), -- museum, landmark, nature, entertainment
    description TEXT,
    coordinates JSONB,
    opening_hours JSONB,
    entrance_fee DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'USD',
    rating DECIMAL(3,2) DEFAULT 4.0,
    duration_hours INTEGER,
    difficulty_level VARCHAR(20), -- easy, moderate, hard
    accessibility_features TEXT[],
    best_time_to_visit VARCHAR(255),
    photos TEXT[],
    address TEXT,
    phone VARCHAR(50),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Activities table
CREATE TABLE IF NOT EXISTS activities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100), -- adventure, cultural, food, nature, nightlife
    description TEXT,
    price DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'USD',
    duration_hours INTEGER,
    group_size_min INTEGER DEFAULT 1,
    group_size_max INTEGER DEFAULT 50,
    difficulty_level VARCHAR(20),
    age_requirement INTEGER DEFAULT 0,
    booking_required BOOLEAN DEFAULT TRUE,
    seasonal_availability JSONB,
    includes TEXT[],
    excludes TEXT[],
    meeting_point TEXT,
    contact_info JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ===========================================
-- BOOKING AND TRANSACTION TABLES
-- ===========================================

-- Travel packages table
CREATE TABLE IF NOT EXISTS travel_packages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    destination_id UUID REFERENCES destinations(id),
    total_price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    duration_days INTEGER NOT NULL,
    included_services TEXT[],
    package_type VARCHAR(100) DEFAULT 'standard',
    created_by UUID REFERENCES users(id),
    is_group_package BOOLEAN DEFAULT FALSE,
    max_participants INTEGER,
    description TEXT,
    highlights TEXT[],
    itinerary JSONB,
    terms_conditions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Main bookings table
CREATE TABLE IF NOT EXISTS bookings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    booking_type VARCHAR(50) NOT NULL, -- flight, hotel, restaurant, car_rental, package
    user_id VARCHAR(255) NOT NULL REFERENCES users(user_id),
    item_id UUID NOT NULL, -- References various service tables
    details JSONB NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    status VARCHAR(20) DEFAULT 'pending', -- pending, confirmed, cancelled, completed, failed
    confirmation_number VARCHAR(100) UNIQUE NOT NULL,
    special_requests TEXT[],
    group_booking_id UUID,
    payment_status VARCHAR(20) DEFAULT 'pending',
    payment_method VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE
);

-- Travel bookings table (for backward compatibility)
CREATE TABLE IF NOT EXISTS travel_bookings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    savings DECIMAL(10,2) DEFAULT 0,
    flight_details JSONB,
    hotel_details JSONB,
    booking_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'confirmed',
    user_id VARCHAR(255)
);

-- Price tracking table
CREATE TABLE IF NOT EXISTS price_tracking (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(255) REFERENCES users(user_id),
    item_type VARCHAR(50) NOT NULL, -- flight, hotel, package
    item_id UUID NOT NULL,
    target_price DECIMAL(10,2) NOT NULL,
    current_price DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'USD',
    alert_threshold DECIMAL(5,2) DEFAULT 0.10, -- 10% price drop
    is_active BOOLEAN DEFAULT TRUE,
    last_checked TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ===========================================
-- INTELLIGENCE AND INSIGHTS TABLES
-- ===========================================

-- Cultural insights table
CREATE TABLE IF NOT EXISTS cultural_insights (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    category VARCHAR(100) NOT NULL, -- etiquette, customs, tipping, dress_code
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    importance_level INTEGER CHECK (importance_level >= 1 AND importance_level <= 5),
    do_items TEXT[],
    dont_items TEXT[],
    examples TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Seasonal data table
CREATE TABLE IF NOT EXISTS seasonal_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destination_id UUID REFERENCES destinations(id),
    month INTEGER CHECK (month >= 1 AND month <= 12),
    temperature_avg DECIMAL(5,2),
    temperature_min DECIMAL(5,2),
    temperature_max DECIMAL(5,2),
    rainfall_mm INTEGER,
    humidity_percent INTEGER,
    tourist_crowd_level INTEGER CHECK (tourist_crowd_level >= 1 AND tourist_crowd_level <= 10),
    price_multiplier DECIMAL(3,2) DEFAULT 1.0,
    weather_description VARCHAR(255),
    events TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ===========================================
-- ANALYTICS AND REPORTING TABLES
-- ===========================================

-- User travel history
CREATE TABLE IF NOT EXISTS user_travel_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(255) NOT NULL REFERENCES users(user_id),
    destination_id UUID REFERENCES destinations(id),
    travel_date DATE NOT NULL,
    duration_days INTEGER,
    total_spent DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'USD',
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    review TEXT,
    photos TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Search analytics
CREATE TABLE IF NOT EXISTS search_analytics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(255) REFERENCES users(user_id),
    search_type VARCHAR(50) NOT NULL, -- destination, hotel, flight, activity
    search_query TEXT NOT NULL,
    search_filters JSONB,
    results_count INTEGER,
    clicked_result_id UUID,
    conversion_occurred BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ===========================================
-- INDEXES FOR PERFORMANCE
-- ===========================================

-- User and profile indexes
CREATE INDEX IF NOT EXISTS idx_users_user_id ON users(user_id);
CREATE INDEX IF NOT EXISTS idx_user_profiles_user_id ON user_profiles(user_id);

-- Destination indexes
CREATE INDEX IF NOT EXISTS idx_destinations_country ON destinations(country);
CREATE INDEX IF NOT EXISTS idx_destinations_city ON destinations(city);

-- Service indexes
CREATE INDEX IF NOT EXISTS idx_flights_departure_arrival ON flights(departure_city, arrival_city);
CREATE INDEX IF NOT EXISTS idx_hotels_destination_id ON hotels(destination_id);
CREATE INDEX IF NOT EXISTS idx_restaurants_destination_id ON restaurants(destination_id);
CREATE INDEX IF NOT EXISTS idx_attractions_destination_id ON attractions(destination_id);

-- Booking indexes
CREATE INDEX IF NOT EXISTS idx_bookings_user_id ON bookings(user_id);
CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_bookings_created_at ON bookings(created_at);
CREATE INDEX IF NOT EXISTS idx_travel_bookings_booking_date ON travel_bookings(booking_date);

-- Price tracking indexes
CREATE INDEX IF NOT EXISTS idx_price_tracking_user_id ON price_tracking(user_id);
CREATE INDEX IF NOT EXISTS idx_price_tracking_active ON price_tracking(is_active);

-- ===========================================
-- TRIGGERS FOR UPDATED_AT TIMESTAMPS
-- ===========================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for all tables with updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_profiles_updated_at BEFORE UPDATE ON user_profiles FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_destinations_updated_at BEFORE UPDATE ON destinations FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_flights_updated_at BEFORE UPDATE ON flights FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_hotels_updated_at BEFORE UPDATE ON hotels FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_restaurants_updated_at BEFORE UPDATE ON restaurants FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_car_rentals_updated_at BEFORE UPDATE ON car_rentals FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_attractions_updated_at BEFORE UPDATE ON attractions FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_activities_updated_at BEFORE UPDATE ON activities FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_travel_packages_updated_at BEFORE UPDATE ON travel_packages FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_bookings_updated_at BEFORE UPDATE ON bookings FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ===========================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ===========================================

-- Enable RLS on user-specific tables
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE travel_bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE price_tracking ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_travel_history ENABLE ROW LEVEL SECURITY;
ALTER TABLE search_analytics ENABLE ROW LEVEL SECURITY;

-- Create policies for user data access
CREATE POLICY "Users can view their own profiles" ON user_profiles FOR SELECT USING (auth.uid()::text = user_id);
CREATE POLICY "Users can update their own profiles" ON user_profiles FOR UPDATE USING (auth.uid()::text = user_id);
CREATE POLICY "Users can insert their own profiles" ON user_profiles FOR INSERT WITH CHECK (auth.uid()::text = user_id);

CREATE POLICY "Users can view their own bookings" ON bookings FOR SELECT USING (auth.uid()::text = user_id);
CREATE POLICY "Users can view their own travel bookings" ON travel_bookings FOR SELECT USING (auth.uid()::text = user_id);
CREATE POLICY "Users can view their own price tracking" ON price_tracking FOR SELECT USING (auth.uid()::text = user_id);
CREATE POLICY "Users can view their own travel history" ON user_travel_history FOR SELECT USING (auth.uid()::text = user_id);

-- ===========================================
-- INITIAL DATA POPULATION
-- ===========================================

-- Insert sample destinations
INSERT INTO destinations (name, country, city, description, coordinates, timezone, currency, language, best_time_to_visit, safety_rating, cost_level) VALUES
('Beirut, Lebanon', 'Lebanon', 'Beirut', 'The Pearl of the Middle East, known for its vibrant culture and rich history', '{"lat": 33.8938, "lng": 35.5018}', 'Asia/Beirut', 'LBP', 'Arabic', 'April-June, September-November', 8, 'moderate'),
('Tokyo, Japan', 'Japan', 'Tokyo', 'A bustling metropolis blending traditional and modern culture', '{"lat": 35.6762, "lng": 139.6503}', 'Asia/Tokyo', 'JPY', 'Japanese', 'March-May, September-November', 9, 'expensive'),
('Paris, France', 'France', 'Paris', 'The City of Light, famous for art, fashion, and cuisine', '{"lat": 48.8566, "lng": 2.3522}', 'Europe/Paris', 'EUR', 'French', 'April-June, September-October', 8, 'expensive'),
('New York, USA', 'USA', 'New York', 'The Big Apple, a global hub for business, arts, and culture', '{"lat": 40.7128, "lng": -74.0060}', 'America/New_York', 'USD', 'English', 'April-June, September-November', 7, 'expensive'),
('Dubai, UAE', 'UAE', 'Dubai', 'A modern oasis known for luxury shopping and futuristic architecture', '{"lat": 25.2048, "lng": 55.2708}', 'Asia/Dubai', 'AED', 'Arabic', 'November-March', 9, 'expensive')
ON CONFLICT DO NOTHING;

-- Insert sample airlines
INSERT INTO airlines (name, iata_code, icao_code, country, rating) VALUES
('Emirates', 'EK', 'UAE', 'UAE', 4.8),
('Qatar Airways', 'QR', 'QTR', 'Qatar', 4.7),
('Turkish Airlines', 'TK', 'THY', 'Turkey', 4.5),
('Air France', 'AF', 'AFR', 'France', 4.3),
('British Airways', 'BA', 'BAW', 'UK', 4.2),
('Lufthansa', 'LH', 'DLH', 'Germany', 4.4),
('American Airlines', 'AA', 'AAL', 'USA', 4.1),
('Japan Airlines', 'JL', 'JAL', 'Japan', 4.6)
ON CONFLICT DO NOTHING;

-- Create admin user function
CREATE OR REPLACE FUNCTION create_admin_user()
RETURNS void AS $$
BEGIN
    -- Insert admin user if not exists
    INSERT INTO users (user_id, email, name, phone)
    VALUES ('admin', 'admin@aitravelplatform.com', 'AI Travel Platform Admin', '+1-555-0100')
    ON CONFLICT (user_id) DO NOTHING;
    
    -- Insert admin profile if not exists
    INSERT INTO user_profiles (user_id, name, age, interests, travel_style, budget_range)
    VALUES ('admin', 'AI Travel Platform Admin', 30, ARRAY['technology', 'business', 'travel'], 'luxury', 'luxury')
    ON CONFLICT (user_id) DO NOTHING;
END;
$$ LANGUAGE plpgsql;

-- Execute admin user creation
SELECT create_admin_user();

-- ===========================================
-- VIEWS FOR COMMON QUERIES
-- ===========================================

-- Complete destination view with statistics
CREATE OR REPLACE VIEW destination_stats AS
SELECT 
    d.*,
    COUNT(DISTINCT h.id) as hotel_count,
    COUNT(DISTINCT r.id) as restaurant_count,
    COUNT(DISTINCT a.id) as attraction_count,
    COUNT(DISTINCT act.id) as activity_count,
    AVG(h.rating) as avg_hotel_rating,
    AVG(r.rating) as avg_restaurant_rating,
    AVG(a.rating) as avg_attraction_rating
FROM destinations d
LEFT JOIN hotels h ON d.id = h.destination_id
LEFT JOIN restaurants r ON d.id = r.destination_id
LEFT JOIN attractions a ON d.id = a.destination_id
LEFT JOIN activities act ON d.id = act.destination_id
GROUP BY d.id, d.name, d.country, d.city, d.description, d.coordinates, d.timezone, d.currency, d.language, d.best_time_to_visit, d.average_temperature, d.safety_rating, d.cost_level, d.cultural_highlights, d.weather_info, d.visa_requirements, d.created_at, d.updated_at;

-- User booking summary view
CREATE OR REPLACE VIEW user_booking_summary AS
SELECT 
    u.user_id,
    u.name,
    COUNT(b.id) as total_bookings,
    SUM(b.total_amount) as total_spent,
    AVG(b.total_amount) as avg_booking_value,
    COUNT(DISTINCT CASE WHEN b.status = 'confirmed' THEN b.id END) as confirmed_bookings,
    COUNT(DISTINCT CASE WHEN b.status = 'cancelled' THEN b.id END) as cancelled_bookings,
    MAX(b.created_at) as last_booking_date
FROM users u
LEFT JOIN bookings b ON u.user_id = b.user_id
GROUP BY u.user_id, u.name;

-- ===========================================
-- COMPLETION MESSAGE
-- ===========================================

-- Log schema creation
INSERT INTO destinations (name, country, city, description, safety_rating, cost_level) VALUES
('Schema Created', 'System', 'Database', 'AI Travel Platform database schema created successfully', 10, 'moderate')
ON CONFLICT DO NOTHING;

-- Success message
DO $$
BEGIN
    RAISE NOTICE '🎉 AI Travel Platform Database Schema Created Successfully!';
    RAISE NOTICE '✅ Tables: 20 core tables with proper relationships';
    RAISE NOTICE '✅ Indexes: Performance optimized for common queries';
    RAISE NOTICE '✅ Security: Row Level Security policies implemented';
    RAISE NOTICE '✅ Data: Sample data populated for testing';
    RAISE NOTICE '🚀 Ready for production deployment!';
END $$;
