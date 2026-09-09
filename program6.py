#Construct a Graph class with kruskal_mst() -> List[Edge] and prim_mst() -> List[Edge] 
# methods that process edge-weighted graph structures and return the MST edge set.
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    # Add an edge
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # ---------------- KRUSKAL'S ALGORITHM ----------------
    def kruskal_mst(self):
        # Sort edges according to weight
        edges = sorted(self.edges)

        parent = list(range(self.vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                return True

            return False

        mst = []

        for weight, u, v in edges:
            if union(u, v):
                mst.append((u, v, weight))

            if len(mst) == self.vertices - 1:
                break

        return mst

    # ---------------- PRIM'S ALGORITHM ----------------
    def prim_mst(self):
        visited = [False] * self.vertices
        mst = []

        # Start from vertex 0
        visited[0] = True

        while len(mst) < self.vertices - 1:
            minimum = None

            for weight, u, v in self.edges:
                # Edge should connect visited to unvisited vertex
                if visited[u] != visited[v]:
                    if minimum is None or weight < minimum[0]:
                        minimum = (weight, u, v)

            if minimum is None:
                break

            weight, u, v = minimum
            mst.append((u, v, weight))

            # Mark the new vertex as visited
            if visited[u]:
                visited[v] = True
            else:
                visited[u] = True

        return mst


# ---------------- MAIN PROGRAM ----------------

g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:")
print(g.kruskal_mst())

print("\nPrim MST:")
print(g.prim_mst())