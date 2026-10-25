#Create a TSPSolver class with solve_tsp(dist_matrix: List[List[int]]) -> int, taking an 
# adjacency matrix and returning the minimum tour cost.
class TSPSolver:
    def solve_tsp(self, dist_matrix):
        n = len(dist_matrix)

        if n == 0:
            return 0
        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Matrix must be square")
        if n == 1:
            return 0

        INF = float("inf")
        dp = [[INF] * n for _ in range(1 << n)]
        dp[1][0] = 0

        for mask in range(1 << n):
            for u in range(n):
                if dp[mask][u] == INF:
                    continue

                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            dp[mask][u] + dist_matrix[u][v]
                        )

        full = (1 << n) - 1
        return min(
            dp[full][u] + dist_matrix[u][0]
            for u in range(1, n)
        )


n = int(input("Enter number of cities: "))
dist_matrix = []

print("Enter distance matrix row by row:")
for _ in range(n):
    dist_matrix.append(list(map(int, input().split())))

solver = TSPSolver()
print("Minimum tour cost:", solver.solve_tsp(dist_matrix))