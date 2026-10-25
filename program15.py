#Build a GraphBacktracker class featuring graph_coloring(m: int) -> List[int] and 
# hamiltonian_cycle() -> List[int] methods returning vertex-color mappings and valid path 
# cycles.
class GraphBacktracker:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def graph_coloring(self, m):
        colors = [0] * self.n

        def backtrack(v):
            if v == self.n:
                return True

            for c in range(1, m + 1):
                safe = True

                for u in range(self.n):
                    if self.graph[v][u] and colors[u] == c:
                        safe = False
                        break

                if safe:
                    colors[v] = c
                    if backtrack(v + 1):
                        return True
                    colors[v] = 0

            return False

        return colors if backtrack(0) else []

    def hamiltonian_cycle(self):
        if self.n == 0:
            return []

        path = [0] + [-1] * (self.n - 1)

        def backtrack(pos):
            if pos == self.n:
                return self.graph[path[-1]][path[0]] != 0

            for v in range(1, self.n):
                if v in path[:pos]:
                    continue
                if not self.graph[path[pos - 1]][v]:
                    continue

                path[pos] = v
                if backtrack(pos + 1):
                    return True
                path[pos] = -1

            return False

        if backtrack(1):
            return path + [path[0]]
        return []


n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix (0 or 1):")
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

solver = GraphBacktracker(graph)

print("Color assignment:", solver.graph_coloring(m))
print("Hamiltonian cycle:", solver.hamiltonian_cycle())