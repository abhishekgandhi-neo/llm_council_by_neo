import asyncio
import os
from unittest.mock import AsyncMock, MagicMock
from llm_council import Council, CouncilConfig

async def mock_chat_completion(*args, **kwargs):
    model = kwargs.get('model', 'unknown')
    messages = kwargs.get('messages', [])
    
    mock_resp = MagicMock()
    mock_choice = MagicMock()
    mock_message = MagicMock()
    
    # Check if this is the synthesis call
    is_synthesis = any("synthesize" in str(m.get('content', '')).lower() for m in messages)
    
    if is_synthesis:
        mock_message.content = "Synthesized answer summarizing all council insights."
    else:
        mock_message.content = f"Response from model {model}"
    
    mock_choice.message = mock_message
    mock_resp.choices = [mock_choice]
    return mock_resp

async def test_council_orchestration():
    print("--- Testing Council Orchestration with Mocks ---")
    
    # Initialize config with explicit values to bypass .env parsing issues
    mock_config = CouncilConfig(
        openrouter_api_key="sk-or-mock-key",
        council_models=["gpt-4", "claude-3", "gemini-pro"],
        council_strategy="synthesis"
    )
    
    council = Council(config=mock_config)
    
    # Mock individual member clients
    for member in council.members:
        member.client.chat.completions.create = AsyncMock(side_effect=mock_chat_completion)
    
    # Mock judge client
    council.judge_client.chat.completions.create = AsyncMock(side_effect=mock_chat_completion)
    
    result = await council.query("Explain quantum entanglement.")
    
    print(f"Strategy: {result['strategy']}")
    print(f"Final Answer: {result['final_answer']}")
    print(f"Models participating: {len(result['individual_responses'])}")
    
    assert len(result['individual_responses']) == 3
    assert "Synthesized" in result['final_answer']
    print("\n--- Mock Test Passed! ---")

if __name__ == "__main__":
    asyncio.run(test_council_orchestration())