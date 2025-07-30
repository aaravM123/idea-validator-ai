import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import validate_idea

def test_idea():
    """Test the idea validation with a sample idea"""
    test_idea = "An AI-powered fitness coach for remote workers"
    
    print("🧪 Testing Idea Validator AI")
    print("=" * 40)
    print(f"Test idea: {test_idea}")
    print()
    
    results = validate_idea(test_idea)
    
    print("✅ Validation Results:")
    print("-" * 30)
    for tool_name, result in results.items():
        print(f"🔧 {tool_name.replace('_', ' ').title()}:")
        print(f"   {result}")
        print()

if __name__ == "__main__":
    test_idea() 