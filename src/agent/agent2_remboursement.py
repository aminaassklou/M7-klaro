"""Agent 2 - Remboursement : verifie l'eligibilite, ne decide jamais seul.

Repond aux demandes de remboursement en verifiant l'eligibilite d'une
commande selon la politique de remboursement et en citant, si necessaire,
des precedents similaires dans l'historique des tickets.

L'agent 2 ne possede que deux outils de lecture :
- verifier_eligibilite_remboursement ;
- rechercher_historique.

Il ne possede jamais l'outil initier_remboursement.
"""

from __future__ import annotations

from .commun import construire_modele_llm, executer_conversation, tracer
from .tools import ContexteOutils, outils_langchain


PROMPT_SYSTEME = """Tu es l'agent remboursement du support Klaro. Tu verifies
si une commande est eligible a un remboursement, a partir de l'outil dedie,
et tu peux citer un precedent similaire dans l'historique des tickets.

Regles imperatives :
- N'affirme AUCUN verdict d'eligibilite qui ne provienne de
  verifier_eligibilite_remboursement.
- Tu informes sur l'eligibilite ; tu ne declenches JAMAIS toi-meme de
  remboursement. La decision et l'execution restent humaines.
- Si la question ne contient pas de numero de commande, demande-le avant
  de conclure quoi que ce soit.
"""


def construire_agent(ctx: ContexteOutils):
    """Construit l'agent 2 avec uniquement ses deux outils de lecture."""
    from langchain.agents import create_agent

    outils = outils_langchain(ctx)

    outils_agent2 = [
        outils["verifier_eligibilite_remboursement"],
        outils["rechercher_historique"],
    ]

    return create_agent(
        model=construire_modele_llm(),
        tools=outils_agent2,
        system_prompt=PROMPT_SYSTEME,
    )


def repondre(
    ctx: ContexteOutils,
    question: str,
    tracer_trace: bool = True,
) -> dict:
    """Retourne une reponse et la trace des appels d'outils."""
    agent = construire_agent(ctx)
    sortie = executer_conversation(agent, question)

    res = {
        "diagnostic": {
            "question": question,
            "reponse": sortie["reponse"],
        },
        "trace": sortie["trace"],
    }

    return tracer("agent2_remboursement", res) if tracer_trace else res
