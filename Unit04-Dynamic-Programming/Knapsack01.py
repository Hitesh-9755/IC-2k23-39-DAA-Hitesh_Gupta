"""
0/1 Knapsack - Dynamic Programming

Given items with weights and values and a knapsack capacity,
select a subset of items (each taken at most once) to maximize
total value without exceeding capacity.

Uses a 2D DP table: dp[i][w] = max value using first i items
with capacity w.
"""


def knapsack_01(weights, values, capacity):
    """Returns (max_value, selected_item_indices)."""
    n = len(weights)
    # dp[i][w] = max value with first i items and capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()

    return dp[n][capacity], selected


if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    max_val, items = knapsack_01(weights, values, capacity)
    print("Capacity:", capacity)
    print("Selected items:", items)
    print("Total weight:", sum(weights[i] for i in items))
    print("Maximum value:", max_val)
