import asyncio
import os
import sys
from unittest.mock import MagicMock, AsyncMock

# Ensure we can import from local directory even without PYTHONPATH set
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_council import Council, CouncilConfig
from llm_council.engine import Response

async def run_test():
    print("--- Starting LLM Council Test (Standalone) ---")
    
    # Check for API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    is_mock = False
    
    if not api_key or api_key == "mock_key":
        print("No valid OPENROUTER_API_KEY found. Running in MOCK mode...")
        is_mock = True
    else:
        print(f"API Key found. Running with real OpenRouter API...")

    # Initialize Council
    council = Council()
    
    if is_mock:
        # Mocking the members to avoid real API calls
        for member in council.members:
            member.get_response = AsyncMock(return_value=Response(
                model=member.model_name,
                content=f"Mock response from {member.model_name} for testing."
            ))
        # Mocking the judge client for synthesis
        council.judge_client.chat.completions.create = AsyncMock(return_value=MagicMock(
            choices=[MagicMock(message=MagicMock(content="FINAL MOCK CONSENSUS: This is a synthesized test result."))]
        ))

    query = "What is the benefit of using an LLM Council?"
    print(f"\nUser Query: {query}")
    
    try:
        results = await council.query(query)
        
        print("\n--- Individual Model Insights ---")
        for resp in results.get("individual_responses", []):
            print(f"[{resp['model']}]: {resp['content'][:100]}...")
            
        print("\n--- Final Aggregated Decision ---")
        print(results.get("final_answer"))
        print("\nTest completed successfully!")
        
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(run_test())