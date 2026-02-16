import asyncio
import logging
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI

from .config import get_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Response:
    def __init__(self, model: str, content: str, raw: Any = None):
        self.model = model
        self.content = content
        self.raw = raw


class CouncilMember:
    def __init__(self, model_name: str, api_key: str, base_url: str):
        self.model_name = model_name
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def get_response(
        self, messages: List[Dict[str, str]], timeout: float
    ) -> Optional[Response]:
        try:
            response = await asyncio.wait_for(
                self.client.chat.completions.create(
                    model=self.model_name, messages=messages, timeout=timeout
                ),
                timeout=timeout + 5,
            )
            content = response.choices[0].message.content
            print()
            return Response(model=self.model_name, content=content, raw=response)
        except Exception as e:
            logger.error(f"Error getting response from {self.model_name}: {e}")
            return None


class Council:
    def __init__(self, config=None):
        self.config = config or get_config()
        self.members = [
            CouncilMember(m, self.config.openrouter_api_key, self.config.api_base)
            for m in self.config.council_models
        ]
        self.judge_client = AsyncOpenAI(
            api_key=self.config.openrouter_api_key, base_url=self.config.api_base
        )

    async def query(
        self, prompt: str, system_prompt: str = "You are a helpful assistant."
    ) -> Dict[str, Any]:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        tasks = [
            member.get_response(messages, self.config.timeout)
            for member in self.members
        ]
        responses = await asyncio.gather(*tasks)

        valid_responses = [r for r in responses if r is not None]

        if not valid_responses:
            return {"error": "No valid responses received from council members."}

        if self.config.council_strategy == "synthesis":
            final_answer = await self._synthesize(prompt, valid_responses)
        elif self.config.council_strategy == "voting":
            final_answer = self._vote(valid_responses)
        else:
            final_answer = valid_responses[0].content  # Fallback

        return {
            "final_answer": final_answer,
            "individual_responses": [
                {"model": r.model, "content": r.content} for r in valid_responses
            ],
            "strategy": self.config.council_strategy,
        }

    async def _synthesize(self, original_prompt: str, responses: List[Response]) -> str:
        synthesis_prompt = f"Original Query: {original_prompt}\n\n"
        synthesis_prompt += "Different AI models provided the following responses:\n\n"
        for i, r in enumerate(responses):
            synthesis_prompt += f"--- Model {i+1} ({r.model}) ---\n{r.content}\n\n"

        synthesis_prompt += (
            "Based on the responses above, provide a single, comprehensive, and accurate final answer. "
            "Resolve any contradictions and combine the best insights from all models."
        )

        try:
            # Using the first model in the list as the synthesis judge or gpt-4o if available
            judge_model = self.config.council_models[0]
            resp = await self.judge_client.chat.completions.create(
                model=judge_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a lead orchestrator who synthesizes multiple perspectives into a consensus.",
                    },
                    {"role": "user", "content": synthesis_prompt},
                ],
            )
            return resp.choices[0].message.content
        except Exception as e:
            logger.error(f"Synthesis failed: {e}")
            return responses[0].content  # Fallback to first valid response

    def _vote(self, responses: List[Response]) -> str:
        from collections import Counter

        contents = [r.content.strip() for r in responses]
        counts = Counter(contents)
        most_common = counts.most_common(1)[0][0]
        return most_common
