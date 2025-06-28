"""
Enhanced Database Schema for AI Travel Platform
Advanced database structure with all required tables and relationships
"""

# SQL Schema for Supabase/PostgreSQL

DATABASE_SCHEMA = """

-- Users table with enhanced profile information
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    phone VARCHAR,
    date_of_birth DATE,
    nationality VARCHAR,
    passport_number VARCHAR,
    profile_picture_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE,
    email_verified BOOLEAN DEFAULT FALSE,
    phone_verified BOOLEAN DEFAULT FALSE,
    status VARCHAR DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'deleted'))
);

-- User profiles with detailed preferences
CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    age INTEGER,
    interests TEXT[], -- ['culture', 'food', 'nature', 'adventure']
    travel_style VARCHAR CHECK (travel_style IN ('budget', 'moderate', 'luxury', 'adventure', 'cultural', 'family')),
    accessibility_needs TEXT[], -- ['wheelchair_accessible', 'hearing_impaired']
    budget_range VARCHAR CHECK (budget_range IN ('budget', 'moderate', 'luxury')),
    preferred_airlines TEXT[],
    dietary_restrictions TEXT[], -- ['vegetarian', 'vegan', 'halal', 'kosher']
    language_preferences TEXT[],
    preferred_currency VARCHAR DEFAULT 'USD',
    notification_preferences JSONB DEFAULT '{}',
    privacy_settings JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Destinations with comprehensive information
CREATE TABLE IF NOT EXISTS destinations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    continent VARCHAR NOT NULL,
    city VARCHAR,
    description TEXT,
    coordinates POINT, -- Latitude, Longitude
    timezone VARCHAR,
    currency VARCHAR,
    language VARCHAR,
    best_season VARCHAR,
    climate_type VARCHAR,
    visa_requirements TEXT,
    safety_rating DECIMAL(2,1) CHECK (safety_rating >= 0 AND safety_rating <= 5),
    cost_level VARCHAR CHECK (cost_level IN ('low', 'medium', 'high')),
    popularity_score INTEGER DEFAULT 0,
    image_urls TEXT[],
    tags TEXT[], -- ['beach', 'mountains', 'cultural', 'adventure']
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Airlines information
CREATE TABLE IF NOT EXISTS airlines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    iata_code VARCHAR(2) UNIQUE,
    icao_code VARCHAR(3) UNIQUE,
    country VARCHAR,
    hub_airports TEXT[],
    fleet_size INTEGER,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    safety_rating DECIMAL(2,1) CHECK (safety_rating >= 0 AND safety_rating <= 5),
    service_class TEXT[], -- ['economy', 'business', 'first']
    amenities TEXT[],
    baggage_policy JSONB,
    contact_info JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Flights with dynamic pricing
CREATE TABLE IF NOT EXISTS flights (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    airline_id UUID REFERENCES airlines(id),
    flight_number VARCHAR NOT NULL,
    departure_airport VARCHAR NOT NULL,
    arrival_airport VARCHAR NOT NULL,
    departure_time TIMESTAMP WITH TIME ZONE NOT NULL,
    arrival_time TIMESTAMP WITH TIME ZONE NOT NULL,
    duration INTERVAL,
    aircraft_type VARCHAR,
    stops INTEGER DEFAULT 0,
    base_price DECIMAL(10,2) NOT NULL,
    current_price DECIMAL(10,2) NOT NULL,
    available_seats INTEGER,
    total_seats INTEGER,
    service_class VARCHAR CHECK (service_class IN ('economy', 'business', 'first')),
    amenities TEXT[],
    booking_url TEXT,
    status VARCHAR DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'delayed', 'cancelled', 'departed', 'arrived')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Hotels with detailed information
CREATE TABLE IF NOT EXISTS hotels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    destination_id UUID REFERENCES destinations(id),
    address TEXT,
    coordinates POINT,
    star_rating INTEGER CHECK (star_rating >= 1 AND star_rating <= 5),
    customer_rating DECIMAL(2,1) CHECK (customer_rating >= 0 AND customer_rating <= 5),
    price_per_night DECIMAL(10,2),
    currency VARCHAR DEFAULT 'USD',
    amenities TEXT[],
    room_types JSONB, -- Different room configurations and prices
    photos TEXT[],
    description TEXT,
    policies JSONB, -- Cancellation, check-in/out policies
    contact_info JSONB,
    booking_url TEXT,
    distance_to_center DECIMAL(5,2), -- in kilometers
    wifi_available BOOLEAN DEFAULT TRUE,
    parking_available BOOLEAN DEFAULT FALSE,
    pet_friendly BOOLEAN DEFAULT FALSE,
    accessibility_features TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Restaurants with reviews and ratings
CREATE TABLE IF NOT EXISTS restaurants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    destination_id UUID REFERENCES destinations(id),
    cuisine_type VARCHAR NOT NULL,
    address TEXT,
    coordinates POINT,
    phone VARCHAR,
    email VARCHAR,
    website TEXT,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    price_range VARCHAR CHECK (price_range IN ('$', '$$', '$$$', '$$$$')),
    specialties TEXT[],
    dietary_options TEXT[], -- ['vegetarian', 'vegan', 'gluten-free']
    opening_hours JSONB,
    reservation_required BOOLEAN DEFAULT FALSE,
    booking_url TEXT,
    photos TEXT[],
    description TEXT,
    atmosphere_tags TEXT[], -- ['romantic', 'family-friendly', 'casual', 'upscale']
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Car rental companies
CREATE TABLE IF NOT EXISTS car_rental_companies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    locations TEXT[], -- Available pickup locations
    contact_info JSONB,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    fleet_types TEXT[], -- ['economy', 'compact', 'luxury', 'suv']
    policies JSONB, -- Insurance, age requirements, etc.
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Car rental options
CREATE TABLE IF NOT EXISTS car_rentals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID REFERENCES car_rental_companies(id),
    destination_id UUID REFERENCES destinations(id),
    car_model VARCHAR NOT NULL,
    car_type VARCHAR CHECK (car_type IN ('economy', 'compact', 'mid-size', 'luxury', 'suv', 'convertible')),
    price_per_day DECIMAL(10,2) NOT NULL,
    currency VARCHAR DEFAULT 'USD',
    features TEXT[],
    pickup_locations TEXT[],
    fuel_type VARCHAR CHECK (fuel_type IN ('gasoline', 'diesel', 'hybrid', 'electric')),
    transmission VARCHAR CHECK (transmission IN ('manual', 'automatic')),
    seats INTEGER,
    insurance_included BOOLEAN DEFAULT FALSE,
    mileage_limit INTEGER, -- per day
    booking_url TEXT,
    availability_status VARCHAR DEFAULT 'available',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Activities and attractions
CREATE TABLE IF NOT EXISTS activities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    destination_id UUID REFERENCES destinations(id),
    name VARCHAR NOT NULL,
    type VARCHAR NOT NULL, -- 'museum', 'tour', 'adventure', 'cultural'
    description TEXT,
    address TEXT,
    coordinates POINT,
    duration VARCHAR, -- 'half-day', 'full-day', '2 hours'
    price DECIMAL(10,2),
    currency VARCHAR DEFAULT 'USD',
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    difficulty_level VARCHAR CHECK (difficulty_level IN ('easy', 'moderate', 'difficult')),
    age_restrictions JSONB,
    accessibility_info TEXT[],
    operating_hours JSONB,
    booking_required BOOLEAN DEFAULT FALSE,
    booking_url TEXT,
    photos TEXT[],
    tags TEXT[], -- ['outdoor', 'cultural', 'family-friendly', 'romantic']
    seasonal_availability JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Travel packages
CREATE TABLE IF NOT EXISTS travel_packages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR NOT NULL,
    destination_id UUID REFERENCES destinations(id),
    duration_days INTEGER NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    current_price DECIMAL(10,2) NOT NULL,
    currency VARCHAR DEFAULT 'USD',
    savings_amount DECIMAL(10,2) DEFAULT 0,
    package_type VARCHAR CHECK (package_type IN ('standard', 'premium', 'luxury', 'budget')),
    included_services TEXT[], -- ['flight', 'hotel', 'car', 'activities']
    description TEXT,
    highlights TEXT[],
    terms_conditions TEXT,
    cancellation_policy TEXT,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    popularity_score INTEGER DEFAULT 0,
    max_group_size INTEGER,
    min_advance_booking INTEGER, -- days
    photos TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User bookings
CREATE TABLE IF NOT EXISTS bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    package_id UUID REFERENCES travel_packages(id),
    booking_reference VARCHAR UNIQUE NOT NULL,
    status VARCHAR DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed', 'refunded')),
    total_amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR DEFAULT 'USD',
    payment_status VARCHAR DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'failed', 'refunded')),
    payment_method VARCHAR,
    payment_reference VARCHAR,
    traveler_count INTEGER DEFAULT 1,
    traveler_details JSONB, -- Information about all travelers
    special_requests TEXT,
    travel_dates DATERANGE,
    booking_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    confirmation_date TIMESTAMP WITH TIME ZONE,
    cancellation_date TIMESTAMP WITH TIME ZONE,
    refund_amount DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Booking components (flights, hotels, etc. for each booking)
CREATE TABLE IF NOT EXISTS booking_components (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id) ON DELETE CASCADE,
    component_type VARCHAR NOT NULL CHECK (component_type IN ('flight', 'hotel', 'car_rental', 'activity')),
    component_id UUID NOT NULL, -- References flights, hotels, car_rentals, or activities
    start_date DATE,
    end_date DATE,
    quantity INTEGER DEFAULT 1,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    status VARCHAR DEFAULT 'booked',
    confirmation_number VARCHAR,
    vendor_booking_reference VARCHAR,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Price tracking
CREATE TABLE IF NOT EXISTS price_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    item_type VARCHAR NOT NULL CHECK (item_type IN ('flight', 'hotel', 'package', 'car_rental')),
    item_id UUID NOT NULL,
    target_price DECIMAL(10,2),
    current_price DECIMAL(10,2),
    price_threshold DECIMAL(5,2) DEFAULT 10.0, -- Percentage change to trigger alert
    notification_enabled BOOLEAN DEFAULT TRUE,
    email_notifications BOOLEAN DEFAULT TRUE,
    sms_notifications BOOLEAN DEFAULT FALSE,
    start_date DATE,
    end_date DATE,
    status VARCHAR DEFAULT 'active' CHECK (status IN ('active', 'paused', 'completed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Price history for trend analysis
CREATE TABLE IF NOT EXISTS price_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    item_type VARCHAR NOT NULL,
    item_id UUID NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR DEFAULT 'USD',
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    source VARCHAR, -- Where the price was scraped from
    availability_count INTEGER -- Available seats/rooms
);

-- Group bookings
CREATE TABLE IF NOT EXISTS group_bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    group_leader_id UUID REFERENCES users(id),
    group_name VARCHAR NOT NULL,
    destination_id UUID REFERENCES destinations(id),
    travel_dates DATERANGE,
    max_participants INTEGER,
    current_participants INTEGER DEFAULT 1,
    min_participants INTEGER DEFAULT 2,
    group_discount_percentage DECIMAL(5,2) DEFAULT 0,
    base_price_per_person DECIMAL(10,2),
    discounted_price_per_person DECIMAL(10,2),
    registration_deadline DATE,
    payment_deadline DATE,
    status VARCHAR DEFAULT 'open' CHECK (status IN ('open', 'confirmed', 'cancelled', 'completed')),
    description TEXT,
    terms_conditions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Group booking participants
CREATE TABLE IF NOT EXISTS group_booking_participants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    group_booking_id UUID REFERENCES group_bookings(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id),
    participant_name VARCHAR NOT NULL,
    participant_email VARCHAR NOT NULL,
    participant_phone VARCHAR,
    payment_status VARCHAR DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'failed')),
    special_requirements TEXT,
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    confirmed_at TIMESTAMP WITH TIME ZONE
);

-- Reviews and ratings
CREATE TABLE IF NOT EXISTS reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    booking_id UUID REFERENCES bookings(id),
    item_type VARCHAR NOT NULL CHECK (item_type IN ('destination', 'hotel', 'restaurant', 'activity', 'package')),
    item_id UUID NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    title VARCHAR,
    review_text TEXT,
    pros TEXT[],
    cons TEXT[],
    photos TEXT[],
    travel_date DATE,
    helpful_votes INTEGER DEFAULT 0,
    verified_booking BOOLEAN DEFAULT FALSE,
    response_from_vendor TEXT,
    response_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR DEFAULT 'published' CHECK (status IN ('draft', 'published', 'hidden', 'flagged')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User calendar integration
CREATE TABLE IF NOT EXISTS user_calendars (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    calendar_type VARCHAR NOT NULL CHECK (calendar_type IN ('google', 'outlook', 'apple', 'other')),
    calendar_id VARCHAR NOT NULL,
    access_token_encrypted TEXT,
    refresh_token_encrypted TEXT,
    sync_enabled BOOLEAN DEFAULT TRUE,
    last_sync TIMESTAMP WITH TIME ZONE,
    sync_frequency INTEGER DEFAULT 60, -- minutes
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User notifications
CREATE TABLE IF NOT EXISTS notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    type VARCHAR NOT NULL CHECK (type IN ('price_alert', 'booking_confirmation', 'travel_reminder', 'group_update', 'review_request')),
    title VARCHAR NOT NULL,
    message TEXT NOT NULL,
    data JSONB, -- Additional data related to notification
    channels TEXT[] DEFAULT ARRAY['email'], -- ['email', 'sms', 'push', 'in_app']
    read BOOLEAN DEFAULT FALSE,
    sent BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP WITH TIME ZONE,
    scheduled_for TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Travel guides and documents
CREATE TABLE IF NOT EXISTS travel_guides (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    destination_id UUID REFERENCES destinations(id),
    booking_id UUID REFERENCES bookings(id),
    user_id UUID REFERENCES users(id),
    title VARCHAR NOT NULL,
    content TEXT,
    pdf_url TEXT,
    guide_type VARCHAR CHECK (guide_type IN ('general', 'personalized', 'group')),
    language VARCHAR DEFAULT 'en',
    version INTEGER DEFAULT 1,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    download_count INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Hidden gems and local experiences
CREATE TABLE IF NOT EXISTS hidden_gems (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    destination_id UUID REFERENCES destinations(id),
    submitted_by_user_id UUID REFERENCES users(id),
    name VARCHAR NOT NULL,
    description TEXT,
    category VARCHAR, -- 'restaurant', 'viewpoint', 'activity', 'shopping'
    coordinates POINT,
    address TEXT,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 5),
    difficulty_level VARCHAR CHECK (difficulty_level IN ('easy', 'moderate', 'difficult')),
    cost_level VARCHAR CHECK (cost_level IN ('free', 'low', 'medium', 'high')),
    best_time_to_visit VARCHAR,
    insider_tips TEXT[],
    photos TEXT[],
    tags TEXT[],
    verified BOOLEAN DEFAULT FALSE,
    verified_by_admin_id UUID,
    verification_date TIMESTAMP WITH TIME ZONE,
    upvotes INTEGER DEFAULT 0,
    downvotes INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Travel news and updates
CREATE TABLE IF NOT EXISTS travel_news (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    summary TEXT,
    author VARCHAR,
    source_url TEXT,
    image_url TEXT,
    category VARCHAR CHECK (category IN ('safety', 'weather', 'events', 'deals', 'transport', 'health')),
    destinations UUID[], -- Array of destination IDs this news affects
    severity VARCHAR CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    valid_until DATE,
    published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP WITH TIME ZONE,
    tags TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_bookings_user_id ON bookings(user_id);
CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_flights_departure_arrival ON flights(departure_airport, arrival_airport);
CREATE INDEX IF NOT EXISTS idx_flights_departure_time ON flights(departure_time);
CREATE INDEX IF NOT EXISTS idx_hotels_destination_id ON hotels(destination_id);
CREATE INDEX IF NOT EXISTS idx_restaurants_destination_id ON restaurants(destination_id);
CREATE INDEX IF NOT EXISTS idx_activities_destination_id ON activities(destination_id);
CREATE INDEX IF NOT EXISTS idx_price_history_item ON price_history(item_type, item_id);
CREATE INDEX IF NOT EXISTS idx_reviews_item ON reviews(item_type, item_id);
CREATE INDEX IF NOT EXISTS idx_notifications_user_id ON notifications(user_id);
CREATE INDEX IF NOT EXISTS idx_travel_news_destinations ON travel_news USING GIN(destinations);

-- Functions for common operations
CREATE OR REPLACE FUNCTION calculate_package_discount(group_size INTEGER)
RETURNS DECIMAL(5,2) AS $$
BEGIN
    CASE 
        WHEN group_size >= 10 THEN RETURN 15.0;
        WHEN group_size >= 5 THEN RETURN 10.0;
        WHEN group_size >= 3 THEN RETURN 5.0;
        ELSE RETURN 0.0;
    END CASE;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updating timestamps
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_user_profiles_updated_at BEFORE UPDATE ON user_profiles
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_destinations_updated_at BEFORE UPDATE ON destinations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_hotels_updated_at BEFORE UPDATE ON hotels
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_bookings_updated_at BEFORE UPDATE ON bookings
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

"""

