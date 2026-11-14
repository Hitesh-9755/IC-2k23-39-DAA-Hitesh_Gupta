# Unit 06 - Backtracking

## Problem Statement

Implement backtracking algorithms that explore the search space
depth-first, undoing choices (backtracking) when constraints are
violated.

## Algorithms / Approach

### N-Queens (`NQueens.py`)

- Place queens row by row on an NxN board.
- Before placing, check column and both diagonals for conflicts.
- If safe, place and recurse to next row; if row == n, record
  solution. On return, remove queen (backtrack) and try next column.

### Subset Sum (`SubsetSum.py`)

- For each number, branch: include it or exclude it.
- Prune when remaining sum < 0 or index exceeds array.
- When remaining == 0, a valid subset is found.

## Pseudocode

```
NQueens(board, row):
    if row == n: record solution; return
    for col in 0..n-1:
        if is_safe(row, col):
            board[row] = col
            NQueens(board, row+1)
            board[row] = -1   // backtrack
```

## Time & Space Complexity

| Algorithm   | Time        | Space  |
|-------------|-------------|--------|
| N-Queens    | O(n!) worst | O(n)   |
| Subset Sum  | O(2^n)      | O(n)   |

Both are exponential — backtracking explores all possibilities
with pruning.

## Sample Input / Output

```
N-Queens n=4 -> 2 solutions:
  Q . . .      . Q . .
  . . . Q      . . . Q
  . . Q .      Q . . .
  . Q . .      . . Q .

Subset Sum [3,34,4,12,5,2] target=9
  -> [3,4,2], [4,5], [7? no] ... subsets summing to 9
```

## Learning Outcomes

- Understood backtracking as DFS with undo on constraint violation.
- Implemented constraint checking (N-Queens) and pruning (Subset Sum).
- Recognized exponential worst-case complexity of exhaustive search.
