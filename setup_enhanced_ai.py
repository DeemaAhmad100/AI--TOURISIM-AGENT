"""
🚀 Enhanced AI Setup Script
Automated setup for conversation memory, psychology analysis, and real-time validation
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("Please upgrade to Python 3.8 or higher")
        return False

def install_requirements():
    """Install Python requirements"""
    requirements_files = [
        "requirements.txt",
        "requirements_enhanced_ai.txt"
    ]
    
    for req_file in requirements_files:
        if os.path.exists(req_file):
            if not run_command(f"pip install -r {req_file}", f"Installing {req_file}"):
                return False
        else:
            print(f"⚠️ {req_file} not found, skipping...")
    
    return True

def setup_spacy():
    """Setup spaCy language model"""
    return run_command(
        "python -m spacy download en_core_web_sm",
        "Downloading spaCy English language model"
    )

def setup_nltk():
    """Setup NLTK data"""
    nltk_setup_script = '''
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

print("Downloading NLTK data...")
nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
print("NLTK data downloaded successfully!")
'''
    
    with open("temp_nltk_setup.py", "w") as f:
        f.write(nltk_setup_script)
    
    success = run_command("python temp_nltk_setup.py", "Setting up NLTK data")
    
    # Clean up temporary file
    if os.path.exists("temp_nltk_setup.py"):
        os.remove("temp_nltk_setup.py")
    
    return success

def create_directory_structure():
    """Create necessary directory structure"""
    directories = [
        "src/ai_agents/memory",
        "src/ai_agents/psychology", 
        "src/ai_agents/validation",
        "src/ai_agents/integration",
        "data/conversations",
        "data/user_profiles",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")
    
    return True

def create_env_file():
    """Create .env file template"""
    env_content = """# Enhanced AI Travel Platform Environment Variables

# === API Keys ===
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# === Database Configuration ===
DATABASE_URL=sqlite:///data/travel_agent.db
CONVERSATION_DB_PATH=data/conversations/conversations.db

# === AI Configuration ===
PSYCHOLOGY_ANALYSIS_ENABLED=True
CONVERSATION_MEMORY_ENABLED=True
REAL_TIME_VALIDATION_ENABLED=True

# === Streamlit Configuration ===
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost

# === Feature Flags ===
ENHANCED_MODE_DEFAULT=True
DEBUG_MODE=False
LOGGING_LEVEL=INFO

# === External APIs (Optional) ===
AMADEUS_API_KEY=your_amadeus_key
STRIPE_PUBLISHABLE_KEY=your_stripe_key
STRIPE_SECRET_KEY=your_stripe_secret

# === Advanced Features ===
ENABLE_DEEP_LEARNING=False
ENABLE_ADVANCED_NLP=True
MAX_CONVERSATION_HISTORY=100
PSYCHOLOGY_CONFIDENCE_THRESHOLD=0.7
"""
    
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ Created .env file template")
        print("⚠️ Please update .env with your actual API keys!")
    else:
        print("📄 .env file already exists")
    
    return True

def test_installation():
    """Test if installation was successful"""
    test_script = '''
print("🧪 Testing Enhanced AI Installation...")

# Test imports
try:
    import streamlit
    print("✅ Streamlit imported successfully")
except ImportError as e:
    print(f"❌ Streamlit import failed: {e}")

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("✅ spaCy model loaded successfully")
except Exception as e:
    print(f"❌ spaCy test failed: {e}")

try:
    from textblob import TextBlob
    blob = TextBlob("test")
    print("✅ TextBlob imported successfully")
except ImportError as e:
    print(f"❌ TextBlob import failed: {e}")

try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    print("✅ NLTK sentiment analyzer loaded successfully")
except Exception as e:
    print(f"❌ NLTK test failed: {e}")

try:
    import sqlite3
    conn = sqlite3.connect(":memory:")
    conn.close()
    print("✅ SQLite database connection successful")
except Exception as e:
    print(f"❌ SQLite test failed: {e}")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("✅ Scikit-learn imported successfully")
except ImportError as e:
    print(f"❌ Scikit-learn import failed: {e}")

print("\\n🎉 Installation test completed!")
'''
    
    with open("temp_test.py", "w") as f:
        f.write(test_script)
    
    success = run_command("python temp_test.py", "Testing installation")
    
    # Clean up
    if os.path.exists("temp_test.py"):
        os.remove("temp_test.py")
    
    return success

def main():
    """Main setup function"""
    print("🚀 Enhanced AI Travel Platform Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directory structure
    print("\n📁 Creating directory structure...")
    if not create_directory_structure():
        return False
    
    # Install requirements
    print("\n📦 Installing Python packages...")
    if not install_requirements():
        print("⚠️ Some packages failed to install. You may need to install them manually.")
    
    # Setup spaCy
    print("\n🔤 Setting up spaCy...")
    if not setup_spacy():
        print("⚠️ spaCy setup failed. Try running manually: python -m spacy download en_core_web_sm")
    
    # Setup NLTK
    print("\n📚 Setting up NLTK...")
    if not setup_nltk():
        print("⚠️ NLTK setup failed. You may need to run setup manually.")
    
    # Create environment file
    print("\n⚙️ Creating environment configuration...")
    create_env_file()
    
    # Test installation
    print("\n🧪 Testing installation...")
    test_installation()
    
    print("\n" + "=" * 50)
    print("🎉 Setup Complete!")
    print("\n📋 Next Steps:")
    print("1. Update your .env file with actual API keys")
    print("2. Run: streamlit run enhanced_streamlit_app.py")
    print("3. Enable Enhanced AI Mode in the sidebar")
    print("4. Start creating AI-powered travel packages!")
    print("\n💡 Features Available:")
    print("  • 🧠 Conversation Memory")
    print("  • 🔬 Enhanced Psychology Analysis") 
    print("  • ⚡ Real-time Validation & Modification")
    print("  • 🔗 Advanced AI Integration")

if __name__ == "__main__":
    main()
