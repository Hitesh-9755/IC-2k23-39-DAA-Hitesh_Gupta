"""
Hamiltonian Cycle - NP-Complete Problem

A Hamiltonian cycle visits every vertex exactly once and returns
to the start. Finding one is NP-complete — no known polynomial
algorithm exists. This implementation uses backtracking to
demonstrate the exponential search.
"""


def is_safe(graph, v, path):
    """Check if v can be added to current path."""
    # v must not already be in path
    if v in path:
        return False
    # v must be adjacent to last vertex in path
    return path[-1] in graph and v in graph[path[-1]]


def hamiltonian_cycle(graph, start):
    """Returns a Hamiltonian cycle (list of vertices) or None.
    graph: dict vertex -> list of neighbors."""
    vertices = list(graph.keys())
    n = len(vertices)
    path = [start]

    def backtrack():
        if len(path) == n:
            # check if last vertex connects back to start
            if start in graph[path[-1]]:
                return True
            return False

        for v in vertices:
            if is_safe(graph, v, path):
                path.append(v)
                if backtrack():
                    return True
                path.pop()  # backtrack
        return False

    if backtrack():
        return path + [start]  # close the cycle
    return None


if __name__ == "__main__":
    # small graph for demo
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2],
    }

    cycle = hamiltonian_cycle(graph, 0)
    if cycle:
        print("Hamiltonian cycle found:", " -> ".join(map(str, cycle)))
    else:
        print("No Hamiltonian cycle exists")
