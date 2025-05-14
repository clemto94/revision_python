from itertools import batched


def sous_ensembles_k(tab, k):
    return [tab[i:i+k] for i in range(0, len(tab), k)]

# Exemple d'utilisation
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
result = sous_ensembles_k(l, k)
print(result)

r_batch = [list(i) for i in list(batched([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))]
print(r_batch)