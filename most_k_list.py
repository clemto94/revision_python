def at_most_k_distinct(arr, k):
    count = {}  # dictionnaire classique
    left = 0
    result = 0

    for i in range(len(arr)):
        if arr[i] not in count:
            count[arr[i]] = 0
        count[arr[i]] += 1

        if count[arr[i]] == 1:
            k -= 1

        while k < 0:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
                k += 1
            left += 1

        result += i - left + 1

    return result

def subarrays_with_at_least_k_distinct(arr, k):
    if k == 0:
        return (len(arr) * (len(arr) + 1)) // 2
    return at_most_k_distinct(arr, len(arr)) - at_most_k_distinct(arr, k - 1)

# Exemple
arr = [2, 1, 2, 1, 6]
k = 2
print(subarrays_with_at_least_k_distinct(arr, k))
