from langchain_core.messages import SystemMessage, HumanMessage
from common.config import get_model
from common.prompts import BASE_SYSTEM_PROMPT

def run():
    model = get_model()
    messages = [SystemMessage(content=BASE_SYSTEM_PROMPT)]
    while True:
        question = input("Vous (quit pour sortir) : ").strip()
        if question.lower() == "quit":
            break
        messages.append(HumanMessage(content=question))
        try:
            answer = model.invoke(messages)
            messages.append(answer)
            print("Assistant :", answer.content)
        except Exception as exc:
            print(f"Erreur pendant l'appel au modèle : {exc}")

if __name__ == "__main__":
    run()
