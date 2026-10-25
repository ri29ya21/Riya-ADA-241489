#Build a HuffmanCoder class with build_tree(frequencies: Dict[str, int]) -> Node and 
# generate_codes() -> Dict[str, str] methods accepting character frequencies and returning 
# binary encoding mappings.

import heapq
from itertools import count


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class HuffmanCoder:
    def build_tree(self, frequencies):
        heap = []
        c = count()

        for char, freq in frequencies.items():
            heapq.heappush(
                heap, (freq, next(c), Node(char, freq))
            )

        if not heap:
            return None

        while len(heap) > 1:
            f1, _, left = heapq.heappop(heap)
            f2, _, right = heapq.heappop(heap)

            parent = Node(None, f1 + f2, left, right)
            heapq.heappush(heap, (f1 + f2, next(c), parent))

        return heap[0][2]

    def generate_codes(self, frequencies):
        root = self.build_tree(frequencies)
        codes = {}

        def traverse(node, code):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = code or "0"
                return
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(root, "")
        return codes


n = int(input("Enter number of characters: "))
frequencies = {}

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    frequencies[char] = freq

coder = HuffmanCoder()
codes = coder.generate_codes(frequencies)

print("\nHuffman Codes:")
for char, code in sorted(codes.items()):
    print(char, ":", code)
