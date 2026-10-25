# Implement solveNQueens(n: int) -> List[List[str]], taking board dimension N and returning
#  all valid N×N board configurations.
def solveNQueens(n):
    results = []
    board = [-1] * n
    columns = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            result = []
            for r in range(n):
                line = ["."] * n
                line[board[r]] = "Q"
                result.append("".join(line))
            results.append(result)
            return

        for col in range(n):
            if (col in columns or
                row - col in diag1 or
                row + col in diag2):
                continue

            board[row] = col
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board[row] = -1

    if n > 0:
        backtrack(0)

    return results


n = int(input("Enter board size N: "))
solutions = solveNQueens(n)

print("Total solutions:", len(solutions))
for solution in solutions:
    for row in solution:
        print(row)
    print()