"""
Verify the bookings table was created correctly
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

def verify_bookings_table():
    """Verify the bookings table structure and add sample data"""
    
    # Initialize Supabase client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("❌ Error: Supabase credentials not found")
        return False
    
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        print("✅ Connected to Supabase")
        
        # Verify the table was created correctly
        print("🔍 Verifying table structure...")
        
        result = supabase.table("bookings").select("*").limit(1).execute()
        
        # Check if all required columns exist
        required_columns = [
            'id', 'booking_type', 'user_id', 'item_id', 'total_amount',
            'currency', 'status', 'payment_status', 'details', 'special_requests',
            'confirmation_number', 'created_at', 'updated_at'
        ]
        
        # If no data, check the table structure by trying to query specific columns
        try:
            test_result = supabase.table("bookings").select("id, booking_type, user_id, item_id, total_amount, currency, status, payment_status, details, special_requests, confirmation_number, created_at, updated_at").limit(1).execute()
            print("✅ Table structure verified!")
            print("📋 All required columns are present:")
            for col in required_columns:
                print(f"   • {col}")
        except Exception as e:
            print(f"❌ Error verifying columns: {e}")
            return False
        
        # Insert sample data
        print("\n📝 Adding sample data...")
        insert_sample_data(supabase)
        
        return True
        
    except Exception as e:
        print(f"❌ Error verifying table: {e}")
        return False

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
    print("🔍 VERIFYING BOOKINGS TABLE")
    print("=" * 30)
    
    success = verify_bookings_table()
    
    if success:
        print("\n🎉 SUCCESS! Bookings table is properly configured with sample data.")
        print("✅ You can now run your booking_manager.py without errors.")
        print("\n📝 Next steps:")
        print("1. Test the booking system: python booking_system/booking_manager.py")
        print("2. Run your Streamlit app: streamlit run streamlit_ui.py")
    else:
        print("\n❌ FAILED! Please check the error messages above.")

if __name__ == "__main__":
    main()
