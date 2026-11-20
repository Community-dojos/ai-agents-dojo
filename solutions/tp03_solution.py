from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from common.config import get_model

ROOT = Path(__file__).resolve().parents[1]

def build_rag():
    docs = []
    for path in (ROOT / "data/documents").glob("*.md"):
        docs.append(Document(page_content=path.read_text(encoding="utf-8"),
                            metadata={"source": path.name}))
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=80
    ).split_documents(docs)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    store = Chroma.from_documents(
        chunks, embeddings, persist_directory=str(ROOT / ".chroma")
    )
    return store.as_retriever(search_kwargs={"k": 3})

def ask(question):
    retriever = build_rag()
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)
    prompt = (
        "Réponds uniquement à partir du contexte. "
        "Si l'information manque, dis-le. Cite les noms des sources.\n\n"
        f"CONTEXTE:\n{context}\n\nQUESTION: {question}"
    )
    answer = get_model().invoke(prompt)
    return answer.content, sorted({d.metadata.get("source", "inconnu") for d in docs})

if __name__ == "__main__":
    response, sources = ask("Comment demander un accès VPN ?")
    print(response, "\nSources :", sources)
