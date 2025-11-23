#!/usr/bin/env python3
"""
🔧 AI Travel Platform - Configuration Management
Centralized configuration settings for the entire platform
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Centralized configuration management for the AI Travel Platform
    """
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.config_dir = self.base_dir / "config"
        self.load_enhanced_features()
    
    # =============================================================================
    # API CONFIGURATION
    # =============================================================================
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
    
    # Tavily Search API
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    MAX_SEARCH_RESULTS: int = int(os.getenv("MAX_SEARCH_RESULTS", "5"))
    
    # Supabase Database Configuration
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    
    # Stripe Payment Configuration
    STRIPE_PUBLISHABLE_KEY: str = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
    STRIPE_PUBLIC_KEY: str = os.getenv("STRIPE_PUBLIC_KEY", "")  # Legacy support
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    
    # Payment processing settings
    PAYMENT_CURRENCY: str = os.getenv("PAYMENT_CURRENCY", "usd")
    PAYMENT_SUCCESS_URL: str = os.getenv("PAYMENT_SUCCESS_URL", "http://localhost:8501?payment=success&session_id={CHECKOUT_SESSION_ID}")
    PAYMENT_CANCEL_URL: str = os.getenv("PAYMENT_CANCEL_URL", "http://localhost:8501?payment=cancelled")
    
    # Google APIs Configuration
    GOOGLE_MAPS_API_KEY: str = os.getenv("GOOGLE_MAPS_API_KEY", "")
    GOOGLE_PLACES_API_KEY: str = os.getenv("GOOGLE_PLACES_API_KEY", "")
    GOOGLE_CALENDAR_API_KEY: str = os.getenv("GOOGLE_CALENDAR_API_KEY", "")
    
    # =============================================================================
    # APPLICATION CONFIGURATION
    # =============================================================================
    
    # Application Settings
    APP_NAME: str = "AI Travel Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Streamlit Configuration
    STREAMLIT_SERVER_PORT: int = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))
    STREAMLIT_SERVER_ADDRESS: str = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")
    STREAMLIT_THEME: str = os.getenv("STREAMLIT_THEME", "light")
    
    # Email Configuration
    EMAIL_ENABLED: bool = os.getenv("EMAIL_ENABLED", "False").lower() == "true"
    EMAIL_BACKEND: str = os.getenv("EMAIL_BACKEND", "sendgrid")
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY", "")
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    
    # =============================================================================
    # CREWAI CONFIGURATION
    # =============================================================================
    
    # CrewAI Settings
    CREWAI_ENABLED: bool = os.getenv("CREWAI_ENABLED", "True").lower() == "true"
    CREWAI_VERBOSE: bool = os.getenv("CREWAI_VERBOSE", "False").lower() == "true"
    CREWAI_MAX_ITERATIONS: int = int(os.getenv("CREWAI_MAX_ITERATIONS", "10"))
    CREWAI_TEMPERATURE: float = float(os.getenv("CREWAI_TEMPERATURE", "0.7"))
    
    # =============================================================================
    # LANGCHAIN CONFIGURATION
    # =============================================================================
    
    # LangChain Settings
    LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2", "False").lower() == "true"
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY", "")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "ai-travel-platform")
    
    # =============================================================================
    # SECURITY CONFIGURATION
    # =============================================================================
    
    # Security Settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-here")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_DELTA: int = int(os.getenv("JWT_EXPIRATION_DELTA", "3600"))
    
    # =============================================================================
    # LOGGING CONFIGURATION
    # =============================================================================
    
    # Logging Settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    LOG_FILE: str = os.getenv("LOG_FILE", "app.log")
    
    # =============================================================================
    # BUSINESS LOGIC CONFIGURATION
    # =============================================================================
    
    # Travel Planning Settings
    DEFAULT_TRIP_DURATION: int = int(os.getenv("DEFAULT_TRIP_DURATION", "7"))
    DEFAULT_BUDGET: int = int(os.getenv("DEFAULT_BUDGET", "2000"))
    DEFAULT_CURRENCY: str = os.getenv("DEFAULT_CURRENCY", "USD")
    MAX_GROUP_SIZE: int = int(os.getenv("MAX_GROUP_SIZE", "50"))
    
    # Booking Settings
    BOOKING_CONFIRMATION_TIMEOUT: int = int(os.getenv("BOOKING_CONFIRMATION_TIMEOUT", "600"))
    MAX_BOOKING_ATTEMPTS: int = int(os.getenv("MAX_BOOKING_ATTEMPTS", "3"))
    
    # =============================================================================
    # FEATURE FLAGS
    # =============================================================================
    
    def load_enhanced_features(self) -> None:
        """Load enhanced features configuration from JSON file"""
        try:
            features_file = self.config_dir / "enhanced_features.json"
            if features_file.exists():
                with open(features_file, 'r') as f:
                    self.enhanced_features = json.load(f)
            else:
                self.enhanced_features = {}
        except Exception as e:
            print(f"Warning: Could not load enhanced features config: {e}")
            self.enhanced_features = {}
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if a specific feature is enabled"""
        return self.enhanced_features.get("enhanced_features", {}).get(feature_name, {}).get("enabled", False)
    
    def get_feature_config(self, feature_name: str) -> Dict[str, Any]:
        """Get configuration for a specific feature"""
        return self.enhanced_features.get("enhanced_features", {}).get(feature_name, {})
    
    # =============================================================================
    # VALIDATION METHODS
    # =============================================================================
    
    def validate_required_config(self) -> Dict[str, bool]:
        """Validate that all required configuration is present"""
        required_configs = {
            "OPENAI_API_KEY": bool(self.OPENAI_API_KEY),
            "SUPABASE_URL": bool(self.SUPABASE_URL),
            "SUPABASE_KEY": bool(self.SUPABASE_KEY),
        }
        
        # Add conditional requirements
        if self.is_feature_enabled("payment_processing"):
            required_configs["STRIPE_SECRET_KEY"] = bool(self.STRIPE_SECRET_KEY)
        
        if self.is_feature_enabled("email_service"):
            required_configs["SENDGRID_API_KEY"] = bool(self.SENDGRID_API_KEY)
        
        return required_configs
    
    def get_missing_config(self) -> list:
        """Get list of missing required configuration"""
        validation = self.validate_required_config()
        return [key for key, is_valid in validation.items() if not is_valid]
    
    def print_config_status(self) -> None:
        """Print current configuration status"""
        print("🔧 Configuration Status:")
        print("=" * 50)
        
        validation = self.validate_required_config()
        for key, is_valid in validation.items():
            status = "✅" if is_valid else "❌"
            print(f"{status} {key}: {'Configured' if is_valid else 'Missing'}")
        
        missing = self.get_missing_config()
        if missing:
            print(f"\n⚠️  Missing configuration: {', '.join(missing)}")
            print("Please check your .env file and ensure all required variables are set.")
        else:
            print("\n✅ All required configuration is present!")

# Create global config instance
config = Config()

# Export commonly used configurations
__all__ = [
    'config',
    'Config'
]

# Quick access to frequently used settings
def get_openai_config() -> Dict[str, Any]:
    """Get OpenAI configuration"""
    return {
        "api_key": config.OPENAI_API_KEY,
        "model": config.OPENAI_MODEL,
        "temperature": config.OPENAI_TEMPERATURE,
        "max_tokens": config.OPENAI_MAX_TOKENS
    }

def get_supabase_config() -> Dict[str, str]:
    """Get Supabase configuration"""
    return {
        "url": config.SUPABASE_URL,
        "key": config.SUPABASE_KEY
    }

def get_stripe_config() -> Dict[str, str]:
    """Get Stripe configuration"""
    return {
        "public_key": config.STRIPE_PUBLIC_KEY,
        "secret_key": config.STRIPE_SECRET_KEY,
        "webhook_secret": config.STRIPE_WEBHOOK_SECRET
    }

# Development helper
if __name__ == "__main__":
    config.print_config_status()