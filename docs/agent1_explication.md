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