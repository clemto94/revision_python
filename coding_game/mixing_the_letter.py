"""
Your friends sent you a message and wanted to show you a funny trick. For each word, the first letter
and the last letter stay the same, but the letters inside are mixed. The human brain is able to recognize
the words and automatically decodes the message.
For example, the word "orange" could become "ogarne", "orngae", ...
You don't find that trick really fun, so you will write a program that does the decoding for you.
Fortunately, your friends have a limited vocabulary. All the words they know are contained in a
predefined list.

You have to implement the function decode(words, message) which takes two parameters:
words : a list of strings, containing all the words known by your friends (20 words max). All the letters
are lower-cased. Some words may have only one letter.
message : a string, containing the message coded by your friends. All the letters are lower-cased too.
Each word is separated by a single space.

The function must return a string, containing the decoded message. For each word, you must find the
original one.

There will never be ambiguity in the known words. There are never two words that are anagrams AND
have the same first and last letters. For example, there will never have both the words "clam" and
"calm".
"""
from json import dumps, loads
import sys
from typing import List
from collections import Counter


def get_anagram_list(words: List[str]) -> List:
    """
    Crée une liste de tuples contenant chaque mot et son compteur de caractères.
    
    Args:
        words (List[str]): Liste de mots à analyser
        
    Returns:
        List: Liste de tuples (mot, Counter)
    """
    anagram_list = []
    for word in words:
        anagram_list.append((word, Counter(word)))
    return anagram_list


def decode(words: List[str], message: str) -> str:
    """
    Décode un message en utilisant une liste de mots connus.
    
    Args:
        words (List[str]): Liste des mots connus par vos amis
        message (str): Le message envoyé par vos amis
        
    Returns:
        str: Le message décodé
    """
    anagram_list = get_anagram_list(words)
    result = []
    
    for word in message.split():
        encoded_counter = Counter(word)
        for w, counter in anagram_list:
            if (counter == encoded_counter and 
                w[0] == word[0] and 
                w[-1] == word[-1]):
                result.append(w)
                
    return ' '.join(result)


def try_solution(clear_message: str):
    """
    Teste une solution.
    
    Args:
        clear_message (str): Le message décodé
    """
    json = clear_message
    print("" + dumps(json, separators=(',', ':')))


def main():
    res = decode(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()