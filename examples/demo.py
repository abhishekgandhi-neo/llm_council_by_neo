import asyncio
import os
from dotenv import load_dotenv
from llm_council import Council, get_config

# Load environment variables from .env if it exists
load_dotenv()

async def main():
    # Ensure OPENROUTER_API_KEY is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Please set OPENROUTER_API_KEY in your environment or .env file.")
        # For the sake of the demo, we'll try to proceed, but it will likely fail 
        # unless the environment is already configured.
    
    print("--- Initializing LLM Council ---")
    council = Council()
    
    question = "What are the primary ethical concerns regarding the development of AGI, and how can they be mitigated?"
    
    print(f"\nQuerying Council with question: {question}\n")
    print("Gathering responses from members...")
    
    result = await council.query(question)
    
    if "error" in result:
        print(f"Error: {result['error']}")
        return

    print(f"\n--- Strategy Used: {result['strategy']} ---")
    print("\n--- Individual Responses Summary ---")
    for resp in result['individual_responses']:
        print(f"Model: {resp['model']} | Response Length: {len(resp['content'])} chars")
    
    print("\n--- Final Aggregated/Synthesized Answer ---")
    print(result['final_answer'])

if __name__ == "__main__":
    asyncio.run(main())