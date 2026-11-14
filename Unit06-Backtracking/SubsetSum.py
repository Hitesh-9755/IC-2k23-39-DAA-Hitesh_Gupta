"""
Subset Sum Problem - Backtracking

Given a set of numbers and a target sum, find all subsets whose
elements add up to the target. Uses backtracking: include or
exclude each element, prune when the current sum exceeds target.
"""


def subset_sum(nums, target):
    """Returns list of subsets (each a list) summing to target."""
    nums = sorted(nums)
    results = []
    current = []

    def backtrack(index, remaining):
        if remaining == 0:
            results.append(current.copy())
            return
        if index >= len(nums) or remaining < 0:
            return

        # include nums[index]
        current.append(nums[index])
        backtrack(index + 1, remaining - nums[index])
        current.pop()

        # exclude nums[index]
        backtrack(index + 1, remaining)

    backtrack(0, target)
    return results


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9

    subsets = subset_sum(nums, target)
    print("Numbers:", nums)
    print("Target sum:", target)
    print("Subsets found:", len(subsets))
    for s in subsets:
        print("  ", s, "=", sum(s))
