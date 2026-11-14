"""
Huffman Coding - Greedy Algorithm

Builds an optimal prefix-free binary code for a set of characters
based on their frequencies. Greedy choice: repeatedly merge the
two least-frequent nodes.
"""

import heapq


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq):
    """freq: dict char -> frequency. Returns root Node."""
    heap = [Node(f, char=c) for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]


def print_codes(node, code=""):
    """Traverse tree and print char -> binary code."""
    if node.char is not None:
        print("  %s : %s" % (node.char, code if code else "0"))
        return
    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")


def huffman_codes(freq):
    """Returns dict char -> code string."""
    root = build_huffman_tree(freq)
    codes = {}

    def traverse(node, code):
        if node.char is not None:
            codes[node.char] = code if code else "0"
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes


if __name__ == "__main__":
    freq = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}

    print("Character frequencies:", freq)
    codes = huffman_codes(freq)
    print("\nHuffman codes:")
    for char, code in sorted(codes.items()):
        print("  %s : %s" % (char, code))

    # average code length
    total_freq = sum(freq.values())
    avg = sum(len(codes[c]) * f for c, f in freq.items()) / total_freq
    print("\nAverage code length: %.2f bits" % avg)
