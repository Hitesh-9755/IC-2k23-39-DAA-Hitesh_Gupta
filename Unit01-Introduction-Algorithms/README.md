# Unit 01 - Introduction to Algorithms

## Problem Statement

Implement and analyze basic sorting algorithms to understand how
different strategies affect time and space complexity.

## Algorithms / Approach

### Bubble Sort (`BubbleSort.py`)

- **Iterative**: repeatedly swap adjacent out-of-order elements;
  each pass places the largest remaining element at the end.
- **Recursive**: one pass of adjacent swaps, then recurse on the
  first `n-1` elements.

### Selection Sort (`SelectionSort.py`)

- Scan the unsorted portion for the minimum element and swap it
  into place. Exactly `n-1` swaps regardless of input order.

### Insertion Sort (`InsertionSort.py`)

- **Iterative**: grow a sorted prefix by inserting each new
  element into its correct position.
- **Recursive**: recursively sort the first `n-1` elements, then
  insert the last element into the sorted prefix.

## Pseudocode

```
InsertionSort(A):
    for i = 1 to n-1:
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

## Time & Space Complexity

| Algorithm        | Best     | Average  | Worst    | Space  |
|------------------|----------|----------|----------|--------|
| Bubble Sort      | O(n)     | O(n^2)   | O(n^2)   | O(1)   |
| Selection Sort   | O(n^2)   | O(n^2)   | O(n^2)   | O(1)   |
| Insertion Sort   | O(n)     | O(n^2)   | O(n^2)   | O(1)   |

## Sample Input / Output

```
Input : [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```

## Learning Outcomes

- Understood iterative vs recursive formulations of the same idea.
- Compared how input order affects running time (best vs worst case).
- Practiced in-place sorting with O(1) auxiliary space.
