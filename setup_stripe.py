#!/usr/bin/env python3
"""
🔧 Stripe Setup Configuration
Configure Stripe API keys for real payment processing
"""

import os
from pathlib import Path

def setup_stripe_environment():
    """
    Set up Stripe environment variables
    """
    
    print("🔧 Setting up Stripe Payment Integration")
    print("="*50)
    
    # Check if .env file exists
    env_file = Path(".env")
    
    print(f"📁 Environment file: {env_file.absolute()}")
    
    # Stripe configuration prompts
    print("\n💳 Stripe Configuration")
    print("-" * 30)
    
    print("""
To enable real Stripe payments, you need to:

1. 📝 Create a Stripe account at https://stripe.com
2. 🔑 Get your API keys from https://dashboard.stripe.com/apikeys
3. 🎯 Set up webhooks at https://dashboard.stripe.com/webhooks

For testing, use Stripe's test keys (they start with 'pk_test_' and 'sk_test_')
For production, use live keys (they start with 'pk_live_' and 'sk_live_')
""")
    
    # Get user input
    print("Enter your Stripe keys (press Enter to skip):")
    
    publishable_key = input("Stripe Publishable Key (pk_test_...): ").strip()
    secret_key = input("Stripe Secret Key (sk_test_...): ").strip()
    webhook_secret = input("Stripe Webhook Secret (whsec_...): ").strip()
    
    # Read existing .env file
    env_content = ""
    if env_file.exists():
        with open(env_file, 'r') as f:
            env_content = f.read()
    
    # Prepare new environment variables
    new_vars = {}
    
    if publishable_key:
        new_vars['STRIPE_PUBLISHABLE_KEY'] = publishable_key
        new_vars['STRIPE_PUBLIC_KEY'] = publishable_key  # Legacy support
    
    if secret_key:
        new_vars['STRIPE_SECRET_KEY'] = secret_key
    
    if webhook_secret:
        new_vars['STRIPE_WEBHOOK_SECRET'] = webhook_secret
    
    # Add default payment settings
    new_vars['PAYMENT_CURRENCY'] = 'usd'
    new_vars['PAYMENT_SUCCESS_URL'] = 'http://localhost:8501?payment=success&session_id={CHECKOUT_SESSION_ID}'
    new_vars['PAYMENT_CANCEL_URL'] = 'http://localhost:8501?payment=cancelled'
    
    # Update .env file
    if new_vars:
        # Remove existing Stripe vars
        env_lines = env_content.split('\n')
        filtered_lines = [line for line in env_lines 
                         if not any(line.startswith(key + '=') for key in new_vars.keys())]
        
        # Add new vars
        for key, value in new_vars.items():
            filtered_lines.append(f"{key}={value}")
        
        # Write back to file
        with open(env_file, 'w') as f:
            f.write('\n'.join(filtered_lines))
        
        print(f"\n✅ Updated {env_file.absolute()}")
        print("\n🔑 Added/Updated environment variables:")
        for key in new_vars.keys():
            if 'SECRET' in key or 'WEBHOOK' in key:
                print(f"   {key}=***hidden***")
            else:
                print(f"   {key}={new_vars[key]}")
    
    else:
        print("\n⏭️ No Stripe keys provided - using test/simulation mode")
    
    print("\n🚀 Setup complete!")
    
    # Display test card information
    if secret_key and secret_key.startswith('sk_test_'):
        print("\n💳 Test Card Numbers for Stripe Testing:")
        print("   Success: 4242 4242 4242 4242")
        print("   Decline: 4000 0000 0000 0002")
        print("   Require Authentication: 4000 0025 0000 3155")
        print("   Expired: Use any past date")
        print("   CVV: Any 3 digits")
    
    # Display webhook setup instructions
    if webhook_secret:
        print("\n🔗 Webhook Setup:")
        print("   1. Go to https://dashboard.stripe.com/webhooks")
        print("   2. Create endpoint: http://localhost:8501/stripe-webhook")
        print("   3. Select events: checkout.session.completed, payment_intent.succeeded")
        print("   4. Copy webhook secret to STRIPE_WEBHOOK_SECRET")

def verify_stripe_setup():
    """
    Verify Stripe configuration
    """
    
    print("\n🔍 Verifying Stripe Setup")
    print("-" * 30)
    
    # Check environment variables
    required_vars = ['STRIPE_SECRET_KEY']
    optional_vars = ['STRIPE_PUBLISHABLE_KEY', 'STRIPE_WEBHOOK_SECRET']
    
    missing_required = []
    missing_optional = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_required.append(var)
        else:
            print(f"✅ {var}: Set")
    
    for var in optional_vars:
        if not os.getenv(var):
            missing_optional.append(var)
        else:
            print(f"✅ {var}: Set")
    
    if missing_required:
        print(f"\n❌ Missing required variables: {', '.join(missing_required)}")
        print("   Payment processing will not work!")
        return False
    
    if missing_optional:
        print(f"\n⚠️ Missing optional variables: {', '.join(missing_optional)}")
        print("   Some features may be limited")
    
    # Test Stripe connection
    try:
        import stripe
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        
        # Simple API test
        stripe.Account.retrieve()
        print("\n✅ Stripe API connection: Working")
        return True
        
    except ImportError:
        print("\n❌ Stripe library not installed")
        print("   Run: pip install stripe")
        return False
        
    except Exception as e:
        print(f"\n❌ Stripe API connection failed: {e}")
        return False

if __name__ == "__main__":
    try:
        # Setup environment
        setup_stripe_environment()
        
        # Reload environment
        from dotenv import load_dotenv
        load_dotenv(override=True)
        
        # Verify setup
        verify_stripe_setup()
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")