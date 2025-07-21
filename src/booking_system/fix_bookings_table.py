"""
Fix the bookings table structure
This script will create the proper bookings table with all required columns
"""

import os
import sys
from pathlib import Path
from supabase import create_client, Client
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Load environment variables
load_dotenv()

def fix_bookings_table():
    """Create the correct bookings table structure"""
    
    # Initialize Supabase client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("❌ Error: Supabase credentials not found")
        print("💡 Make sure SUPABASE_URL and SUPABASE_KEY are set in your .env file")
        return False
    
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase")
        
        # Check if bookings table exists
        print("🔍 Checking current bookings table...")
        
        try:
            result = supabase.table("bookings").select("*").limit(1).execute()
            print("⚠️  Bookings table exists but may have wrong structure")
            
            if result.data:
                print("📋 Current table columns:")
                for key in result.data[0].keys():
                    print(f"   • {key}")
            
            # Ask user if they want to recreate the table
            print("\n🔄 To fix the table structure, we need to recreate it.")
            print("⚠️  This will DELETE ALL EXISTING DATA in the bookings table!")
            
            response = input("\nDo you want to proceed? (yes/y/no/n): ").strip().lower()
            
            if response not in ['yes', 'y']:
                print("❌ Operation cancelled by user")
                return False
            
        except Exception as e:
            print(f"📝 Bookings table doesn't exist or has issues: {e}")
            print("✅ Will create new table")
        
        # Show the SQL that needs to be executed
        sql_commands = get_table_creation_sql()
        
        print("\n📝 COPY AND PASTE THIS SQL INTO YOUR SUPABASE SQL EDITOR:")
        print("=" * 60)
        print(sql_commands)
        print("=" * 60)
        
        print("\n🌐 Steps to execute:")
        print("1. Go to your Supabase dashboard")
        print("2. Navigate to SQL Editor")
        print("3. Copy and paste the SQL above")
        print("4. Click 'Run' to execute")
        
        input("\nPress Enter after you've executed the SQL in Supabase...")
        
        # Verify the table was created correctly
        print("\n🔍 Verifying table structure...")
        try:
            result = supabase.table("bookings").select("*").limit(1).execute()
            
            # Check if all required columns exist
            required_columns = [
                'id', 'booking_type', 'user_id', 'item_id', 'total_amount',
                'currency', 'status', 'payment_status', 'details', 'special_requests',
                'confirmation_number', 'created_at', 'updated_at'
            ]
            
            if result.data:
                existing_columns = list(result.data[0].keys())
                print("✅ Table structure verified!")
                print("📋 Available columns:")
                for col in existing_columns:
                    print(f"   • {col}")
                
                # Check if all required columns exist
                missing_columns = [col for col in required_columns if col not in existing_columns]
                if missing_columns:
                    print(f"\n⚠️  Missing columns: {missing_columns}")
                    return False
                else:
                    print("\n✅ All required columns are present!")
            
            # Insert sample data
            print("\n📝 Adding sample data...")
            insert_sample_data(supabase)
            
            return True
            
        except Exception as e:
            print(f"❌ Error verifying table: {e}")
            print("💡 Make sure you executed the SQL in Supabase dashboard")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def get_table_creation_sql():
    """Get the SQL commands to create the bookings table"""
    
    return '''
-- Drop existing table if it exists (THIS WILL DELETE ALL DATA!)
DROP TABLE IF EXISTS bookings CASCADE;

-- Create the correct bookings table structure
CREATE TABLE bookings (
    -- Primary identifiers
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    confirmation_number VARCHAR(10) UNIQUE NOT NULL DEFAULT upper(substring(md5(random()::text), 1, 8)),
    
    -- Booking details
    booking_type VARCHAR(50) NOT NULL CHECK (booking_type IN ('flight', 'hotel', 'restaurant', 'car_rental', 'package')),
    user_id VARCHAR(255) NOT NULL,
    item_id VARCHAR(255) NOT NULL,
    
    -- Financial information
    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
    currency VARCHAR(3) DEFAULT 'USD',
    deposit_amount DECIMAL(10,2) DEFAULT 0,
    refunded_amount DECIMAL(10,2) DEFAULT 0,
    
    -- Status and workflow
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed', 'failed')),
    payment_status VARCHAR(20) DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'refunded', 'failed')),
    
    -- Booking details (JSON for flexibility)
    details JSONB NOT NULL DEFAULT '{}',
    special_requests TEXT[],
    
    -- Group booking support
    group_booking_id UUID,
    is_group_booking BOOLEAN DEFAULT FALSE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE,
    confirmed_at TIMESTAMP WITH TIME ZONE,
    cancelled_at TIMESTAMP WITH TIME ZONE,
    modified_at TIMESTAMP WITH TIME ZONE,
    
    -- Payment integration
    stripe_payment_intent_id VARCHAR(255),
    payment_method_id VARCHAR(255),
    
    -- Customer information
    customer_details JSONB DEFAULT '{}'
);

-- Create indexes for better performance
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_bookings_booking_type ON bookings(booking_type);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_bookings_created_at ON bookings(created_at);
CREATE INDEX idx_bookings_confirmation ON bookings(confirmation_number);

-- Updated timestamp trigger
CREATE OR REPLACE FUNCTION update_bookings_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_bookings_updated_at
    BEFORE UPDATE ON bookings
    FOR EACH ROW
    EXECUTE FUNCTION update_bookings_updated_at();

-- Add comments for documentation
COMMENT ON TABLE bookings IS 'Central table for all booking records across the travel platform';
COMMENT ON COLUMN bookings.booking_type IS 'Type of booking: flight, hotel, restaurant, car_rental, or package';
COMMENT ON COLUMN bookings.confirmation_number IS 'Short confirmation code for customer reference';
COMMENT ON COLUMN bookings.item_id IS 'References the specific item in service tables';
COMMENT ON COLUMN bookings.details IS 'Flexible JSON field for booking-specific information';
'''

