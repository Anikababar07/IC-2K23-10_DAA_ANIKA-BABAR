def display_array(arr):
    print("Array elements:", arr)


def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        print("Invalid position!")
    else:
        arr.insert(position, element)
        print("Element inserted successfully.")


def delete_element(arr, position):
    if position < 0 or position >= len(arr):
        print("Invalid position!")
    else:
        deleted_element = arr.pop(position)
        print("Deleted element:", deleted_element)


def search_element(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


def main():
    arr = []

    n = int(input("Enter the number of elements: "))

    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        arr.append(element)

    while True:
        print("\n----- ARRAY OPERATIONS MENU -----")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Search Element")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_array(arr)

        elif choice == 2:
            element = int(input("Enter element to insert: "))
            position = int(input("Enter position (starting from 0): "))
            insert_element(arr, element, position)

        elif choice == 3:
            position = int(input("Enter position to delete (starting from 0): "))
            delete_element(arr, position)

        elif choice == 4:
            element = int(input("Enter element to search: "))
            position = search_element(arr, element)

            if position == -1:
                print("Element not found.")
            else:
                print("Element found at index:", position)

        elif choice == 5:
            print("Program exited successfully.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()