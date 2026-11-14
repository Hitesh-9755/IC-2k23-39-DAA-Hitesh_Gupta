"""
Coin Change - Dynamic Programming

Given coin denominations and a target amount, find the minimum
number of coins needed to make the amount (infinite supply of
each coin). Returns -1 if impossible.

dp[x] = min coins to make amount x.
"""


def coin_change(coins, amount):
    """Returns (min_coins, coin_list) or (-1, [])."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    parent = [None] * (amount + 1)

    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x and dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                parent[x] = coin

    if dp[amount] == float("inf"):
        return -1, []

    # reconstruct coins used
    used = []
    x = amount
    while x > 0:
        used.append(parent[x])
        x -= parent[x]

    return dp[amount], used


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11

    count, used = coin_change(coins, amount)
    print("Coins:", coins)
    print("Amount:", amount)
    if count == -1:
        print("Cannot make amount")
    else:
        print("Minimum coins:", count)
        print("Coins used:", used)