def insert_sample_data(supabase: Client):
    """Insert sample data for testing"""
    
    sample_bookings = [
        {
            "booking_type": "flight",
            "user_id": "demo_user_001",
            "item_id": "flight_demo_001",
            "total_amount": 299.99,
            "currency": "USD",
            "status": "confirmed",
            "payment_status": "paid",
            "details": {
                "flight_number": "AA101",
                "departure": "JFK",
                "arrival": "LAX",
                "departure_time": "2024-08-15T08:00:00Z",
                "arrival_time": "2024-08-15T11:30:00Z",
                "passengers": 1
            },
            "special_requests": ["Window seat", "Vegetarian meal"],
            "customer_details": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890"
            }
        },
        {
            "booking_type": "hotel",
            "user_id": "demo_user_001",
            "item_id": "hotel_demo_001",
            "total_amount": 189.99,
            "currency": "USD",
            "status": "confirmed",
            "payment_status": "paid",
            "details": {
                "hotel_name": "Grand Plaza Hotel",
                "check_in": "2024-08-15",
                "check_out": "2024-08-17",
                "nights": 2,
                "room_type": "Deluxe King",
                "guests": 2
            },
            "special_requests": ["Late checkout", "High floor"],
            "customer_details": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890"
            }
        },
        {
            "booking_type": "restaurant",
            "user_id": "demo_user_002",
            "item_id": "restaurant_demo_001",
            "total_amount": 0.00,
            "currency": "USD",
            "status": "confirmed",
            "payment_status": "paid",
            "details": {
                "restaurant_name": "Le Bistro",
                "reservation_date": "2024-08-16",
                "reservation_time": "19:00",
                "party_size": 4,
                "table_preference": "Window table"
            },
            "special_requests": ["Birthday celebration"],
            "customer_details": {
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "phone": "+1234567891"
            }
        }
    ]
    
    try:
        result = supabase.table("bookings").insert(sample_bookings).execute()
        print(f"✅ Inserted {len(sample_bookings)} sample bookings")
        
        for booking in result.data:
            print(f"   • {booking['booking_type'].title()}: {booking['confirmation_number']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error inserting sample data: {e}")
        return False

def main():
    """Main function"""
    print("🔧 FIXING BOOKINGS TABLE STRUCTURE")
    print("=" * 40)
    
    success = fix_bookings_table()
    
    if success:
        print("\n🎉 SUCCESS! Bookings table is now properly configured.")
        print("✅ You can now run your booking_manager.py without errors.")
        print("\n📝 Next steps:")
        print("1. Test the booking system: python booking_system/booking_manager.py")
        print("2. Run your Streamlit app: streamlit run streamlit_ui.py")
    else:
        print("\n❌ FAILED! Please check the error messages above.")
        print("💡 Make sure you have proper Supabase credentials in your .env file")

if __name__ == "__main__":
    main()
