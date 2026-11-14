"""
Activity Selection - Greedy Algorithm

Given activities with start and finish times, select the maximum
number of non-overlapping activities. Greedy choice: always pick
the activity that finishes earliest.
"""


def activity_selection(activities):
    """activities: list of (start, finish, name).
    Returns list of selected activity names."""
    # sort by finish time
    sorted_acts = sorted(activities, key=lambda a: a[1])

    selected = []
    last_finish = float("-inf")

    for start, finish, name in sorted_acts:
        if start >= last_finish:
            selected.append(name)
            last_finish = finish

    return selected


if __name__ == "__main__":
    activities = [
        (1, 4, "A1"),
        (3, 5, "A2"),
        (0, 6, "A3"),
        (5, 7, "A4"),
        (3, 8, "A5"),
        (5, 9, "A6"),
        (8, 9, "A7"),
        (8, 10, "A8"),
    ]

    result = activity_selection(activities)
    print("Selected activities:", result)
    print("Count:", len(result))
