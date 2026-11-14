"""
Fractional Knapsack - Greedy Algorithm

Given items with weights and values, fill a knapsack of capacity W
to maximize total value. Items can be broken (fractional), so the
greedy choice is: always take the item with the highest
value/weight ratio first.
"""


def fractional_knapsack(items, capacity):
    """items: list of (weight, value). Returns (max_value, taken)."""
    # sort by value/weight ratio, descending
    indexed = [(v / w, i, w, v) for i, (w, v) in enumerate(items)]
    indexed.sort(reverse=True)

    total_value = 0.0
    taken = []
    remaining = capacity

    for ratio, i, w, v in indexed:
        if remaining <= 0:
            break
        if w <= remaining:
            # take whole item
            taken.append((i, 1.0))
            total_value += v
            remaining -= w
        else:
            # take fraction of the item
            frac = remaining / w
            taken.append((i, frac))
            total_value += v * frac
            remaining = 0

    return total_value, taken


if __name__ == "__main__":
    # (weight, value)
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50

    value, taken = fractional_knapsack(items, capacity)
    print("Capacity:", capacity)
    for idx, frac in taken:
        w, v = items[idx]
        print("  Item %d: weight=%d value=%d -> taken %.2f"
              % (idx, w, v, frac))
    print("Maximum value:", value)
