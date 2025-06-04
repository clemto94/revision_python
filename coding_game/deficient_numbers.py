"""
Goal A deficient number is a number such that the sum of its divisors is less than the double of that
number. Each deficient number has a deficiency, which is the difference between the sum of its divisors
and the double of that number.
Consider the number 21 . Its divisors are 1 , 3 , 7 , and 21 . The sum of those numbers is 32 , which is less
than the double of 21 , 42 . Therefore, 21 is a deficient number. It's deficiency is 10 , because 42 - 32 = 10
.
implement sum_deficiency(ranges) , which takes a list in parameters. Each element of the list
contains 2 integers, defining a range of number between the first and the second integer (inclusive).
You must return a list of integers, having the same size as the parameter ranges . Each of these
integers is the sum of the deficiency of all deficient numbers that exist within the corresponding range.
There is a maximum of 170 elements in ranges . The biggest range can be 0 to 10000.
Hint: these numbers are quite big, maybe you should optimize your algorithm. If you recalculate the
deficiency of each number of each range, the execution may timeout.
"""
from json import dumps, loads
from typing import List

def sum_deficiency(ranges: List[List[int]]) -> List[int]:
    """Calcule la somme des déficiences pour chaque plage donnée.

    Args:
        ranges (List[List[int]]): Liste de plages. Chaque plage est une liste de 2 entiers.

    Returns:
        List[int]: Liste contenant la somme des déficiences pour chaque plage.
    """
    max_range = 10000
    deficiences = [0] * (max_range + 1)

    # Pré-calcul des déficiences pour tous les nombres jusqu'à max_range
    for n in range(1, max_range + 1):
        divisors = []
        # Optimisation : on ne va que jusqu'à la racine carrée
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                # Si i n'est pas la racine carrée et pas 1, ajouter n//i
                if i != n // i and i != 1:
                    divisors.append(n // i)
        if n not in divisors:
            divisors.append(n)

        sum_div = sum(divisors)
        double_n = n * 2

        # Si le nombre est déficient, calculer sa déficience
        if sum_div < double_n:
            deficiences[n] = double_n - sum_div

    # Calculer la somme des déficiences pour chaque plage
    result = []
    for r in ranges:
        start, end = r
        result.append(sum(deficiences[start:end + 1]))
    return result


def try_solution(output: List[int]):
    """Teste une solution.

    Args:
        output (List[int]): Liste des sommes de déficiences pour chaque plage.
    """
    json = output
    print("" + dumps(json, separators=(',', ':')))


def main():
    res = sum_deficiency(loads(input()))
    try_solution(res)


if __name__ == "__main__":
    main()