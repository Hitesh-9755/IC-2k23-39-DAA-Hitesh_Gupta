"""
Insertion Sort - iterative and recursive versions.

Insertion sort builds the sorted array one element at a time by
inserting each element into its correct position in the sorted
prefix.
"""


def insertion_sort(arr):
    """Iterative insertion sort. Sorts arr in place."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insertion_sort_recursive(arr, n=None):
    """Recursive insertion sort on arr[0..n-1]."""
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr

    insertion_sort_recursive(arr, n - 1)

    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    return arr


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]

    a = data.copy()
    insertion_sort(a)
    print("Iterative insertion sort :", a, "| sorted:", is_sorted(a))

    b = data.copy()
    insertion_sort_recursive(b)
    print("Recursive insertion sort :", b, "| sorted:", is_sorted(b))
