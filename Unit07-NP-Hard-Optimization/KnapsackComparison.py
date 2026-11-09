# Compare 0/1 Knapsack using Dynamic Programming
# and Branch and Bound

import time


# Dynamic Programming Approach
def knapsack_dp(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Branch and Bound Approach
def knapsack_branch_bound(profits, weights, capacity):
    n = len(profits)
    max_profit = 0

    # Recursive branch and bound function
    def solve(index, current_weight, current_profit):
        nonlocal max_profit

        # If capacity is exceeded, stop this branch
        if current_weight > capacity:
            return

        # Update maximum profit
        if current_profit > max_profit:
            max_profit = current_profit

        # If all items are checked, stop
        if index == n:
            return

        # Include current item
        solve(
            index + 1,
            current_weight + weights[index],
            current_profit + profits[index]
        )

        # Exclude current item
        solve(index + 1, current_weight, current_profit)

    solve(0, 0, 0)
    return max_profit


# Example input
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50


# Dynamic Programming execution
start = time.perf_counter()
dp_result = knapsack_dp(profits, weights, capacity)
dp_time = time.perf_counter() - start


# Branch and Bound execution
start = time.perf_counter()
bb_result = knapsack_branch_bound(profits, weights, capacity)
bb_time = time.perf_counter() - start


# Display results
print("0/1 Knapsack Comparison")
print("-" * 30)

print("\nDynamic Programming:")
print("Maximum Profit:", dp_result)
print("Execution Time:", dp_time, "seconds")

print("\nBranch and Bound:")
print("Maximum Profit:", bb_result)
print("Execution Time:", bb_time, "seconds")