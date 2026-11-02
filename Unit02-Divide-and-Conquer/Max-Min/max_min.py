
def find_max_min(arr, low, high):

    # Case 1: Only one element
    if low == high:
        return arr[low], arr[low]

    # Case 2: Two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2

    # Find maximum and minimum in left half
    left_max, left_min = find_max_min(arr, low, mid)

    # Find maximum and minimum in right half
    right_max, right_min = find_max_min(arr, mid + 1, high)

    # Combine results
    maximum = max(left_max, right_max)
    minimum = min(left_min, right_min)

    return maximum, minimum


def main():
    try:
        n = int(input("Enter number of elements: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

        arr = []

        print("Enter array elements:")

        for i in range(n):
            arr.append(int(input()))

        maximum, minimum = find_max_min(arr, 0, n - 1)

        print("\nArray:", arr)
        print("Maximum element:", maximum)
        print("Minimum element:", minimum)

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()

