# TP5 – Outils appelant des API Web

- **Technologies :** LangChain + REST
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
### Exercice 1 — Appeler une API publique avec requests et un timeout.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 2 — Lire et valider une réponse JSON.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 3 — Créer un tool météo Open-Meteo à partir de coordonnées.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 4 — Créer un tool de consultation de données JSONPlaceholder.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 5 — Valider les paramètres et valeurs de retour.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 6 — Gérer HTTP errors, timeout et indisponibilité réseau.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 7 — Donner plusieurs outils API à un agent.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

### Exercice 8 — Créer un assistant qui combine les résultats de deux API.

**À faire :** implémentez la fonctionnalité dans `starter.py`, exécutez le script et notez le résultat attendu.

## Validation
- Le script s'exécute sans erreur.
- Vous pouvez expliquer le rôle des composants utilisés.
- Vous avez testé au moins un cas nominal et un cas d'erreur.
- Vous avez commité votre travail.

## Correction
Une proposition de correction est disponible dans `solutions/`. Essayez d'abord sans la consulter.
