import time
from collections import defaultdict
from itertools import islice


def subarrays_with_at_least_k_distinct(arr, k):
    def at_most_k(arr, k):
        count = 0
        left = 0
        freq = {}
        for right in range(len(arr)):
            if arr[right] not in freq:
                freq[arr[right]] = 0
            freq[arr[right]] += 1

            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            count += right - left + 1

        return count

    return at_most_k(arr, k) - at_most_k(arr, k - 1)


def findMinimumLengthSubarray(arr, k):
    n = len(arr)
    if len(set(arr)) < k:
        return -1

    min_len = n + 1

    for start in range(n):
        for end in range(start + k, n + 1):
            window = list(islice(arr, start, end))
            if len(set(window)) >= k:
                min_len = min(min_len, len(window))
                print(window, min_len)
                break

    return min_len if min_len <= n else -1


# Exemple
arr = [2, 1, 2, 1, 6]
k = 2
s1 = time.time()
print(subarrays_with_at_least_k_distinct(arr, k))
e1 = time.time()
print(e1 - s1)

arr1 = [2, 1, 2, 1, 6]
s2 = time.time()
print(findMinimumLengthSubarray(arr1, k))
e2 = time.time()
print(e2 - s2)
