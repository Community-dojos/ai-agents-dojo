"""Configuration commune au dojo."""
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL") or None

def get_model():
    """Retourne un ChatModel LangChain. Nécessite une clé API valide."""
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY absente. Copiez .env.example vers .env et renseignez la clé."
        )
    from langchain.chat_models import init_chat_model
    kwargs = {"model": MODEL_NAME, "model_provider": "openai", "api_key": OPENAI_API_KEY}
    if OPENAI_BASE_URL:
        kwargs["base_url"] = OPENAI_BASE_URL
    return init_chat_model(**kwargs)
