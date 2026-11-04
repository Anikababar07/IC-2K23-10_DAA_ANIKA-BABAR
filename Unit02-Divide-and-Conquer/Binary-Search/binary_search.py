
def binary_search(arr, low, high, target):

    # Base condition: element not found
    if low > high:
        return -1

    # Find middle element
    mid = (low + high) // 2

    # Element found
    if arr[mid] == target:
        return mid

    # Search right half
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    # Search left half
    else:
        return binary_search(arr, low, mid - 1, target)


def main():
    try:
        n = int(input("Enter number of elements: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        arr = []

        print("Enter elements in sorted ascending order:")

        for i in range(n):
            element = int(input())
            arr.append(element)

        # Validate sorted array
        if arr != sorted(arr):
            print("Error: Array must be sorted in ascending order.")
            return

        target = int(input("Enter element to search: "))

        result = binary_search(arr, 0, n - 1, target)

        if result == -1:
            print("Element not found.")
        else:
            print("Element found at index:", result)

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
