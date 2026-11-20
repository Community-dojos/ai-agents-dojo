from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from common.config import get_model
from common.safe_math import safe_calculate

@tool
def calculate(expression: str) -> str:
    """Calcule une expression arithmétique simple et sûre."""
    return str(safe_calculate(expression))

@tool
def explain_devops(topic: str) -> str:
    """Retourne un rappel pédagogique sur un sujet DevOps."""
    return f"Prépare une explication pédagogique sur : {topic}"

def build_agent():
    return create_agent(
        model=get_model(),
        tools=[calculate, explain_devops],
        system_prompt="Tu es un assistant technique. Utilise les outils quand ils sont utiles.",
        checkpointer=InMemorySaver()
    )

if __name__ == "__main__":
    agent = build_agent()
    config = {"configurable": {"thread_id": "participant-demo"}}
    result = agent.invoke({"messages": [{"role": "user", "content": "Calcule 125 * 18"}]}, config)
    print(result["messages"][-1].content)
