"""
Bubble Sort - iterative and recursive versions.

Bubble sort repeatedly swaps adjacent elements if they are in the
wrong order. Each pass moves the largest unsorted element to its
correct position at the end of the array.
"""


def bubble_sort(arr):
    """Iterative bubble sort. Sorts arr in place."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_recursive(arr, n=None):
    """Recursive bubble sort. Sorts arr[0..n-1] in place."""
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr

    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return bubble_sort_recursive(arr, n - 1)


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]

    a = data.copy()
    bubble_sort(a)
    print("Iterative bubble sort :", a, "| sorted:", is_sorted(a))

    b = data.copy()
    bubble_sort_recursive(b)
    print("Recursive bubble sort :", b, "| sorted:", is_sorted(b))
