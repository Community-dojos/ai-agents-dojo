# Guide formateur

## Avant la session
- Tester la création d'un Codespace depuis un compte participant.
- Vérifier que les secrets API sont disponibles.
- Vérifier les quotas et plafonds de dépenses du fournisseur.
- Exécuter `python scripts/check_setup.py` et `pytest -q`.
- Préparer un jeu de questions de test stable.

## Animation
- 10 minutes : concept et démonstration.
- 25–35 minutes : manipulation.
- 10 minutes : challenge.
- 5 minutes : restitution.

## Conseils
- Ne pas distribuer les solutions au début.
- Faire commiter chaque étape.
- Utiliser les mêmes données fictives pour RAG, API, MCP et projet final.
- Demander une trace LangSmith en preuve de compréhension, si LangSmith est configuré.
- Prévoir une alternative sans LangSmith pour les participants sans compte.

## Critères de validation
1. Le participant peut expliquer l'architecture.
2. Le code s'exécute dans Codespaces.
3. Les erreurs et limites sont prises en compte.
4. Les secrets ne sont pas versionnés.
5. Les actions sensibles sont soumises à autorisation.
