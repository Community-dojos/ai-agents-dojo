from pydantic import BaseModel, Field, ValidationError
from typing import Literal

class UserRequest(BaseModel):
    question: str = Field(min_length=5, max_length=1000)

class FinalAnswer(BaseModel):
    answer: str
    sources: list[str] = []
    status: Literal["answered", "insufficient_context", "refused"]

ALLOWED_TOOLS = {"get_training_catalog", "get_employee_profile"}

def validate_request(raw: str):
    return UserRequest(question=raw)

def tool_is_allowed(name: str) -> bool:
    return name in ALLOWED_TOOLS

def require_human_approval(action_description: str) -> bool:
    print(f"Action proposée : {action_description}")
    return input("Autoriser cette action ? (oui/non) : ").strip().lower() == "oui"

def main():
    try:
        request = validate_request("Comment trouver une formation Kubernetes ?")
        print("Entrée validée :", request.question)
        print("Tool autorisé :", tool_is_allowed("get_training_catalog"))
        print("Tool interdit :", tool_is_allowed("delete_employee"))
        print("Approbation :", require_human_approval("Envoyer une demande d'inscription"))
    except ValidationError as exc:
        print("Entrée invalide :", exc)

if __name__ == "__main__":
    main()
