#Implement fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float
#  and job_scheduling(jobs: List[Job]) -> List[int] functions returning maximum attainable 
# profit and optimal job sequence.
def fractional_knapsack(weights, values, capacity):
    items = []

    # Calculate value/weight ratio
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort according to highest ratio
    items.sort(reverse=True)

    total_profit = 0.0

    for ratio, weight, value in items:

        if capacity == 0:
            break

        # Take complete item
        if weight <= capacity:
            capacity -= weight
            total_profit += value

        # Take fraction of item
        else:
            fraction = capacity / weight
            total_profit += value * fraction
            capacity = 0

    return total_profit


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, values, capacity))