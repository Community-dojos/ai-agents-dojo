import importlib.util
import os
from dotenv import load_dotenv

load_dotenv()
modules = ["langchain", "langchain_openai", "langgraph", "mcp", "langsmith", "streamlit"]
print("Vérification des dépendances :")
for name in modules:
    print(f"  {'OK' if importlib.util.find_spec(name) else 'MANQUANT'}  {name}")
print(f"\nOPENAI_API_KEY : {'configurée' if os.getenv('OPENAI_API_KEY') else 'absente (les exercices sans LLM restent accessibles)'}")
print(f"LANGSMITH_API_KEY : {'configurée' if os.getenv('LANGSMITH_API_KEY') else 'absente (facultatif)'}")
