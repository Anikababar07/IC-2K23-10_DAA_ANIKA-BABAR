# 0/1 Knapsack Problem using Branch and Bound

class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight


def bound(node, n, capacity, weights, profits):
    # If weight exceeds capacity, return 0
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1

    # Add items while they fit completely
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += profits[j]
        j += 1

    # Add a fraction of the next item
    if j < n:
        remaining_capacity = capacity - total_weight
        profit_bound += remaining_capacity * profits[j] / weights[j]

    return profit_bound


def knapsack(capacity, weights, profits):
    n = len(profits)

    # Sort items according to profit/weight ratio
    items = sorted(
        zip(weights, profits),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    weights = [item[0] for item in items]
    profits = [item[1] for item in items]

    queue = []
    root = Node(-1, 0, 0)
    queue.append(root)

    max_profit = 0

    while queue:
        current = queue.pop(0)

        if current.level == n - 1:
            continue

        next_level = current.level + 1

        # Include the next item
        include = Node(
            next_level,
            current.profit + profits[next_level],
            current.weight + weights[next_level]
        )

        if include.weight <= capacity and include.profit > max_profit:
            max_profit = include.profit

        if bound(include, n, capacity, weights, profits) > max_profit:
            queue.append(include)

        # Exclude the next item
        exclude = Node(
            next_level,
            current.profit,
            current.weight
        )

        if bound(exclude, n, capacity, weights, profits) > max_profit:
            queue.append(exclude)

    return max_profit


# Example input
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack(capacity, weights, profits)

print("Maximum Profit:", result)