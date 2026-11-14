"""
Selection Sort

Repeatedly find the minimum element in the unsorted portion and
swap it into its correct position.
"""


def selection_sort(arr):
    """Sorts arr in place using selection sort."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    selection_sort(data)
    print("Sorted array:", data)
    print("Verified sorted:", is_sorted(data))
