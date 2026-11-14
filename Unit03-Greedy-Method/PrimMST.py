"""
Prim's Algorithm - Minimum Spanning Tree (Greedy)

Grows the MST by always adding the cheapest edge that connects a
vertex in the tree to a vertex outside it.
"""

import heapq


def prim_mst(graph):
    """graph: dict vertex -> list of (neighbor, weight).
    Returns list of (u, v, weight) edges in the MST."""
    start = next(iter(graph))
    in_mst = {start}
    heap = []

    # push all edges from start
    for neighbor, weight in graph[start]:
        heapq.heappush(heap, (weight, start, neighbor))

    mst = []
    while heap and len(in_mst) < len(graph):
        weight, u, v = heapq.heappop(heap)
        if v in in_mst:
            continue
        mst.append((u, v, weight))
        in_mst.add(v)
        for neighbor, w in graph[v]:
            if neighbor not in in_mst:
                heapq.heappush(heap, (w, v, neighbor))

    return mst


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("H", 8)],
        "B": [("A", 4), ("C", 8), ("H", 11)],
        "C": [("B", 8), ("D", 7), ("F", 4)],
        "D": [("C", 7), ("E", 9), ("F", 14)],
        "E": [("D", 9), ("F", 10)],
        "F": [("C", 4), ("D", 14), ("E", 10), ("G", 2)],
        "G": [("F", 2), ("H", 1), ("I", 6)],
        "H": [("A", 8), ("B", 11), ("G", 1), ("I", 7)],
        "I": [("G", 6), ("H", 7)],
    }

    mst = prim_mst(graph)
    print("Edges in MST:")
    total = 0
    for u, v, w in mst:
        print("  %s -- %s : %d" % (u, v, w))
        total += w
    print("Total weight:", total)
