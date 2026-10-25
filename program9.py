#Implement knapsack_01(weights: List[int], values: List[int], capacity: int) -> int utilizing
#  2D/1D DP methods that accept item properties and return maximum value.

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter knapsack capacity: "))

if len(weights) != n or len(values) != n:
    print("Error: Enter exactly", n, "weights and values.")
else:
    result = knapsack_01(weights, values, capacity)
    print("Maximum value:", result)
