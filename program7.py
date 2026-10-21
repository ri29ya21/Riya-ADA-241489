#program7:Build a ShortestPath class containing dijkstra(src: int) -> List[int] and 
# bellman_ford(src: int) -> List[int] methods taking a starting node and returning 
# distance arrays (or error status for negative cycles).


import heapq

class ShortestPath:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.graph = [[] for _ in range(n)]

        for u, v, w in edges:
            self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.n
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)

            if d != dist[u]:
                continue

            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist

    def bellman_ford(self, src):
        dist = [float('inf')] * self.n
        dist[src] = 0

        for _ in range(self.n - 1):
            updated = False

            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            if not updated:
                break

        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return None

        return dist


# Terminal input
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []
print("Enter edges (source destination weight):")

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

src = int(input("Enter source vertex: "))

sp = ShortestPath(n, edges)

print("Dijkstra:", sp.dijkstra(src))

result = sp.bellman_ford(src)
if result is None:
    print("Bellman-Ford: Negative weight cycle detected")
else:
    print("Bellman-Ford:", result)