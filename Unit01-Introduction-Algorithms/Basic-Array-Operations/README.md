# Basic Array Operations

## Problem Statement

Write a program to perform basic operations on an array such as:

- Display
- Insertion
- Deletion
- Searching

## Algorithm

1. Start the program.
2. Input the number of elements.
3. Store the elements in an array.
4. Display a menu with available operations.
5. Perform the selected operation:
   - Display all array elements.
   - Insert an element at a specified position.
   - Delete an element from a specified position.
   - Search for an element using linear search.
6. Repeat the menu until the user selects Exit.
7. Stop the program.

## Pseudocode

```text
START

INPUT number of elements
CREATE array

FOR each element
    INPUT element
    ADD element to array

REPEAT
    DISPLAY menu
    INPUT choice

    IF choice = 1
        DISPLAY array

    ELSE IF choice = 2
        INPUT element and position
        INSERT element at position

    ELSE IF choice = 3
        INPUT position
        DELETE element from position

    ELSE IF choice = 4
        INPUT element
        SEARCH element in array

    ELSE IF choice = 5
        EXIT program

UNTIL choice = 5

END
```

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Display | O(n) |
| Insertion | O(n) |
| Deletion | O(n) |
| Searching | O(n) |

## Space Complexity

**O(n)** for storing the array elements.

## Sample Output

```text
Enter the number of elements: 5
Enter the array elements:
10
20
30
40
50

----- ARRAY OPERATIONS MENU -----
1. Display Array
2. Insert Element
3. Delete Element
4. Search Element
5. Exit
```

## Learning Outcomes

- Learned basic array operations.
- Implemented insertion and deletion operations.
- Implemented linear search.
- Analyzed the time complexity of array operations.
- Practiced modular programming using Python functions.