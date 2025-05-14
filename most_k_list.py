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

# Exemple
arr = [2, 1, 2, 1, 6]
k = 2
print(subarrays_with_at_least_k_distinct(arr, k))
