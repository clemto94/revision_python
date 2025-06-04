"""
Objectif : Implémenter reorder (text, indices) qui prend 2 paramètres
 – text : une chaîne de caractères de longueur N
 — indices : une liste de N entiers, allant de 1 à N (pas de zéro), sans doublons.

La fonction doit retourner une chaîne contenant tous les caractères de 'text', 
mais réordonnés selon les positions indiquées dans 'indices'.
Par exemple, si le premier indice est 4, le quatrième caractère de 'text' 
sera placé en première position dans la chaîne retournée.
"""

from json import dumps, loads
import sys
from typing import List


def reorder(text: str, indices: List[int]) -> str:
    """
    Réordonne une chaîne de caractères selon une liste d'indices donnée.

    Args:
        text (str) : La chaîne de caractères à réordonner
        indices (List[int]) : Liste d'entiers uniques, commençant à 1,
                            de même longueur que le texte

    Returns:
        str: Le texte réordonné
    """
    # Initialisation d'une liste vide de la taille du texte
    result = [''] * len(text)
    
    # Réorganisation des caractères selon les indices
    for pos, index in enumerate(indices):
        result[pos] = text[index-1]
    
    # Conversion de la liste en chaîne
    return ''.join(result)


def try_solution(output: str):
    """
    Teste une solution.

    Args:
        output (str): Le texte réordonné
    """
    json = output
    print("" + dumps(json, separators=(',', ':')))


def main():
    """Fonction principale pour l'exécution du programme."""
    res = reorder(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()