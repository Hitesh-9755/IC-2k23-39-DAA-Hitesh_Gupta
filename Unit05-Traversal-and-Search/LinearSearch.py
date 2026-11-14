"""
Linear Search

Traverses the array sequentially and compares each element with
the target until a match is found or the array ends.
"""


def linear_search(arr, target):
    """Returns index of target in arr, or -1 if not present."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    for target in [30, 99]:
        idx = linear_search(arr, target)
        if idx != -1:
            print("Target %d found at index %d" % (target, idx))
        else:
            print("Target %d not found" % target)
