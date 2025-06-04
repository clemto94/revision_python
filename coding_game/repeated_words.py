"""
You are given a string text containing lowercase words, separated by a space. Count how many words
show up in the string more than once.
If the same word shows up two times or more, your counting must be increased just by one.
"""
from json import dumps, loads
import sys
from typing import List
from collections import Counter


def count_repeated_words(text: str) -> int:
    """
    Args:
        text (str): lowercase words, each separated by a single space.

    Returns:
        int: number of repeated words.
    """
    # Write your code here
    # To debug: print ("Debug messages...", file=sys.stderr, flush=True)
    words = text.split()
    words_count = Counter(words)
    return len([word for word, count in words_count.items() if count >= 2])


# Ignore and do not change the code below
def try_solution(count: int):
    """
    Try a solution

    Args:
        count (int): number of repeated words.
    """
    json = count
    print("" + dumps(json, separators=(',', ':')))


def main():
    res = count_repeated_words(
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()