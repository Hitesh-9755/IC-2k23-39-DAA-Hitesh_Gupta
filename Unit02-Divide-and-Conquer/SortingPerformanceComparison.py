"""
Sorting Performance Comparison System

Compares Merge Sort, Quick Sort, and Heap Sort experimentally:

- generates random input for different values of n
- verifies the sorted output of every run
- measures execution time for each algorithm
- stores results in a CSV file
- plots n vs execution time and compares with the theoretical
  n log n growth curve
"""

import csv
import math
import os
import random
import time

import matplotlib.pyplot as plt

from MergeSort import merge_sort
from QuickSort import quick_sort
from HeapSort import heap_sort


RESULTS_FILE = os.path.join("outputs", "sorting_results.csv")
PLOT_FILE = os.path.join("outputs", "sorting_performance.png")

SIZES = [1000, 2000, 4000, 8000, 16000, 32000]
REPEATS = 3


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def time_sort(sort_fn, arr):
    """Run sort_fn on a copy of arr and return elapsed seconds."""
    data = arr.copy()
    start = time.perf_counter()
    result = sort_fn(data)
    elapsed = time.perf_counter() - start
    if not is_sorted(result):
        raise ValueError("Sort produced incorrect output")
    return elapsed


def theoretical_nlogn(n, scale):
    """Normalized n log n curve for visual comparison."""
    return scale * n * math.log2(n)


def main():
    os.makedirs("outputs", exist_ok=True)

    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
    }

    results = {name: [] for name in algorithms}

    print("%-10s" % "n", end="")
    for name in algorithms:
        print("%-14s" % name, end="")
    print()
    print("-" * 52)

    for n in SIZES:
        # one random array per size, reused across algorithms
        base = [random.randint(0, 10**6) for _ in range(n)]

        row = [n]
        for name, fn in algorithms.items():
            times = [time_sort(fn, base) for _ in range(REPEATS)]
            avg = sum(times) / len(times)
            results[name].append(avg)
            row.append(avg)

        print("%-10d" % n, end="")
        for t in row[1:]:
            print("%-14.6f" % t, end="")
        print()

    # ---- save CSV ----
    with open(RESULTS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n"] + list(algorithms.keys()))
        for i, n in enumerate(SIZES):
            writer.writerow([n] + [results[name][i] for name in algorithms])
    print("\nResults saved to", RESULTS_FILE)

    # ---- plot ----
    plt.figure(figsize=(10, 6))
    colors = {"Merge Sort": "tab:blue", "Quick Sort": "tab:orange",
              "Heap Sort": "tab:green"}

    for name, times in results.items():
        plt.plot(SIZES, times, marker="o", label=name,
                 color=colors[name], linewidth=2)

    # theoretical n log n reference (scaled to merge sort's last point)
    scale = results["Merge Sort"][-1] / (SIZES[-1] * math.log2(SIZES[-1]))
    theory = [theoretical_nlogn(n, scale) for n in SIZES]
    plt.plot(SIZES, theory, "k--", label="Theoretical n log n",
             linewidth=1.5)

    plt.xlabel("Input size (n)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Sorting Performance Comparison: Merge vs Quick vs Heap Sort")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=150)
    print("Plot saved to", PLOT_FILE)


if __name__ == "__main__":
    main()
