# TP7 – Model Context Protocol

- **Technologies :** MCP + LangChain
- **Durée indicative :** 60 min
- **Mode :** participant, commencer par `starter.py`.

## Objectifs
À la fin de ce TP, vous serez capable de mettre en œuvre les concepts présentés et d'expliquer les choix réalisés.

## Préparation
Depuis la racine du dépôt :

```bash
python -m pip install -r requirements.txt
cp .env.example .env
```

Renseignez `OPENAI_API_KEY` dans `.env` pour les exercices qui appellent un LLM. LangSmith est facultatif.

## Les 8 exercices
### Exercice 1 — Identifier client, serveur, tools, resources et prompts MCP.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 2 — Démarrer un serveur MCP local en transport stdio.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 3 — Exposer une fonction Python comme tool MCP.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 4 — Découvrir les outils depuis un client MCP.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 5 — Connecter les outils MCP à LangChain via langchain-mcp-adapters.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 6 — Appeler un outil MCP depuis un agent.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 7 — Connecter deux serveurs ou deux ensembles d'outils.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 8 — Créer un agent qui choisit un outil MCP selon la demande.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

## Validation
- Le script s'exécute sans erreur.
- Vous pouvez expliquer le rôle des composants utilisés.
- Vous avez testé au moins un cas nominal et un cas d'erreur.
- Vous avez commité votre travail.

## Correction
Une proposition de correction est disponible dans `solutions/`. Essayez d'abord sans la consulter.
