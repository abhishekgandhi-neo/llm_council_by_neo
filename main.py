import os
import asyncio
from dotenv import load_dotenv
from llm_council.engine import Council
from llm_council.config import get_config

async def main():
    load_dotenv()
    
    # Initialize config and council
    config = get_config()
    council = Council(config)
    
    print(f"Active Council Models: {config.council_models}")
    
    query = "What are the core benefits of a multi-LLM orchestration pattern like a 'Council' for complex reasoning tasks?"
    print(f"\nQuerying the LLM Council: {query}\n")
    
    try:
        result = await council.query(query)
        
        if "error" in result:
            print(f"Error: {result['error']}")
            return

        output_file = "council_answer.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Council Query: {query}\n\n")
            f.write(f"## Aggregated Response ({result['strategy']})\n\n{result['final_answer']}\n\n")
            f.write("## Individual Contributions\n\n")
            for resp in result['individual_responses']:
                f.write(f"### {resp['model']}\n{resp['content']}\n\n")
        
        print(f"Success! Response generated in {output_file}")
        print("\n--- Final Answer Summary ---\n")
        print(result['final_answer'][:500] + "...")
        
    except Exception as e:
        print(f"Engine Execution Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())