"""
Merge Sort - divide and conquer sorting algorithm.

Recursively splits the array into halves, sorts each half, and
merges the two sorted halves.
"""


def merge(arr, left, mid, right):
    """Merge two sorted subarrays arr[left..mid] and arr[mid+1..right]."""
    n1 = mid - left + 1
    n2 = right - mid

    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i = j = k = 0
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[left + k] = left_half[i]
            i += 1
        else:
            arr[left + k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[left + k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[left + k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr, left=0, right=None):
    """Sorts arr[left..right] in place using merge sort."""
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(data)
    print("Sorted array:", data)
    print("Verified sorted:", is_sorted(data))
