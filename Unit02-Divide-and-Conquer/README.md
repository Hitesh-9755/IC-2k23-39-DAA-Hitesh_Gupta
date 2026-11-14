# Unit 02 - Divide and Conquer

## Problem Statement

Implement searching and sorting algorithms based on the
divide-and-conquer paradigm, and build a performance analyzer
that compares experimental running times against theoretical
complexity.

## Algorithms / Approach

### Binary Search - Iterative (`BinarySearchIterative.py`)

- Requires a sorted array; halves the search interval each step.
- O(log n) time, O(1) space.

### Binary Search - Recursive (`BinarySearchRecursive.py`)

- Same halving strategy expressed as recursion on sub-intervals.
- O(log n) time, O(log n) recursion stack space.

### Merge Sort (`MergeSort.py`)

- Divide array in half, sort each half recursively, merge the two
  sorted halves.
- Stable sort; O(n log n) time in all cases; O(n) auxiliary space.

### Quick Sort (`QuickSort.py`)

- Partition around a pivot (Lomuto scheme), recurse on both sides.
- O(n log n) average, O(n^2) worst; O(log n) stack space average.

### Heap Sort (`HeapSort.py`)

- Build a max-heap, repeatedly extract the maximum to the end.
- O(n log n) time in all cases; O(1) auxiliary space.

## Pseudocode

```
MergeSort(A, left, right):
    if left < right:
        mid = (left + right) / 2
        MergeSort(A, left, mid)
        MergeSort(A, mid+1, right)
        Merge(A, left, mid, right)
```

## Time & Space Complexity

| Algorithm            | Best     | Average  | Worst    | Space      |
|----------------------|----------|----------|----------|------------|
| Binary Search (iter) | O(1)     | O(log n) | O(log n) | O(1)       |
| Binary Search (rec)  | O(1)     | O(log n) | O(log n) | O(log n)   |
| Merge Sort           | O(nlogn) | O(nlogn) | O(nlogn) | O(n)       |
| Quick Sort           | O(nlogn) | O(nlogn) | O(n^2)   | O(log n)   |
| Heap Sort            | O(nlogn) | O(nlogn) | O(nlogn) | O(1)       |

## Sorting Performance Comparison System

`SortingPerformanceComparison.py` implements the lab activity:

1. Generates random input arrays for n = 1000 to 32000.
2. Runs Merge Sort, Quick Sort, and Heap Sort on each input.
3. Verifies every output is correctly sorted.
4. Records average execution time over 3 repeats per size.
5. Saves results to `outputs/sorting_results.csv`.
6. Plots n vs execution time with a theoretical n log n curve in
   `outputs/sorting_performance.png`.

### Sample Output

```
n         Merge Sort     Quick Sort     Heap Sort
----------------------------------------------------
1000      0.001245       0.000891       0.001102
...
32000     0.048231       0.039114       0.052876

Results saved to outputs\sorting_results.csv
Plot saved to outputs\sorting_performance.png
```

### Experimental Results

See `outputs/sorting_results.csv` and
`outputs/sorting_performance.png` for measured data. All three
algorithms show the expected O(n log n) growth; Quick Sort is
typically fastest in practice due to cache-friendly partitioning,
while Heap Sort has guaranteed O(n log n) with O(1) space.

## Learning Outcomes

- Applied divide-and-conquer to searching and sorting problems.
- Compared recursive vs iterative implementations.
- Measured real execution times and validated them against
  theoretical complexity analysis.
