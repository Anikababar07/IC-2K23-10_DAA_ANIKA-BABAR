# Unit 1 - Complexity Analysis

## 1. Basic Array Operations

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Display | O(n) | O(1) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |
| Searching | O(n) | O(1) |

## 2. Iterative Binary Search

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Auxiliary Space: O(1)

## 3. Recursive Binary Search

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Auxiliary Space: O(log n)

## 4. Performance Analysis

The performance analyzer compares iterative and recursive Binary Search using different input sizes.

Input sizes:
- 1000
- 5000
- 10000
- 50000
- 100000
- 200000

Experimental results are stored in performance_results.csv.

Performance graph is stored in performance_graph.png.

## 5. Conclusion

Binary Search provides logarithmic average and worst-case time complexity. Iterative Binary Search uses constant auxiliary space, whereas Recursive Binary Search requires additional stack space.