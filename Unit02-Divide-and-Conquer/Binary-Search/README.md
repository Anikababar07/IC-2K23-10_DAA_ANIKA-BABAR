# Binary Search Using Divide and Conquer

## 1. Problem Statement

Implement Binary Search using the Divide and Conquer technique to find a given element in a sorted array.

## 2. Algorithm / Approach

1. Start.
2. Input a sorted array and the target element.
3. Initialize low = 0 and high = n - 1.
4. Calculate the middle index:
   mid = (low + high) // 2
5. If the middle element equals the target, return its index.
6. If the middle element is smaller than the target, recursively search the right half.
7. Otherwise, recursively search the left half.
8. If low becomes greater than high, return -1.
9. Stop.

## 3. Pseudocode

```text
FUNCTION BinarySearch(arr, low, high, target)

    IF low > high THEN
        RETURN -1
    END IF

    mid = (low + high) // 2

    IF arr[mid] == target THEN
        RETURN mid

    ELSE IF arr[mid] < target THEN
        RETURN BinarySearch(arr, mid+1, high, target)

    ELSE
        RETURN BinarySearch(arr, low, mid-1, target)

    END IF

END FUNCTION

START

INPUT n
INPUT sorted array
INPUT target

result = BinarySearch(arr, 0, n-1, target)

IF result == -1 THEN
    PRINT "Element not found"
ELSE
    PRINT "Element found at index", result
END IF

END
```

## 4. Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input sorted array and target/]
    B --> C[low = 0, high = n-1]
    C --> D{low <= high?}
    D -- No --> E[/Print Element Not Found/]
    E --> Z([End])
    D -- Yes --> F[mid = low + high // 2]
    F --> G{arr[mid] == target?}
    G -- Yes --> H[/Print index/]
    H --> Z
    G -- No --> I{arr[mid] < target?}
    I -- Yes --> J[Search right half recursively]
    I -- No --> K[Search left half recursively]
    J --> D
    K --> D
```

## 5. Time Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

## 6. Space Complexity

O(log n) auxiliary space due to recursive function calls.

## 7. Sample Input

```text
Enter number of elements: 6
10
20
30
40
50
60
Enter element to search: 40
```

## 8. Sample Output

```text
Element found at index: 3
```

## 9. Experimental Results

The program was tested with:
- An element present in the array.
- An element absent from the array.
- An unsorted input array.
- Different input sizes.

The program verifies that the input array is sorted before performing Binary Search.

## 10. Learning Outcomes

- Understood the Divide and Conquer technique.
- Implemented recursive Binary Search.
- Learned how to divide a problem into smaller subproblems.
- Analyzed time and space complexity.
- Implemented input validation.