"""
Objective Suppose there is a sale on blue, green, and red shirts for the next n days. On day , it costs
dollars to buy a blue shirt, dollars to buy a green shirt, and dollars to buy a red shirt. You wish to
buy a single shirt for each for the next n days, but with the caveat that you cannot buy the same color
shirt on consecutive days.
Implementation Implement the function lowest_cost(blue_costs, green_costs, red_costs)
which takes in three lists of length n: blue_costs , green_costs , red_costs . Each element in these
lists is a positive integer that represents the daily price of a shirt. Your task is to output a list
representing the shirt color you buy for each of the n days, such that the total combined cost of the n
shirts is minimized. Specifically, your output list will be of length n, where each element in the list is
either 'b' , 'g' , or 'r' . The element of the output list represents the color of the day's shirt.
Note that there will be exactly one color sequence that minimizes the cost for the n shirts.
Examples For inputs blue_costs = [1, 1, 1] green_costs = [3, 5, 7] red_costs = [4,
6, 4] the output list should be ['b', 'g', 'b'] (total cost of 7). Buying only blue shirts would be
the cheapest, but remember that no two consecutive days can have the same color shirt.
For inputs blue_costs = [18, 12, 1, 9] green_costs = [13, 15, 7, 9] red_costs =
[12, 16, 4, 8] the output list should be ['r', 'g', 'b', 'r'] (total cost of 36).
For inputs blue_costs = [100, 1, 76, 14] green_costs = [22, 20, 1, 2] red_costs =
[99, 99, 5, 12] the output list should be ['g', 'b', 'r', 'g'] (total cost of 30).
"""
def lowest_cost(blue_costs, green_costs, red_costs):
    n = len(blue_costs)

    # dp[i][color] = (total_cost, previous_color)
    dp = [{'b': (blue_costs[0], None),
           'g': (green_costs[0], None),
           'r': (red_costs[0], None)}]

    for i in range(1, n):
        prev = dp[-1]
        curr = {}

        # Choisir bleu aujourd'hui, donc hier = g ou r
        cost_b = blue_costs[i] + min(prev['g'][0], prev['r'][0])
        prev_b = 'g' if prev['g'][0] <= prev['r'][0] else 'r'
        curr['b'] = (cost_b, prev_b)

        # Choisir vert aujourd'hui, donc hier = b ou r
        cost_g = green_costs[i] + min(prev['b'][0], prev['r'][0])
        prev_g = 'b' if prev['b'][0] <= prev['r'][0] else 'r'
        curr['g'] = (cost_g, prev_g)

        # Choisir rouge aujourd'hui, donc hier = b ou g
        cost_r = red_costs[i] + min(prev['b'][0], prev['g'][0])
        prev_r = 'b' if prev['b'][0] <= prev['g'][0] else 'g'
        curr['r'] = (cost_r, prev_r)

        dp.append(curr)

    # Dernier jour : prendre la couleur avec le coût minimum
    last_day = dp[-1]
    last_color = min(last_day, key=lambda c: last_day[c][0])

    # Backtrack pour retrouver les choix
    result = [last_color]
    for i in range(n - 1, 0, -1):
        last_color = dp[i][last_color][1]
        result.append(last_color)

    return result[::-1]  # on inverse car on a backtracké

print(lowest_cost([1, 1, 1], [3, 5, 7], [4, 6, 4]))
# ➤ ['b', 'g', 'b']

print(lowest_cost([18, 12, 1, 9], [13, 15, 7, 9], [12, 16, 4, 8]))
# ➤ ['r', 'g', 'b', 'r']

print(lowest_cost([100, 1, 76, 14], [22, 20, 1, 2], [99, 99, 5, 12]))
# ➤ ['g', 'b', 'r', 'g']
