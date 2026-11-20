"""TP3 - RAG. Le corpus fictif est dans data/documents/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "data" / "documents"

def exercise_1():
    # TODO : charger les .md en Document LangChain.
    raise NotImplementedError

def exercise_2():
    # TODO : découper les documents en chunks.
    raise NotImplementedError

def exercise_3():
    # TODO : initialiser OpenAIEmbeddings.
    raise NotImplementedError

def exercise_4():
    # TODO : indexer les chunks dans Chroma.
    raise NotImplementedError

def exercise_5():
    # TODO : faire une recherche top-k.
    raise NotImplementedError

def exercise_6():
    # TODO : construire une réponse en injectant les passages récupérés.
    raise NotImplementedError

def exercise_7():
    # TODO : retourner la réponse et les sources (metadata/source).
    raise NotImplementedError

def exercise_8():
    # TODO : tester une question sans réponse dans le corpus.
    raise NotImplementedError

if __name__ == "__main__":
    print(f"Documents de départ : {list(DOCS.glob('*.md'))}")
    print("Complétez les TODO du TP3.")
