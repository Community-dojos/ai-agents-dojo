# Suivi participant – AI Agents Dojo

Cochez les exercices terminés.

## TP1 – Premier assistant IA
- [ ] Exercice 1 — Premier appel LLM : envoyer un prompt et afficher la réponse.
- [ ] Exercice 2 — Messages : tester les rôles system, user et assistant.
- [ ] Exercice 3 — Paramètres : modifier le modèle et ses paramètres disponibles.
- [ ] Exercice 4 — Assistant à rôle : définir une personnalité et des limites.
- [ ] Exercice 5 — Historique : conserver plusieurs tours de conversation.
- [ ] Exercice 6 — Streaming : afficher les tokens au fur et à mesure.
- [ ] Exercice 7 — Gestion d'erreurs : traiter clé absente, timeout et erreur API.
- [ ] Exercice 8 — Mini-chat : créer une boucle CLI interactive avec commande de sortie.

## TP2 – Modèles de prompts
- [ ] Exercice 1 — Comparer un prompt vague et un prompt contextualisé.
- [ ] Exercice 2 — Structurer un prompt avec rôle, contexte, tâche et contraintes.
- [ ] Exercice 3 — Créer un PromptTemplate avec variables.
- [ ] Exercice 4 — Créer un ChatPromptTemplate multi-messages.
- [ ] Exercice 5 — Ajouter des exemples few-shot.
- [ ] Exercice 6 — Imposer une sortie structurée avec Pydantic.
- [ ] Exercice 7 — Chaîner prompt, modèle et parser.
- [ ] Exercice 8 — Comparer deux variantes de prompt sur un petit jeu de questions.

## TP3 – RAG documentaire
- [ ] Exercice 1 — Charger les fichiers Markdown du dossier data/documents.
- [ ] Exercice 2 — Découper les documents avec RecursiveCharacterTextSplitter.
- [ ] Exercice 3 — Créer les embeddings avec le modèle choisi.
- [ ] Exercice 4 — Indexer les chunks dans Chroma.
- [ ] Exercice 5 — Effectuer une recherche sémantique top-k.
- [ ] Exercice 6 — Construire une réponse basée uniquement sur le contexte récupéré.
- [ ] Exercice 7 — Afficher les sources utilisées dans la réponse.
- [ ] Exercice 8 — Tester une question absente du corpus et gérer l'absence de preuve.

## TP4 – Premier agent, outils et mémoire
- [ ] Exercice 1 — Créer un agent avec create_agent.
- [ ] Exercice 2 — Observer le cycle décision, tool call et réponse.
- [ ] Exercice 3 — Créer un outil Python simple avec @tool.
- [ ] Exercice 4 — Ajouter un outil de calcul arithmétique sécurisé.
- [ ] Exercice 5 — Enregistrer plusieurs outils dans le même agent.
- [ ] Exercice 6 — Conserver l'état d'une conversation avec un thread_id et un checkpointer.
- [ ] Exercice 7 — Tester la persistance de l'état entre deux exécutions.
- [ ] Exercice 8 — Créer un assistant qui choisit lui-même quand appeler un outil.

## TP5 – Outils appelant des API Web
- [ ] Exercice 1 — Appeler une API publique avec requests et un timeout.
- [ ] Exercice 2 — Lire et valider une réponse JSON.
- [ ] Exercice 3 — Créer un tool météo Open-Meteo à partir de coordonnées.
- [ ] Exercice 4 — Créer un tool de consultation de données JSONPlaceholder.
- [ ] Exercice 5 — Valider les paramètres et valeurs de retour.
- [ ] Exercice 6 — Gérer HTTP errors, timeout et indisponibilité réseau.
- [ ] Exercice 7 — Donner plusieurs outils API à un agent.
- [ ] Exercice 8 — Créer un assistant qui combine les résultats de deux API.

## TP6 – Orchestrateur et agents spécialisés
- [ ] Exercice 1 — Définir un State partagé avec TypedDict.
- [ ] Exercice 2 — Créer un graphe avec nodes et edges.
- [ ] Exercice 3 — Ajouter une condition de routage selon la demande.
- [ ] Exercice 4 — Créer un agent Research spécialisé.
- [ ] Exercice 5 — Créer un agent Analyst spécialisé.
- [ ] Exercice 6 — Construire un supervisor qui choisit le prochain agent.
- [ ] Exercice 7 — Fusionner les résultats des agents dans l'état.
- [ ] Exercice 8 — Ajouter une synthèse finale et tester plusieurs parcours.

## TP7 – Model Context Protocol
- [ ] Exercice 1 — Identifier client, serveur, tools, resources et prompts MCP.
- [ ] Exercice 2 — Démarrer un serveur MCP local en transport stdio.
- [ ] Exercice 3 — Exposer une fonction Python comme tool MCP.
- [ ] Exercice 4 — Découvrir les outils depuis un client MCP.
- [ ] Exercice 5 — Connecter les outils MCP à LangChain via langchain-mcp-adapters.
- [ ] Exercice 6 — Appeler un outil MCP depuis un agent.
- [ ] Exercice 7 — Connecter deux serveurs ou deux ensembles d'outils.
- [ ] Exercice 8 — Créer un agent qui choisit un outil MCP selon la demande.

## TP8 – Guardrails, sécurité et évaluation
- [ ] Exercice 1 — Valider les entrées avec Pydantic et des limites de taille.
- [ ] Exercice 2 — Définir des demandes hors périmètre et leur traitement.
- [ ] Exercice 3 — Tester des tentatives de prompt injection sur le corpus fictif.
- [ ] Exercice 4 — Valider la structure des sorties avec un schéma Pydantic.
- [ ] Exercice 5 — Appliquer une liste d'autorisation sur les outils disponibles.
- [ ] Exercice 6 — Ajouter une étape d'approbation humaine avant une action sensible.
- [ ] Exercice 7 — Tracer et évaluer les cas de test avec LangSmith (facultatif).
- [ ] Exercice 8 — Assembler les contrôles dans le mini-projet final.
