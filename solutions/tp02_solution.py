from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from common.config import get_model

class Explanation(BaseModel):
    definition: str = Field(description="Définition courte")
    example: str = Field(description="Exemple concret")
    difficulty: str = Field(description="Débutant, intermédiaire ou avancé")

def run(concept="GitOps"):
    model = get_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Tu es un formateur technique. Réponds en français."),
        ("human", "Explique {concept} avec un exemple.")
    ])
    print((prompt | model).invoke({"concept": concept}).content)
    structured = model.with_structured_output(Explanation)
    print(structured.invoke(f"Explique {concept}"))

if __name__ == "__main__":
    run()
