def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    try:
        n = int(input("Enter the number of terms: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        print("\nFibonacci Series:")

        for i in range(n):
            print(fibonacci(i), end=" ")

        print()

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()