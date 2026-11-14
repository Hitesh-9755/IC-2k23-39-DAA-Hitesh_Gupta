"""
Vertex Cover - NP-Hard Problem

A vertex cover is a set of vertices such that every edge in the
graph has at least one endpoint in the set. Finding the minimum
vertex cover is NP-hard.

This implementation uses brute-force backtracking to find the
minimum vertex cover, demonstrating exponential complexity.
"""

from itertools import combinations


def is_vertex_cover(graph, vertices, cover):
    """Check if cover set covers all edges."""
    for u in vertices:
        for v in graph[u]:
            if u < v:  # each edge once
                if u not in cover and v not in cover:
                    return False
    return True


def min_vertex_cover(graph):
    """Find minimum vertex cover by trying all subset sizes.
    graph: dict vertex -> list of neighbors."""
    vertices = list(graph.keys())
    n = len(vertices)

    for size in range(1, n + 1):
        for combo in combinations(vertices, size):
            cover = set(combo)
            if is_vertex_cover(graph, vertices, cover):
                return list(cover)
    return vertices  # worst case: all vertices


if __name__ == "__main__":
    # triangle + one extra edge
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2],
    }

    cover = min_vertex_cover(graph)
    print("Vertices:", list(graph.keys()))
    print("Edges:", [(u, v) for u in graph for v in graph[u] if u < v])
    print("Minimum vertex cover:", cover)
    print("Size:", len(cover))
