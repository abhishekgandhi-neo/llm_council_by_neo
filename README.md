# Neo LLM Council: Decision Intelligence via Orchestrated Consensus

Made with [Neo](https://neo.com)

The **Neo LLM Council** is a high-impact orchestration system designed to transform raw AI outputs into reliable decision intelligence. By convening a digital "council" of diverse Large Language Models (LLMs), it eliminates the bias and hallucinations inherent in single-model responses, delivering synthesized, high-confidence results for complex real-world reasoning.

## Why Neo LLM Council?

In standard AI environments, organizations often struggle with "model plumbing"—the manual work of connecting multiple APIs and then trying to make sense of conflicting data. **Neo LLM Council** changes this dynamic from technical friction to strategic advantage.

### Built for Higher-Impact Outcomes

- **Seamless Orchestration vs. Manual Plumbing**: Instead of complex custom scripts, Neo LLM Council provides a unified interface to OpenRouter, allowing you to deploy a multi-model strategy in minutes rather than weeks.
- **High-Impact Consensus over Simple Averaging**: Our system doesn't just average outputs. It uses advanced synthesis strategies to cross-examine viewpoints, surfacing the most robust and accurate insights for critical decision-making.
- **Resilient Decision Making**: By leveraging the Neo ecosystem, you gain a system that handles API instability and model variance gracefully, ensuring your business continuity isn't dependent on a single model provider.
- **Verified Transparency**: Every decision made by the Council is traceable. You can see exactly how each member (model) contributed to the final synthesis, providing an audit trail for AI-assisted decisions.

## Overview

The Neo LLM Council acts as your organization’s digital roundtable. It brings together the world's most advanced models to debate, verify, and resolve complex queries. The result is a robust, balanced final answer that far exceeds the capability of any individual LLM.

## Usage with Neo

The Neo LLM Council is optimized for the **[Neo VSCode Extension](https://neo.com)**, providing a frictionless deployment experience that bridges the gap between development and production.

### Steps to Run:

1. **Open in VSCode**: Open the `llm_council` folder in VSCode where the Neo extension is installed.
2. **Environment Setup**:
   - Click on the Neo extension icon in the sidebar.
   - Use Neo to automate the setup: "Neo, set up the virtual environment and install requirements."
   - Create your `.env` file (Neo can help you populate the `OPENROUTER_API_KEY`).
3. **Run the Application**:
   - In the VSCode terminal, run `python main.py`.
   - Alternatively, ask Neo: "Run the LLM Council with the prompt 'Explain quantum entanglement'."
4. **View Results**:
   - Once completed, open `council_answer.md` in the VSCode editor to see the aggregated response.

## Strategic Use Cases

- **Strategic Decision Support**: Cross-validate high-stakes business strategies across multiple reasoning models.
- **High-Fidelity Research**: Aggregate diverse perspectives to generate comprehensive, unbiased technical and market summaries.
- **AI Governance & Safety**: Implement model cross-checking to detect hallucinations and ensure output compliance.
- **Automated Benchmarking**: Instantly compare how different frontier models interpret the same complex logic.

## Project Structure

```
llm_council/
│
├── main.py                 # Entry point
├── llm_council/
│   ├── config.py           # Environment configuration
│   └── engine.py           # Model querying layer
│
│
├── .env.example            # Example environment variables
├── requirements.txt        # Dependencies
└── README.md
```

## Quick Start (Manual)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
copy .env.example .env
```

Edit `.env` with your `OPENROUTER_API_KEY`.

### 3. Run the Council

```bash
python main.py
```

## Consensus Strategies

### Synthesis (default)

A lead model combines all responses into a single comprehensive answer. Best for research and analysis.

### Voting

Selects the most common response among models. Best for objective questions.

## License

MIT License

Made with [Neo](https://neo.com)
