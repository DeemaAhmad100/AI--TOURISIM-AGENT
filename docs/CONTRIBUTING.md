# 🤝 Contributing to AI Travel Platform

We love your input! We want to make contributing to the AI Travel Platform as easy and transparent as possible.

## 🚀 Development Process

We use GitHub to sync code, track issues, feature requests, and accept pull requests.

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/AI--TOURISIM-AGENT.git
cd AI--TOURISIM-AGENT
```

### 2. Set Up Development Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Configure your API keys in .env
# Get your keys from:
# - CrewAI: https://app.crewai.com/
# - Supabase: https://app.supabase.com/
```

### 3. Run Tests
```bash
# Run all tests
python tests/run_all_tests.py

# Run specific test
python tests/test_individual_modules.py
```

### 4. Development Workflow

1. **Create a branch**: `git checkout -b feature/amazing-feature`
2. **Make changes**: Follow our code style guidelines
3. **Add tests**: For any new functionality
4. **Run tests**: Ensure all tests pass
5. **Commit**: Use clear, descriptive commit messages
6. **Push**: `git push origin feature/amazing-feature`
7. **Pull Request**: Open a PR with a clear description

## 📝 Code Style Guidelines

### Python Code Style
- Follow PEP 8 conventions
- Use type hints where possible
- Add docstrings to all functions and classes
- Keep functions focused and small

### Example:
```python
from typing import Dict, List, Optional

def analyze_destination(
    destination: str, 
    preferences: Dict[str, str]
) -> Optional[Dict[str, any]]:
    """
    Analyze a destination and return insights.
    
    Args:
        destination: The destination to analyze
        preferences: User travel preferences
        
    Returns:
        Dictionary containing destination analysis or None if error
    """
    # Implementation here
    pass
```

## 🐛 Bug Reports

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening)

## 💡 Feature Requests

We track feature requests as GitHub issues. Provide:

- **Clear title** and description
- **Use case**: Why would this feature be useful?
- **Acceptance criteria**: What defines "done"?

## 📦 Pull Request Process

1. **Update Documentation**: If you change APIs, update the README
2. **Add Tests**: For any new functionality
3. **Follow Style Guide**: Ensure code follows our conventions
4. **Update CHANGELOG**: Add entry for your changes
5. **Get Review**: Wait for maintainer review and approval

## 🏗️ Project Structure

```
src/
├── agents/           # CrewAI agent implementations
├── database/         # Database models and operations
├── intent/          # Intent detection system
├── utils/           # Utility functions
└── config/          # Configuration management

tests/               # Test suite
docs/               # Documentation
demo/               # Demo scripts
.github/            # GitHub workflows and templates
```

## 🔒 Security

If you discover a security vulnerability, please email the maintainers directly instead of using the issue tracker.

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙋‍♀️ Questions?

Feel free to open an issue for:
- Questions about the codebase
- Clarification on features
- General discussion

---

**Thank you for contributing!** 🎉
