-- 🍽️ Restaurant Data - SQL INSERT Statements for Supabase
-- Copy and paste this entire script into your Supabase SQL Editor

-- Insert restaurants with proper data for your AI Travel Platform
INSERT INTO restaurants (
    name,
    cuisine_type,
    rating,
    price_range,
    specialties,
    phone,
    address,
    reservation_required,
    local_authenticity,
    tourist_trap_score,
    created_at
) VALUES 

-- Beirut Restaurants
('Em Sherif Restaurant', 'Lebanese Fine Dining', 4.9, 'expensive', 
 ARRAY['Mixed Mezze', 'Grilled Lamb', 'Fattoush', 'Baklava'], 
 '+961-1-322-722', 'Ashrafieh, Beirut, Lebanon', true, 8, 3, NOW()),

('Babel Bay', 'Mediterranean', 4.5, 'moderate', 
 ARRAY['Seafood Mezze', 'Grilled Fish', 'Mediterranean Salads'], 
 '+961-1-565-777', 'Zaitunay Bay, Beirut, Lebanon', false, 7, 4, NOW()),

('Urbanista Beirut', 'International', 4.6, 'expensive', 
 ARRAY['Fusion Dishes', 'Craft Cocktails', 'International Tapas'], 
 '+961-1-988-555', 'Hamra District, Beirut, Lebanon', true, 6, 3, NOW()),

-- Dubai Restaurants
('Pierchic', 'Seafood', 4.6, 'expensive', 
 ARRAY['Fresh Lobster', 'Sea Bass', 'Oysters', 'Seafood Platter'], 
 '+971-4-432-3232', 'Al Qasr, Madinat Jumeirah, Dubai', true, 6, 5, NOW()),

('Zuma Dubai', 'Japanese Contemporary', 4.7, 'expensive', 
 ARRAY['Robata Grill', 'Sushi', 'Sake Selection'], 
 '+971-4-425-5660', 'Gate Village, DIFC, Dubai', true, 5, 4, NOW()),

('Al Hadheerah', 'Traditional Emirati', 4.4, 'moderate', 
 ARRAY['Lamb Ouzi', 'Camel Meat', 'Arabic Coffee', 'Date Sweets'], 
 '+971-4-432-3000', 'Al Sahra Desert Resort, Dubai', true, 9, 3, NOW()),

-- Paris Restaurants
('Le Jules Verne', 'French Fine Dining', 4.4, 'expensive', 
 ARRAY['French Gastronomy', 'Seasonal Menu', 'Wine Pairing'], 
 '+33-1-45-55-61-44', 'Eiffel Tower, 2nd Floor, Paris', true, 7, 8, NOW()),

('L''As du Fallafel', 'Middle Eastern', 4.3, 'budget', 
 ARRAY['Falafel', 'Shawarma', 'Hummus', 'Fresh Pita'], 
 '+33-1-48-87-63-60', '34 Rue des Rosiers, Marais, Paris', false, 8, 2, NOW()),

('L''Ami Jean', 'French Bistro', 4.6, 'moderate', 
 ARRAY['Cassoulet', 'Duck Confit', 'French Wine'], 
 '+33-1-47-05-86-89', '27 Rue Malar, 7th Arrondissement, Paris', true, 9, 1, NOW()),

('Breizh Café', 'French Contemporary', 4.5, 'moderate', 
 ARRAY['Gourmet Crêpes', 'Buckwheat Galettes', 'Organic Cider'], 
 '+33-1-42-72-13-77', '109 Rue Vieille du Temple, Marais, Paris', false, 7, 3, NOW()),

-- Tokyo Restaurants
('Sukiyabashi Jiro', 'Sushi', 4.8, 'expensive', 
 ARRAY['Omakase Sushi', 'Premium Fish', 'Traditional Technique'], 
 '+81-3-3535-3600', 'Ginza, Tokyo', true, 10, 2, NOW()),

('Gonpachi Shibuya', 'Japanese Traditional', 4.4, 'moderate', 
 ARRAY['Yakitori', 'Sake', 'Robatayaki'], 
 '+81-3-5771-0170', 'Shibuya, Tokyo', false, 8, 3, NOW()),

('Narisawa', 'Japanese Contemporary', 4.7, 'expensive', 
 ARRAY['Innovative Techniques', 'Local Ingredients', 'Nature-inspired'], 
 '+81-3-5785-0799', 'Minato, Tokyo', true, 9, 2, NOW()),

-- London Restaurants
('Dishoom', 'Indian', 4.6, 'moderate', 
 ARRAY['Black Dal', 'Pau Bhaji', 'Biryanis', 'Masala Chai'], 
 '+44-20-7420-9320', 'Covent Garden, London', false, 7, 4, NOW()),

('Rules Restaurant', 'British Traditional', 4.3, 'expensive', 
 ARRAY['Game Meats', 'British Classics', 'Historic Atmosphere'], 
 '+44-20-7836-5314', 'Covent Garden, London', true, 9, 5, NOW()),

('Sketch', 'French Contemporary', 4.5, 'expensive', 
 ARRAY['Modern French', 'Artistic Presentation', 'Afternoon Tea'], 
 '+44-20-7659-4500', 'Mayfair, London', true, 6, 6, NOW()),

('Borough Market Restaurant', 'British Modern', 4.4, 'moderate', 
 ARRAY['Market Fresh', 'British Seasonal', 'Local Produce'], 
 '+44-20-7407-1002', 'Borough Market, London', false, 8, 3, NOW());

-- Verify the insertion
SELECT COUNT(*) as total_restaurants FROM restaurants;
SELECT name, cuisine_type, rating, price_range FROM restaurants ORDER BY created_at DESC LIMIT 10;
