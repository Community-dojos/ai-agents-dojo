# TP6 – Orchestrateur et agents spécialisés

- **Technologies :** LangGraph
- **Durée indicative :** 75 min
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
### Exercice 1 — Définir un State partagé avec TypedDict.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 2 — Créer un graphe avec nodes et edges.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 3 — Ajouter une condition de routage selon la demande.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 4 — Créer un agent Research spécialisé.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 5 — Créer un agent Analyst spécialisé.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 6 — Construire un supervisor qui choisit le prochain agent.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 7 — Fusionner les résultats des agents dans l'état.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 8 — Ajouter une synthèse finale et tester plusieurs parcours.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

## Validation
- Le script s'exécute sans erreur.
- Vous pouvez expliquer le rôle des composants utilisés.
- Vous avez testé au moins un cas nominal et un cas d'erreur.
- Vous avez commité votre travail.

## Correction
Une proposition de correction est disponible dans `solutions/`. Essayez d'abord sans la consulter.
