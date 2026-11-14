# Unit 05 - Traversal and Search

## Problem Statement

Implement fundamental searching techniques over linear data
structures.

## Algorithms / Approach

### Linear Search (`LinearSearch.py`)

- Scan the array element by element until the target is found.
- Works on sorted and unsorted data.
- O(n) time, O(1) space.

## Pseudocode

```
LinearSearch(A, key):
    for i = 0 to n-1:
        if A[i] == key:
            return i
    return -1
```

## Time & Space Complexity

| Case    | Time   | Space |
|---------|--------|-------|
| Best    | O(1)   | O(1)  |
| Average | O(n/2) | O(1)  |
| Worst   | O(n)   | O(1)  |

## Sample Input / Output

```
Input : [10, 20, 30, 40, 50], target = 30
Output: Target 30 found at index 2

Input : [10, 20, 30, 40, 50], target = 99
Output: Target 99 not found
```

## Learning Outcomes

- Understood sequential search and its linear complexity.
- Compared it conceptually with binary search (Unit 02), which
  trades the sorted-input requirement for O(log n) lookup.
