# TP4 – Premier agent, outils et mémoire

- **Technologies :** LangChain + LangGraph
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
### Exercice 1 — Créer un agent avec create_agent.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 2 — Observer le cycle décision, tool call et réponse.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 3 — Créer un outil Python simple avec @tool.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 4 — Ajouter un outil de calcul arithmétique sécurisé.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 5 — Enregistrer plusieurs outils dans le même agent.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 6 — Conserver l'état d'une conversation avec un thread_id et un checkpointer.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 7 — Tester la persistance de l'état entre deux exécutions.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 8 — Créer un assistant qui choisit lui-même quand appeler un outil.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

## Validation
- Le script s'exécute sans erreur.
- Vous pouvez expliquer le rôle des composants utilisés.
- Vous avez testé au moins un cas nominal et un cas d'erreur.
- Vous avez commité votre travail.

## Correction
Une proposition de correction est disponible dans `solutions/`. Essayez d'abord sans la consulter.