# Sample data insertion script
SAMPLE_DATA = """

-- Insert sample destinations
INSERT INTO destinations (name, country, continent, city, description, timezone, currency, language, best_season, climate_type, safety_rating, cost_level, tags) VALUES
('Beirut', 'Lebanon', 'Asia', 'Beirut', 'The Paris of the Middle East, known for its vibrant nightlife, rich history, and excellent cuisine', 'Asia/Beirut', 'LBP', 'Arabic', 'Spring/Fall', 'Mediterranean', 4.2, 'medium', ARRAY['cultural', 'nightlife', 'food', 'history']),
('Dubai', 'UAE', 'Asia', 'Dubai', 'A modern metropolis with luxury shopping, ultramodern architecture, and vibrant nightlife', 'Asia/Dubai', 'AED', 'Arabic', 'Winter', 'Desert', 4.8, 'high', ARRAY['luxury', 'shopping', 'modern', 'desert']),
('Paris', 'France', 'Europe', 'Paris', 'The City of Light, famous for art, fashion, gastronomy, and culture', 'Europe/Paris', 'EUR', 'French', 'Spring/Summer', 'Temperate', 4.5, 'high', ARRAY['cultural', 'art', 'fashion', 'romantic']),
('Tokyo', 'Japan', 'Asia', 'Tokyo', 'A bustling metropolis blending traditional culture with cutting-edge technology', 'Asia/Tokyo', 'JPY', 'Japanese', 'Spring/Fall', 'Humid Subtropical', 4.7, 'high', ARRAY['technology', 'culture', 'food', 'modern']);

-- Insert sample airlines
INSERT INTO airlines (name, iata_code, icao_code, country, rating, safety_rating, service_class, amenities) VALUES
('Emirates', 'EK', 'UAE', 'United Arab Emirates', 4.7, 4.9, ARRAY['economy', 'business', 'first'], ARRAY['Wi-Fi', 'Entertainment', 'Gourmet Meals', 'Lounge Access']),
('Qatar Airways', 'QR', 'QTR', 'Qatar', 4.8, 4.9, ARRAY['economy', 'business', 'first'], ARRAY['Wi-Fi', 'Premium Entertainment', 'Award-winning Cuisine', 'Luxury Lounges']),
('Turkish Airlines', 'TK', 'THY', 'Turkey', 4.5, 4.6, ARRAY['economy', 'business', 'first'], ARRAY['Wi-Fi', 'Entertainment', 'Turkish Cuisine', 'Miles&Smiles']);

-- Insert sample hotels
INSERT INTO hotels (name, destination_id, address, star_rating, customer_rating, price_per_night, amenities, description, wifi_available, parking_available) VALUES
((SELECT id FROM destinations WHERE name = 'Beirut'), 'Four Seasons Hotel Beirut', 'Beirut Central District', 5, 4.8, 280.00, ARRAY['Pool', 'Spa', 'Gym', 'Sea View', 'Concierge'], 'Luxury hotel with stunning Mediterranean views', true, true),
((SELECT id FROM destinations WHERE name = 'Beirut'), 'InterContinental Phoenicia Beirut', 'Ain Mreisseh', 5, 4.6, 220.00, ARRAY['Pool', 'Business Center', 'Restaurant', 'Sea View'], 'Historic hotel with excellent location', true, true);

-- Insert sample restaurants
INSERT INTO restaurants (name, destination_id, cuisine_type, rating, price_range, specialties, dietary_options, reservation_required) VALUES
((SELECT id FROM destinations WHERE name = 'Beirut'), 'Tawlet', 'Lebanese Traditional', 4.7, '$$', ARRAY['Meze', 'Kibbeh', 'Traditional Stews'], ARRAY['vegetarian', 'vegan'], false),
((SELECT id FROM destinations WHERE name = 'Beirut'), 'Em Sherif', 'Lebanese Fine Dining', 4.9, '$$$$', ARRAY['Gourmet Meze', 'Lamb Ouzi', 'Traditional Sweets'], ARRAY['vegetarian'], true);

-- Insert sample activities
INSERT INTO activities (name, destination_id, type, description, duration, price, rating, difficulty_level, tags) VALUES
('National Museum of Beirut', (SELECT id FROM destinations WHERE name = 'Beirut'), 'museum', 'Explore Lebanon rich archaeological heritage', 'half-day', 15.00, 4.5, 'easy', ARRAY['cultural', 'history', 'indoor']),
('Jeita Grotto Day Trip', (SELECT id FROM destinations WHERE name = 'Beirut'), 'tour', 'Visit the stunning underground limestone caves', 'full-day', 45.00, 4.8, 'moderate', ARRAY['nature', 'adventure', 'photography']);

"""

if __name__ == "__main__":
    print("Enhanced Database Schema for AI Travel Platform")
    print("=" * 60)
    print("This schema includes:")
    print("✅ User management with detailed profiles")
    print("✅ Comprehensive travel data (flights, hotels, restaurants)")
    print("✅ Advanced booking system with package management")
    print("✅ Price tracking and notifications")
    print("✅ Group booking functionality")
    print("✅ Review and rating system")
    print("✅ Calendar integration")
    print("✅ Travel guides and documents")
    print("✅ Hidden gems and local experiences")
    print("✅ Travel news and updates")
    print("✅ Optimized indexes and triggers")
    print("\nTo implement:")
    print("1. Run the DATABASE_SCHEMA in your Supabase SQL editor")
    print("2. Run the SAMPLE_DATA to populate with test data")
    print("3. Configure Row Level Security (RLS) policies")
    print("4. Set up real-time subscriptions for live updates")
