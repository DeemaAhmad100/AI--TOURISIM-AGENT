"""
🚀 AI Integration Status Test
Quick verification that AI features are properly integrated and accessible
"""

import sys
import streamlit as st
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.append(str(src_path))

st.title("🤖 AI Integration Status")

# Test imports
try:
    from ai_agents.integration.advanced_ai_integrator import ai_integrator, MODULES_AVAILABLE
    st.success("✅ AI Integrator imported successfully!")
    
    if MODULES_AVAILABLE:
        st.success("✅ All AI modules are available!")
        
        # Test functionality
        with st.spinner("Testing AI processing..."):
            result = ai_integrator.process_user_input_with_ai("I want to explore Paris!", "test_user")
        
        st.success("✅ AI processing test completed!")
        
        # Show results
        st.subheader("📊 AI Analysis Results")
        with st.expander("View detailed results"):
            st.json(result)
            
        # Show specific features
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🧠 Memory System", "Available" if result.get("conversation_context") else "N/A")
        
        with col2:
            st.metric("🔮 Psychology Analysis", "Available" if result.get("psychology_analysis") else "N/A")
            
        with col3:
            st.metric("📋 Validation System", "Available")
    else:
        st.warning("⚠️ AI modules imported but some components are not available")
        
except ImportError as e:
    st.error(f"❌ AI Import Error: {e}")
except Exception as e:
    st.error(f"❌ AI Runtime Error: {e}")
    
st.divider()
st.subheader("🎯 Next Steps")
st.info("""
If all tests pass above:
1. 🌟 Enable Enhanced AI Mode in the main app sidebar
2. 🔍 Try creating a travel package with AI assistance
3. 💬 Experience personalized conversation memory
4. 🧠 See psychology-based recommendations in action
""")
