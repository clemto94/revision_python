
from itertools import permutations, combinations, combinations_with_replacement, groupby
from operator import itemgetter

# INPUT
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# output
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle
def person_lister(f):
    def inner(people):
        getcount = itemgetter(0, 1, 2, 3)
        people = sorted(people, key=lambda x: int(itemgetter(2)(x)))
        l = list(map(getcount, people))
        return [f(s) for s in l]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# sort + permutation
# input HACK 2
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
m, n = input().split(" ")
getter = itemgetter(*range(int(n)))
p = permutations(list(m), int(n))
p_s = sorted(p, key=getter)
for p in p_s:
    print("".join(p))

# sort + combination
# input HACK 2
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
v, k = input().split(" ")
word = sorted(v)
for n in range(1, int(k) + 1):
    getter = itemgetter(*range(int(n)))

    c = combinations(word, n)
    c_s = sorted(c, key=getter)
    # print(list(c_s))

    for items in c_s:
        print("".join(items))

# sort + combinations_with_replacement
# input HACK 2
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK
v, k = input().split(" ")
word = sorted(v)

for items in combinations_with_replacement(word, int(k)):
    print("".join(items))

# groupby
# input 1222311
# (1, 1) (3, 2) (1, 3) (2, 1)
s_in = list(input())
s_a = []

for k, g in groupby(s_in):
    s_a.append(str((len(list(g)), int(k))))

print(" ".join(s_a))

def permu_list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([
        [i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i+j+k != n
    ])