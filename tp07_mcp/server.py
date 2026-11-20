"""Serveur MCP local de démonstration : données fictives uniquement."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dojo-hr-demo")

@mcp.tool()
def get_training_catalog(topic: str) -> str:
    """Recherche une formation fictive par thème."""
    catalog = {
        "kubernetes": "Kubernetes Fundamentals — 2 jours — prérequis : bases Linux et conteneurs.",
        "python": "Python Essentials — 2 jours — prérequis : aucun."
    }
    key = topic.lower()
    return catalog.get(key, "Aucune formation trouvée dans le catalogue fictif.")

@mcp.tool()
def get_employee_profile(employee_id: int) -> str:
    """Retourne un profil fictif. Ne contient aucune donnée réelle."""
    profiles = {1001: "Collaborateur fictif : rôle DevOps, compétences Linux et Git."}
    return profiles.get(employee_id, "Profil fictif introuvable.")

if __name__ == "__main__":
    mcp.run(transport="stdio")
