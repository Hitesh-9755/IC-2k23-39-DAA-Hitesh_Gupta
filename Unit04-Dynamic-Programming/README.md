# Unit 04 - Dynamic Programming

## Problem Statement

Implement dynamic programming solutions for optimization problems
with overlapping subproblems and optimal substructure.

## Algorithms / Approach

### 0/1 Knapsack (`Knapsack01.py`)

- 2D DP table: `dp[i][w]` = max value using first i items with
  capacity w.
- For each item: either skip it (`dp[i-1][w]`) or take it
  (`value + dp[i-1][w-weight]`), whichever is larger.
- Backtrack through the table to recover selected items.

### Longest Common Subsequence (`LongestCommonSubsequence.py`)

- `dp[i][j]` = LCS length of `s1[:i]` and `s2[:j]`.
- If characters match: `dp[i][j] = dp[i-1][j-1] + 1`.
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
- Backtrack to recover the actual subsequence string.

### Coin Change (`CoinChange.py`)

- `dp[x]` = minimum coins to make amount x.
- For each amount, try every coin: `dp[x] = min(dp[x], dp[x-coins[i]] + 1)`.
- Parent array tracks which coin was used for reconstruction.

## Pseudocode

```
Knapsack01(W, V, C):
    for i = 1 to n:
        for w = 0 to C:
            if W[i] <= w:
                dp[i][w] = max(V[i] + dp[i-1][w-W[i]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
```

## Time & Space Complexity

| Algorithm            | Time        | Space       |
|----------------------|-------------|-------------|
| 0/1 Knapsack         | O(n * C)    | O(n * C)    |
| LCS                  | O(m * n)    | O(m * n)    |
| Coin Change          | O(amount*k) | O(amount)   |

(k = number of coin denominations)

## Sample Input / Output

```
Knapsack: weights=[10,20,30], values=[60,100,120], cap=50
  -> max value 220, items [0, 2]

LCS: "AGGTAB" vs "GXTXAYB"
  -> length 4, subsequence "GTAB"

Coin Change: coins=[1,2,5], amount=11
  -> 3 coins: [5, 5, 1]
```

## Learning Outcomes

- Identified problems with optimal substructure and overlapping
  subproblems.
- Implemented bottom-up tabulation DP with backtracking.
- Compared DP (guaranteed optimal, more space) vs greedy
  (faster, may be suboptimal) approaches.
