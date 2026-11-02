
def heapify(arr, n, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Check whether the left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check whether the right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def main():
    try:
        arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

        if not arr:
            print("Please enter at least one number.")
            return

        print("Original Array:", arr)
        sorted_arr = heap_sort(arr)
        print("Sorted Array:", sorted_arr)

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
