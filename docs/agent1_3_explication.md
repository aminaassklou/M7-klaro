Agent 1 : renseignement général

Le client pose une question.

L’Agent 1 utilise seulement 2 outils :
- chercher_faq : pour les questions générales
- consulter_commande : pour voir le statut d’une commande

Ces outils sont définis dans tools.py.

Le modèle Mistral est récupéré avec construire_modele_llm() dans commun.py.

Ensuite create_agent() crée l’agent avec :
- le modèle Mistral
- les 2 outils autorisés
- le prompt système

Exemple :
Question : "Quel est le délai de livraison standard ?"
→ l’agent utilise chercher_faq()
→ il lit la FAQ
→ il répond avec l’information trouvée

Question : "Où en est ma commande CMD-1013 ?"
→ l’agent utilise consulter_commande()
→ il lit les données de commandes.csv
→ il répond avec le statut de la commande

La trace est aussi récupérée avec les fonctions déjà présentes dans commun.py.


## Agent 3 : pré-triage des messages

L’Agent 3 sert à classer les messages clients.

Il utilise le modèle Mistral avec `construire_modele_llm()` dans `commun.py`.

La fonction `classifier_message()` reçoit le texte du client et demande au modèle de retourner :

- une catégorie ;
- un niveau de confiance ;
- une justification.

La réponse est demandée en JSON puis vérifiée avec `_parser_reponse_json()`.

Exemple :

Message : "Je n’ai toujours pas reçu mon colis"

→ l’agent analyse le message  
→ il propose une catégorie  
→ il donne un niveau de confiance  
→ il ajoute une justification

Ensuite, le conseiller peut valider ou corriger la proposition.

