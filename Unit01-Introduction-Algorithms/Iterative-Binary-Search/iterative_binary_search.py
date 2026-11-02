def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    n = int(input("Enter the number of elements: "))

    arr = []
    print("Enter elements in sorted order:")

    for i in range(n):
        element = int(input())
        arr.append(element)

    target = int(input("Enter the element to search: "))

    result = iterative_binary_search(arr, target)

    if result == -1:
        print("Element not found.")
    else:
        print(f"Element found at index {result}.")


if __name__ == "__main__":
    main()