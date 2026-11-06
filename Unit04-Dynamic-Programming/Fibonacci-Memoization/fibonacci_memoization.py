def fibonacci(n, memo):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


def main():
    try:
        n = int(input("Enter the number of terms: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        memo = [-1] * n

        print("\nFibonacci Series using Memoization:")

        for i in range(n):
            print(fibonacci(i, memo), end=" ")

        print()

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()