import asyncio
import os
from unittest.mock import AsyncMock, MagicMock
from llm_council import Council, CouncilConfig

async def mock_response(*args, **kwargs):
    model = kwargs.get('model', 'model')
    messages = kwargs.get('messages', [])
    m = MagicMock()
    c = MagicMock()
    msg = MagicMock()
    
    if any("synthesize" in str(msg.get('content', '')).lower() for msg in messages):
        msg.content = "FINAL COUNCIL CONSENSUS: After evaluating all insights, we conclude that AGI ethics mitigation requires a multi-layered governance framework including technical alignment, policy oversight, and global transparency."
    else:
        msg.content = f"Simulated insight from {model} regarding AGI ethics."
    
    c.message = msg
    m.choices = [c]
    return m

async def main():
    print("--- Running Verification Demo with Simulated API ---")
    cfg = CouncilConfig(openrouter_api_key="mock", council_models=["model-a", "model-b", "model-c"])
    council = Council(config=cfg)
    
    # Inject mocks
    for member in council.members:
        member.client.chat.completions.create = AsyncMock(side_effect=mock_response)
    council.judge_client.chat.completions.create = AsyncMock(side_effect=mock_response)
    
    question = "What are the primary ethical concerns regarding the development of AGI?"
    result = await council.query(question)
    
    print(f"\nQuery: {question}")
    print(f"Strategy: {result['strategy']}")
    print("\n--- Individual Council Insights ---")
    for r in result['individual_responses']:
        print(f"[{r['model']}]: {r['content'][:60]}...")
        
    print("\n--- Final Aggregated Decision ---")
    print(result['final_answer'])

if __name__ == "__main__":
    asyncio.run(main())