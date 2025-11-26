from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("openai_api_key")
claude_api_key = os.getenv("claude_api_key")
hf_access_token = os.getenv("hf_access_token")

model_config = {
    "openai": {
        "model": "gpt-4o-mini",
        "api_key": openai_api_key
    },
    "claude": {
        "model": "claude-3-5-sonnet-20241022",
        "api_key": claude_api_key
    },
    "hf": {
        "model": "hf-transformers/bert-base-uncased",
        "api_key": hf_access_token
    }
}