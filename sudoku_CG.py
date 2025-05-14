from json import dumps, loads
import sys
from typing import List

def check_sudoku(sudoku: List[List[int]]) -> int:
    '''

    Args:

        - sudoku (List[List[int]]): A 2-dimensional array containing integers from 1 to 9.

    Returns:

        An integer. 1 if the sudoku grid is correct. 0 if it is not.
    '''
    def is_valid_group(group: list[int]) -> bool:
        return sorted(group) == list(range(1, 10))

    # Vérifier les lignes
    for row in sudoku:
        if not is_valid_group(row):
            return 0

    # Vérifier les colonnes
    for col in zip(*sudoku):
        if not is_valid_group(list(col)):
            return 0

    # Vérifier les régions 3x3
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            region = [
                sudoku[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(region):
                return 0

    return 1

# Ignore and do not change the code below


def try_solution(is_correct: int):
    '''
    Try a solution

    Args:

        - int (int): An integer. 1 if the sudoku grid is correct. 0 if it is not.
    '''
    json = is_correct
    print("" + dumps(json, separators=(',', ':')))

def main():
    sudoku_grid = [
        [5, 9, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    print(check_sudoku(sudoku_grid))


if __name__ == "__main__":
    main()