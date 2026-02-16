import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
models = os.getenv("COUNCIL_MODELS", "").split(",")

def test_model(model_id):
    print(f"Testing model: {model_id}...")
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": "Say hello"}],
                "max_tokens": 10
            },
            timeout=10
        )
        if response.status_code == 200:
            print(f"✅ Success: {model_id}")
            return True
        else:
            print(f"❌ Failed: {model_id} - Status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error testing {model_id}: {str(e)}")
        return False

if __name__ == "__main__":
    results = [test_model(m.strip()) for m in models if m.strip()]
    if any(results):
        print("\nConclusion: Connectivity is working for some/all models.")
    else:
        print("\nConclusion: All models failed. Check API Key or OpenRouter status.")