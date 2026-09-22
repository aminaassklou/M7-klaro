# Étape 1 - Évaluation de l'ancienne architecture

## Tests réalisés

Nous avons testé l'ancien bot avec plusieurs questions.

### Test 1
Question : Où en est ma commande CMD-1013 ?

Réponse :
Je n'ai pas compris votre demande, un conseiller vous recontactera.

Observation :
Le bot ne consulte pas les données de commandes.

### Test 2
Question : Je veux être remboursé pour la commande CMD-1007.

Réponse :
Pas de souci, vous serez remboursé sous peu !

Observation :
Le bot annonce un remboursement sans vérifier si la commande est éligible.

### Test 3
Question : Quel est le délai pour retourner un produit ?

Réponse :
Pas de souci, vous serez remboursé sous peu !

Observation :
Le bot voit le mot "retourner" et répond avec un remboursement, alors que la question porte seulement sur le délai de retour.

### Test 4
Question : Ma carte a été débitée deux fois, que faire ?

Réponse :
Je n'ai pas compris votre demande, un conseiller vous recontactera.

Observation :
Le bot ne comprend pas certaines demandes pourtant présentes dans les données du projet.

### Test 5
Question : Je souhaite retourner mon aspirateur, il ne me convient pas.

Réponse :
Pas de souci, vous serez remboursé sous peu !

Observation :
Le bot confond une demande de retour avec une décision de remboursement.


## 2. Nouvelle architecture

Nous allons remplacer l'ancien bot par 4 agents.

### Agent 1
Il répond aux questions générales des clients.

### Agent 2
Il vérifie si une commande peut être remboursée.

Il peut seulement lire les données.

Il ne peut pas faire le remboursement.

### Agent 3
Il aide à classer les messages des clients.

Il propose une catégorie, mais le conseiller peut la modifier.

### Agent 4
Il peut préparer une demande de remboursement.

Avant de lancer le remboursement, il doit obligatoirement attendre la validation d'un humain.

## 3. Répartition du travail

### Amina
- Agent 1
- Agent 3

### Ahmed
- Agent 2
- Agent 4
