# Recursive Binary Search

## Problem Statement
Implement Binary Search using recursion to find a given element in a sorted array.

## Algorithm
1. Start.
2. Initialize low = 0 and high = n-1.
3. If low > high, return -1.
4. Calculate mid = (low + high) // 2.
5. If arr[mid] equals target, return mid.
6. If arr[mid] is smaller than target, recursively search the right half.
7. Otherwise, recursively search the left half.
8. Return the result.
9. Stop.

## Pseudocode

```text
BINARY_SEARCH(arr, low, high, target)

IF low > high:
    RETURN -1

mid = (low + high) // 2

IF arr[mid] == target:
    RETURN mid

ELSE IF arr[mid] < target:
    RETURN BINARY_SEARCH(arr, mid+1, high, target)

ELSE:
    RETURN BINARY_SEARCH(arr, low, mid-1, target)
```

## Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

## Space Complexity
O(log n) auxiliary space due to recursive function calls.

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
- Understanding recursion.
- Implementing recursive Binary Search.
- Understanding recursive function calls.
- Comparing iterative and recursive searching.