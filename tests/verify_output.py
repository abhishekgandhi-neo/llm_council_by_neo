import os

mock_content = """# LLM Council Response
## Original Query
Mock Query?
## Aggregated Council Answer
Mock Answer
## Individual Model Contributions
### Model 1: mock/model
Mock Content
"""

output_path = "council_answer.md"
# Simulate the final step of main.py
with open(output_path, "w", encoding="utf-8") as f:
    f.write(mock_content)

if os.path.exists(output_path):
    print(f"SUCCESS: {output_path} generated.")
    with open(output_path, "r") as f:
        print("Content Preview:")
        print(f.read()[:50] + "...")
else:
    print("FAILED: Output file not found.")