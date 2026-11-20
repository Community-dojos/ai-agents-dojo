from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict, total=False):
    question: str
    research: str
    analysis: str
    answer: str

def research(state: State):
    return {"research": f"Éléments à rechercher sur : {state['question']}"}

def analyze(state: State):
    return {"analysis": f"Analyse basée sur : {state.get('research', '')}"}

def synthesize(state: State):
    return {"answer": state.get("research", "") + "\n" + state.get("analysis", "")}

def build_graph():
    builder = StateGraph(State)
    builder.add_node("research", research)
    builder.add_node("analyze", analyze)
    builder.add_node("synthesize", synthesize)
    builder.add_edge(START, "research")
    builder.add_edge("research", "analyze")
    builder.add_edge("analyze", "synthesize")
    builder.add_edge("synthesize", END)
    return builder.compile()

if __name__ == "__main__":
    print(build_graph().invoke({"question": "Tendances DevOps"}))
