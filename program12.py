# Implement floyd_warshall(graph: List[List[int]]) -> List[List[int]] and 
# optimal_bst(keys: List[int], freq: List[int]) -> int, accepting distance/frequency matrices
#  and returning shortest-path or cost matrices.
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    INF = float("inf")

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    if any(dist[i][i] < 0 for i in range(n)):
        raise ValueError("Negative cycle detected")

    return dist


def optimal_bst(keys, freq):
    n = len(keys)

    if n != len(freq):
        raise ValueError("Keys and frequencies must have equal length")
    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]
    prefix = [0]

    for f in freq:
        prefix.append(prefix[-1] + f)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = prefix[j + 1] - prefix[i]
            dp[i][j] = float("inf")

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                dp[i][j] = min(dp[i][j], left + right + total)

    return dp[0][n - 1]


print("Floyd-Warshall input:")
n = int(input("Enter number of vertices: "))
INF = float("inf")
graph = []

print("Enter adjacency matrix row by row (-1 for no edge):")
for i in range(n):
    row = list(map(int, input().split()))
    row = [INF if x == -1 else x for x in row]
    graph.append(row)

dist = floyd_warshall(graph)

print("Shortest distance matrix:")
for row in dist:
    print(["INF" if x == INF else x for x in row])

print("\nOptimal BST input:")
keys = list(map(int, input("Enter sorted keys: ").split()))
freq = list(map(int, input("Enter frequencies: ").split()))

print("Minimum search cost:", optimal_bst(keys, freq))