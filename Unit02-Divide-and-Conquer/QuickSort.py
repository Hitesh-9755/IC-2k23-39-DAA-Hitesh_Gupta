"""
Quick Sort - divide and conquer sorting algorithm.

Picks a pivot element, partitions the array so elements smaller
than the pivot go left and larger go right, then recurses on
both partitions.
"""


def partition(arr, low, high):
    """Lomuto partition scheme. Returns final pivot index."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    """Sorts arr[low..high] in place using quick sort."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    quick_sort(data)
    print("Sorted array:", data)
    print("Verified sorted:", is_sorted(data))
