# TP8 – Guardrails, sécurité et évaluation

- **Technologies :** LangChain + LangGraph + LangSmith
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
### Exercice 1 — Valider les entrées avec Pydantic et des limites de taille.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 2 — Définir des demandes hors périmètre et leur traitement.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 3 — Tester des tentatives de prompt injection sur le corpus fictif.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 4 — Valider la structure des sorties avec un schéma Pydantic.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 5 — Appliquer une liste d'autorisation sur les outils disponibles.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 6 — Ajouter une étape d'approbation humaine avant une action sensible.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 7 — Tracer et évaluer les cas de test avec LangSmith (facultatif).

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 8 — Assembler les contrôles dans le mini-projet final.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

## Validation
- Le script s'exécute sans erreur.
- Vous pouvez expliquer le rôle des composants utilisés.
- Vous avez testé au moins un cas nominal et un cas d'erreur.
- Vous avez commité votre travail.

## Correction
Une proposition de correction est disponible dans `solutions/`. Essayez d'abord sans la consulter.
