import json
import os
from datetime import datetime
from .tools.market_trend_check import market_trend_check
from .tools.pain_point_matcher import pain_point_matcher
from .tools.uniqueness_scorer import uniqueness_scorer

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IdeaRequest(BaseModel):
    idea: str

def validate_idea(idea: str):
    """Validate a startup idea using all tools"""
    idea = idea.strip()
    if not idea:
        return {"error": "Startup idea cannot be empty."}

    results = {
        "market_trend_check": market_trend_check(idea),
        "pain_point_matcher": pain_point_matcher(idea),
        "uniqueness_scorer": uniqueness_scorer(idea)
    }

    return results

@app.post("/validate")
def validate_idea_api(request: IdeaRequest):
    """FastAPI endpoint for idea validation"""
    return validate_idea(request.idea)

def save_result(idea, results, filename="validated_ideas.json"):
    entry = {
        "idea": idea,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }

    # Load existing data if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    # Save updated data
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    print("💡 Idea Validator AI - Multi-Idea Mode")
    print("=" * 40)
    print("Enter ideas one at a time, or type 'file' to load from ideas.txt.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("🚀 Enter your startup idea (or 'file' / 'quit'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            elif user_input.lower() == 'file':
                if not os.path.exists("ideas.txt"):
                    print("❌ No 'ideas.txt' file found.")
                    continue

                with open("ideas.txt", "r") as f:
                    ideas = [line.strip() for line in f if line.strip()]
                    print(f"📄 Found {len(ideas)} ideas in ideas.txt\n")

                for idea in ideas:
                    print(f"💡 Validating: {idea}")
                    results = validate_idea(idea)
                    save_result(idea, results)
                    print("✅ Done\n")

            else:
                idea = user_input
                results = validate_idea(idea)
                print("\n✅ Validation Results:")
                print("-" * 30)
                for tool_name, result in results.items():
                    print(f"🔧 {tool_name.replace('_', ' ').title()}:")
                    print(f"   {result}")
                    print()
                save_result(idea, results)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
