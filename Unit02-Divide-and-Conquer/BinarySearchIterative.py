"""
Binary Search - Iterative version.

Requires a sorted array. Repeatedly halves the search interval
until the target is found or the interval is empty.
"""


def binary_search_iterative(arr, target):
    """Returns index of target in sorted arr, or -1 if absent."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for target in [23, 50]:
        idx = binary_search_iterative(arr, target)
        if idx != -1:
            print("Target %d found at index %d" % (target, idx))
        else:
            print("Target %d not found" % target)
