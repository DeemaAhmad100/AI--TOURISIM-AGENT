#!/usr/bin/env python3
"""
🔧 Configuration Usage Example
Example showing how to use the centralized configuration system
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from core.config import config, get_openai_config, get_supabase_config, get_stripe_config

def main():
    """Demonstrate configuration usage"""
    
    print("🔧 AI Travel Platform - Configuration Usage Example")
    print("=" * 60)
    
    # 1. Check configuration status
    print("\n1. Configuration Status:")
    config.print_config_status()
    
    # 2. Access individual config values
    print("\n2. Individual Configuration Values:")
    print(f"   App Name: {config.APP_NAME}")
    print(f"   App Version: {config.APP_VERSION}")
    print(f"   Environment: {config.ENVIRONMENT}")
    print(f"   Debug Mode: {config.DEBUG}")
    print(f"   OpenAI Model: {config.OPENAI_MODEL}")
    print(f"   Default Budget: ${config.DEFAULT_BUDGET}")
    print(f"   Default Currency: {config.DEFAULT_CURRENCY}")
    
    # 3. Use helper functions for common configs
    print("\n3. Helper Functions:")
    
    # OpenAI configuration
    openai_config = get_openai_config()
    print(f"   OpenAI Config: {openai_config}")
    
    # Supabase configuration
    supabase_config = get_supabase_config()
    print(f"   Supabase Config: {supabase_config}")
    
    # Stripe configuration
    stripe_config = get_stripe_config()
    print(f"   Stripe Config: {stripe_config}")
    
    # 4. Feature flags
    print("\n4. Feature Flags:")
    print(f"   Email Service: {config.is_feature_enabled('email_service')}")
    print(f"   Payment Processing: {config.is_feature_enabled('payment_processing')}")
    print(f"   Price Tracking: {config.is_feature_enabled('price_tracking')}")
    
    # 5. Feature configuration
    print("\n5. Feature Configuration:")
    email_config = config.get_feature_config('email_service')
    print(f"   Email Service Config: {email_config}")
    
    payment_config = config.get_feature_config('payment_processing')
    print(f"   Payment Config: {payment_config}")
    
    # 6. Validation
    print("\n6. Configuration Validation:")
    missing_configs = config.get_missing_config()
    if missing_configs:
        print(f"   Missing configs: {missing_configs}")
    else:
        print("   ✅ All required configurations are present!")
    
    print("\n" + "=" * 60)
    print("✅ Configuration system is working properly!")
    print("\n💡 Usage in your code:")
    print("   from core.config import config")
    print("   api_key = config.OPENAI_API_KEY")
    print("   is_debug = config.DEBUG")
    print("   feature_enabled = config.is_feature_enabled('email_service')")

if __name__ == "__main__":
    main()
