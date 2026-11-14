"""
Binary Search - Recursive version.

Same divide-and-conquer idea as the iterative version, but the
search interval is halved through recursive calls.
"""


def binary_search_recursive(arr, target, low=0, high=None):
    """Returns index of target in sorted arr[low..high], or -1."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for target in [16, 40]:
        idx = binary_search_recursive(arr, target)
        if idx != -1:
            print("Target %d found at index %d" % (target, idx))
        else:
            print("Target %d not found" % target)
