"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
Sac a dos (Knapsack Problem)


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
import math


def canPartition(nums) -> bool:
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # somme 0 est toujours possible

    for num in nums:
        for i in range(target, num - 1, -1):
            print(dp[i], dp[i - num])
            dp[i] = dp[i] or dp[i - num]
    # print(dp)
    return dp[target]

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp

def is_premier(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): # num**0.5
        if num % i == 0:
            return False
    return True

def nombres_premiers_jusqua(N):
    if N < 2:
        return []

    est_premier = [True] * (N + 1)
    est_premier[0] = est_premier[1] = False

    for i in range(2, int(N**0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, N + 1, i):
                est_premier[multiple] = False

    return [i for i, premier in enumerate(est_premier) if premier]