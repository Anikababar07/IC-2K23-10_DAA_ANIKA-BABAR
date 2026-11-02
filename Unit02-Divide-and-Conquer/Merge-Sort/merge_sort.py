
def merge(arr, left, mid, right):
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


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

        merge_sort(arr, 0, n - 1)

        print("Sorted Array:", arr)

    except ValueError:
        print("Invalid input! Enter integers only.")


if __name__ == "__main__":
    main()
