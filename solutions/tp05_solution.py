import requests
from langchain.tools import tool
from langchain.agents import create_agent
from common.config import get_model

@tool
def get_demo_todo(todo_id: int) -> dict:
    """Récupère une tâche de démonstration JSONPlaceholder."""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}", timeout=10
    )
    response.raise_for_status()
    return response.json()

@tool
def get_weather(latitude: float, longitude: float) -> dict:
    """Récupère la température actuelle à partir de coordonnées GPS."""
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": latitude, "longitude": longitude, "current": "temperature_2m"},
        timeout=10
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    agent = create_agent(
        model=get_model(), tools=[get_demo_todo, get_weather],
        system_prompt="Utilise les API disponibles et précise les limites des données."
    )
    result = agent.invoke({"messages": [{"role": "user", "content":
        "Donne la tâche de démonstration numéro 1."}]})
    print(result["messages"][-1].content)
