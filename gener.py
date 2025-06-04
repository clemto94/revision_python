import string
from typing import List


def stepping_cycle(iterable, step):
    buffer = []
    it = iter(iterable)
    idx = 0
    pos = 0

    while True:
        while len(buffer) <= (pos % max(1, len(buffer))):
            try:
                buffer.append(next(it))
            except StopIteration:
                if not buffer:
                    return
                break

        if not buffer:
            return

        current_index = pos % len(buffer)
        pass_num = (pos // len(buffer)) + 1
        yield (idx, pass_num, buffer[current_index])
        idx += 1
        pos += step


def count_replace(ex: str):
    count = 0
    enter = 0
    end = 0
    for s in ex:
        if s == '<':
            count += 1
            enter += 1
        if s == '>':
            count -= 1
            end += 1
    return count, enter, end

def first_duplicate(nums: List[int]):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
        return None
    return None

def pangram(s: str):
    alphabet = set(string.ascii_lowercase)
    letters = set(c for c in s.lower() if c in alphabet)
    return len(letters) == 26

class MaMeta(type):
    def __new__(cls, nom, bases, dct):
        print(f"Création de la classe {nom}")
        return super().__new__(cls, nom, bases, dct)

class MaClasse(metaclass=MaMeta):
    def __new__(cls, a):
        print(f"Création de l'instance {cls} de la classe {cls.__name__}")
        return super().__new__(cls)
    def __init__(self, a):
        self.a = a
    @property
    def carres(self):
        return (x**2 for x in range(self.a))

#m = MaClasse(10)
#print([x for x in m.carres])
