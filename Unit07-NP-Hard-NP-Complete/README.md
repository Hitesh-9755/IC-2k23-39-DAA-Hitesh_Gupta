# Unit 07 - NP-Hard and NP-Complete

## Problem Statement

Study NP-hard and NP-complete problems and implement brute-force /
backtracking solutions that demonstrate their exponential
complexity.

## Concepts

### Complexity Classes

- **P** — problems solvable in polynomial time (e.g., sorting, BFS)
- **NP** — problems whose solutions can be *verified* in polynomial
  time (e.g., Hamiltonian cycle — check a given cycle is valid fast)
- **NP-hard** — at least as hard as every problem in NP; no known
  polynomial algorithm (e.g., optimization versions)
- **NP-complete** — in NP AND NP-hard; if any one is solved in P,
  all are (e.g., SAT, Hamiltonian Cycle, Vertex Cover, Clique)

### Key Relationships

```
P ⊆ NP
NP-complete = NP ∩ NP-hard
If P ≠ NP (believed), NP-complete problems have no polynomial algo
```

## Algorithms / Approach

### Hamiltonian Cycle (`HamiltonianCycle.py`)

- NP-complete decision problem: does a cycle visiting every vertex
  exactly once exist?
- Backtracking: extend path vertex by vertex, check adjacency,
  backtrack on dead ends. Exponential O(n!) worst case.

### Vertex Cover (`VertexCover.py`)

- NP-hard optimization: find smallest set of vertices covering all
  edges.
- Brute force: try all subsets of size 1, 2, 3, ... until one
  covers every edge. O(2^n) subsets.

## Pseudocode

```
HamiltonianCycle(path):
    if path contains all vertices:
        return path[0] in neighbors(path[-1])
    for each vertex v not in path:
        if v adjacent to path[-1]:
            path.append(v)
            if HamiltonianCycle(path): return True
            path.pop()
    return False
```

## Time & Space Complexity

| Problem            | Complexity | Class        |
|--------------------|------------|--------------|
| Hamiltonian Cycle  | O(n!)      | NP-complete  |
| Vertex Cover       | O(2^n)     | NP-hard      |

## Sample Input / Output

```
Hamiltonian Cycle on 4-vertex graph:
  -> 0 -> 1 -> 2 -> 3 -> 0 (found)

Vertex Cover on triangle+edge graph:
  -> minimum cover {0, 2} or {1, 2} (size 2)
```

## Why These Problems Matter

- Many real problems (routing, scheduling, network design) reduce
  to NP-complete problems.
- Since no polynomial algorithm is known, we use:
  - **Approximation algorithms** — guaranteed near-optimal
  - **Heuristics** — good solutions fast (greedy, local search)
  - **Exponential algorithms** — exact but only feasible for small n

## Learning Outcomes

- Understood P, NP, NP-hard, NP-complete classes and their
  relationships.
- Implemented brute-force/backtracking for NP-hard problems.
- Recognized why exponential algorithms are infeasible for large
  inputs and when heuristics are necessary.
