# LLM Council

A modular system to orchestrate multiple Large Language Models (LLMs) via OpenRouter for enhanced reasoning and consensus.

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**:
   Copy `.env.example` to `.env` and fill in your details:
   ```bash
   cp .env.example .env
   ```

3. **Usage**:
   Run the main entry point to query the council and generate `council_answer.md`:
   ```bash
   python main.py
   ```

## Key Features
- **Parallel Orchestration**: Queries multiple models simultaneously via OpenRouter.
- **Consensus Strategies**: Supports `synthesis` (lead model aggregates insights) and `voting`.
- **OpenAI Compatibility**: Leverages standard OpenAI-compatible implementation.
- **Configurable Output**: Results are saved to a markdown file for easy review.

## Environment Variables
Defined in `.env`:
- `OPENROUTER_API_KEY`: Your API key for model access.
- `COUNCIL_MODELS`: Comma-separated list of OpenRouter models.
- `COUNCIL_STRATEGY`: Strategy for aggregating answers (`synthesis` or `voting`).
- `COUNCIL_OUTPUT_FILE`: Markdown file path for saving the council's answer.

## Output Structure
Running `main.py` produces a markdown file containing:
1. The user's original query.
2. The synthesized final answer.
3. Detailed individual responses from each council member.