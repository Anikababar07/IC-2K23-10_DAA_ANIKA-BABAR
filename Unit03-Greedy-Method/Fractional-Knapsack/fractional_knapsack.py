def fractional_knapsack(items, capacity):
    # Sort items according to profit-to-weight ratio
    items.sort(key=lambda item: item[0] / item[1], reverse=True)

    total_profit = 0.0
    selected_items = []

    for profit, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            capacity -= weight
            total_profit += profit
            selected_items.append((profit, weight, 1.0))
        else:
            fraction = capacity / weight
            total_profit += profit * fraction
            selected_items.append((profit, weight, fraction))
            capacity = 0

    return total_profit, selected_items


def main():
    try:
        n = int(input("Enter number of items: "))

        if n <= 0:
            print("Please enter a positive number of items.")
            return

        items = []

        for i in range(n):
            print(f"\nItem {i + 1}")
            profit = float(input("Enter profit: "))
            weight = float(input("Enter weight: "))

            if weight <= 0:
                print("Weight must be greater than zero.")
                return

            items.append((profit, weight))

        capacity = float(input("\nEnter knapsack capacity: "))

        if capacity <= 0:
            print("Capacity must be greater than zero.")
            return

        total_profit, selected_items = fractional_knapsack(
            items, capacity
        )

        print("\nSelected Items:")
        for i, (profit, weight, fraction) in enumerate(
            selected_items, start=1
        ):
            print(
                f"Item {i}: Profit = {profit}, "
                f"Weight = {weight}, "
                f"Fraction Taken = {fraction:.2f}"
            )

        print(f"\nMaximum Profit: {total_profit:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    main()