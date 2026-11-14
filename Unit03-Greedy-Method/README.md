# Unit 03 - Greedy Method

## Problem Statement

Implement greedy algorithms that make the locally optimal choice at
each step to reach a globally optimal (or near-optimal) solution.

## Algorithms / Approach

### Fractional Knapsack (`FractionalKnapsack.py`)

- Sort items by value/weight ratio descending.
- Take whole items while capacity remains; take a fraction of the
  last item that doesn't fully fit.
- Greedy works because items are divisible — the ratio ordering is
  provably optimal.

### Activity Selection (`ActivitySelection.py`)

- Sort activities by finish time.
- Select each activity whose start time is after the last selected
  finish time.
- Greedy choice (earliest finish) leaves maximum room for the rest.

### Huffman Coding (`HuffmanCoding.py`)

- Build a min-heap of (frequency, node) pairs.
- Repeatedly merge the two smallest nodes until one tree remains.
- Traverse tree: left = 0, right = 1 to assign prefix-free codes.
- Most frequent characters get shortest codes → minimum expected
  code length.

### Prim's MST (`PrimMST.py`)

- Start from any vertex; maintain a min-heap of crossing edges.
- Always add the cheapest edge connecting tree to non-tree vertex.
- Produces a minimum spanning tree.

## Pseudocode

```
ActivitySelection(A):
    sort A by finish time
    selected = []
    last_finish = -infinity
    for each activity a in A:
        if a.start >= last_finish:
            select a
            last_finish = a.finish
```

## Time & Space Complexity

| Algorithm            | Time       | Space  |
|----------------------|------------|--------|
| Fractional Knapsack  | O(n log n) | O(n)   |
| Activity Selection   | O(n log n) | O(n)   |
| Huffman Coding       | O(n log n) | O(n)   |
| Prim's MST           | O(E log V) | O(V+E) |

## Sample Input / Output

```
Fractional Knapsack: capacity=50, items=[(10,60),(20,100),(30,120)]
  -> value 240.0 (item0 full, item1 full, item2 taken 0.67)

Activity Selection: 8 activities -> selects A1, A4, A7 (3 total)

Huffman: freq {a:5,b:9,c:12,d:13,e:16,f:45}
  -> f=0, c=100, d=101, e=111, a=1100, b=1101 ; avg 2.24 bits

Prim MST: 9-vertex graph -> MST weight 41
```

## Learning Outcomes

- Understood when greedy choice yields optimal solutions
  (fractional knapsack, activity selection, Huffman, MST).
- Compared greedy vs dynamic programming approaches.
- Implemented heap-based greedy selection (Prim, Huffman).
