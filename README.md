# AI Agents Developer Dojo

Parcours pratique en 8 TP (64 exercices) pour construire progressivement un assistant IA avec Python, LangChain, LangGraph, LangSmith et MCP.

> **Mode participant :** forkez ce dépôt, ouvrez-le dans GitHub Codespaces, configurez vos secrets, puis suivez les TP dans l'ordre. Les solutions sont volontairement séparées dans `solutions/` : ne les consultez qu'après avoir essayé.

## Objectif final

Construire un assistant d'entreprise capable de :
- répondre à partir d'une base documentaire (RAG) ;
- appeler des outils Python et des API REST ;
- déléguer des tâches à des agents spécialisés avec LangGraph ;
- utiliser des outils exposés via MCP ;
- appliquer des contrôles de sécurité et une validation humaine ;
- tracer et évaluer les exécutions avec LangSmith.

## Prérequis

- Bases de Python : variables, fonctions, listes/dictionnaires, exceptions.
- Bases de Git : clone/fork, commit, push.
- Un compte GitHub avec Codespaces activé.
- Une clé API de modèle compatible avec `langchain-openai` (OpenAI ou endpoint compatible).
- Facultatif : un compte LangSmith. Le dojo fonctionne sans tracing LangSmith.

Les exercices utilisent des données fictives. N'ajoutez aucune donnée réelle ou confidentielle.

## Démarrage rapide avec GitHub Codespaces

1. Cliquez sur **Use this template** ou faites un fork du dépôt.
2. Ouvrez **Code → Codespaces → Create codespace on main**.
3. Dans Codespaces, ouvrez `Terminal → New Terminal`.
4. Copiez `.env.example` vers `.env` :

   ```bash
   cp .env.example .env
   ```

5. Renseignez les variables nécessaires dans `.env` (ne commitez jamais ce fichier).
6. Installez les dépendances si le post-create ne l'a pas déjà fait :

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Vérifiez l'environnement :

   ```bash
   python scripts/check_setup.py
   ```

8. Lancez le TP1 :

   ```bash
   python -m tp01_first_assistant.starter
   ```

> Les secrets GitHub Codespaces peuvent aussi être configurés dans GitHub → Settings → Secrets and variables → Codespaces. Après ajout/modification, recréez ou redémarrez le Codespace pour que les variables soient disponibles.

## Configuration

Variables reconnues :

| Variable | Obligatoire | Rôle |
|---|---:|---|
| `OPENAI_API_KEY` | Pour les appels LLM | Clé API du fournisseur |
| `OPENAI_BASE_URL` | Non | URL d'un endpoint compatible OpenAI |
| `MODEL_NAME` | Non | Modèle, défaut `gpt-4o-mini` |
| `LANGSMITH_API_KEY` | Non | Clé LangSmith |
| `LANGSMITH_TRACING` | Non | Active le tracing, défaut `false` |
| `LANGSMITH_PROJECT` | Non | Projet LangSmith |

Pour un endpoint compatible OpenAI, renseignez `OPENAI_BASE_URL` selon les indications de votre fournisseur.

## Parcours

| TP | Sujet | Durée indicative | Dossier |
|---|---|---:|---|
| 1 | Premier assistant | 45 min | `tp01_first_assistant/` |
| 2 | Modèles de prompts | 45 min | `tp02_prompt_engineering/` |
| 3 | RAG documentaire | 60 min | `tp03_rag/` |
| 4 | Premier agent, tools et mémoire | 60 min | `tp04_first_agent/` |
| 5 | Outils appelant des API Web | 60 min | `tp05_api_tools/` |
| 6 | Orchestrateur et agents spécialisés | 75 min | `tp06_multi_agents/` |
| 7 | MCP | 60 min | `tp07_mcp/` |
| 8 | Guardrails et évaluation | 75 min | `tp08_guardrails/` |

Chaque TP contient :
- `README.md` : consignes et 8 exercices ;
- `starter.py` : squelette à compléter ;
- `solution.py` : proposition de correction ;
- `tests/` : tests locaux lorsque cela est pertinent.

## Règles de travail

1. Faites les exercices dans l'ordre.
2. Commencez par `starter.py`, pas par `solution.py`.
3. Faites un commit à la fin de chaque TP.
4. Vérifiez les traces et les erreurs, ne vous contentez pas d'une réponse qui « semble bonne ».
5. Les appels aux LLM et certaines API peuvent être payants : surveillez vos quotas.
6. Les tools peuvent exécuter des actions. N'exposez jamais un outil dangereux à un agent sans contrôle.

## Commandes utiles

```bash
# Tests
pytest -q

# Lancer l'application finale
streamlit run app.py --server.address 0.0.0.0

# Lancer le serveur MCP (stdio)
python -m tp07_mcp.server
```

## Architecture du dépôt

```text
.
├── .devcontainer/       # Environnement GitHub Codespaces
├── common/              # Configuration et utilitaires partagés
├── data/documents/      # Corpus fictif du RAG
├── tp01...tp08/         # Les 8 ateliers
├── solutions/           # Corrections de référence
├── tests/               # Tests transverses
├── app.py               # Démonstrateur final Streamlit
├── requirements.txt
└── .env.example
```

## Limites pédagogiques et sécurité

- Le dojo est un environnement d'apprentissage, pas une application prête pour la production.
- Le tool de calcul utilise une évaluation arithmétique restreinte ; n'utilisez jamais `eval()` sur une entrée utilisateur.
- Les données RH sont fictives.
- Les contrôles anti-injection sont illustratifs et ne garantissent pas une protection complète.
- Les opérations d'écriture ou d'envoi doivent être protégées par une validation humaine et des autorisations côté serveur.
