
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


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

        print("Original Array:", arr)

        quick_sort(arr, 0, n - 1)

        print("Sorted Array:", arr)

    except ValueError:
        print("Invalid input! Enter integers only.")


if __name__ == "__main__":
    main()
