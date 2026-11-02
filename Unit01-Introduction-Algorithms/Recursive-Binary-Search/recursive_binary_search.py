
def recursive_binary_search(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return recursive_binary_search(
            arr, mid + 1, high, target
        )

    else:
        return recursive_binary_search(
            arr, low, mid - 1, target
        )


def main():
    n = int(input("Enter number of elements: "))

    arr = []

    print("Enter elements in sorted order:")

    for i in range(n):
        arr.append(int(input()))

    target = int(input("Enter element to search: "))

    result = recursive_binary_search(
        arr, 0, n - 1, target
    )

    if result == -1:
        print("Element not found")
    else:
        print("Element found at index:", result)


if __name__ == "__main__":
    main()
