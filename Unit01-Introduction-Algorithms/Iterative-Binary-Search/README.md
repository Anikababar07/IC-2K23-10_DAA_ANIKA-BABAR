# Iterative Binary Search

## Problem Statement
Implement Binary Search using an iterative approach to find a given element in a sorted array.

## Algorithm
1. Start.
2. Initialize low = 0 and high = n-1.
3. Calculate mid = (low + high) // 2.
4. Compare the middle element with the target.
5. If equal, return the index.
6. If the middle element is smaller, search the right half.
7. Otherwise, search the left half.
8. Repeat until the element is found or low becomes greater than high.
9. Return -1 if the element is not found.
10. Stop.

## Pseudocode

```text
START
INPUT sorted array and target
low = 0
high = n - 1

WHILE low <= high:
    mid = (low + high) // 2

    IF arr[mid] == target:
        RETURN mid

    ELSE IF arr[mid] < target:
        low = mid + 1

    ELSE:
        high = mid - 1

RETURN -1
END
```

## Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

## Space Complexity
O(1) auxiliary space.

## Sample Input

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

## Sample Output

```text
Element found at index: 3
```

## Learning Outcomes
- Understanding Binary Search.
- Implementing iterative searching.
- Understanding time and space complexity.
- Working with sorted arrays.