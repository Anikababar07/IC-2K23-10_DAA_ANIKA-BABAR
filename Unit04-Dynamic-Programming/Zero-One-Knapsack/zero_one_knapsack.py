def knapsack(weights, profits, capacity):
    n = len(profits)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for current_capacity in range(capacity + 1):
            if weights[i - 1] <= current_capacity:
                include_item = (
                    profits[i - 1]
                    + dp[i - 1][current_capacity - weights[i - 1]]
                )
                exclude_item = dp[i - 1][current_capacity]

                dp[i][current_capacity] = max(
                    include_item,
                    exclude_item
                )
            else:
                dp[i][current_capacity] = dp[i - 1][current_capacity]

    return dp[n][capacity]


def main():
    try:
        n = int(input("Enter the number of items: "))

        if n <= 0:
            print("Please enter a positive number of items.")
            return

        weights = []
        profits = []

        print("\nEnter weight and profit for each item:")

        for i in range(n):
            weight = int(input(f"Enter weight of item {i + 1}: "))
            profit = int(input(f"Enter profit of item {i + 1}: "))

            if weight <= 0 or profit < 0:
                print("Invalid weight or profit.")
                return

            weights.append(weight)
            profits.append(profit)

        capacity = int(input("\nEnter knapsack capacity: "))

        if capacity <= 0:
            print("Capacity must be positive.")
            return

        maximum_profit = knapsack(weights, profits, capacity)

        print(f"\nMaximum Profit: {maximum_profit}")

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()