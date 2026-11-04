# Unit 2 - Divide and Conquer: Complexity Analysis

This document presents the time and space complexity analysis of all algorithms implemented in Unit 2.

---

## 1. Binary Search

Binary Search repeatedly divides a sorted array into two halves.

| Case | Time Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

**Space Complexity:** O(log n) for the recursive implementation.

---

## 2. Maximum and Minimum

The Divide and Conquer approach divides the array into smaller subarrays and combines their maximum and minimum values.

**Recurrence Relation:**

```text
T(n) = 2T(n/2) + O(1)
```

| Case | Time Complexity |
|---|---|
| Best Case | O(n) |
| Average Case | O(n) |
| Worst Case | O(n) |

**Space Complexity:** O(log n) due to the recursive call stack.

---

## 3. Merge Sort

Merge Sort divides the array into two halves, recursively sorts both halves, and merges them.

**Recurrence Relation:**

```text
T(n) = 2T(n/2) + O(n)
```

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

**Space Complexity:** O(n) for temporary arrays.

---

## 4. Quick Sort

Quick Sort partitions the array around a pivot and recursively sorts the two subarrays.

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

**Space Complexity:**

- Best/Average Case: O(log n) recursion stack.
- Worst Case: O(n) recursion stack.

---

## 5. Heap Sort

Heap Sort builds a Max Heap and repeatedly extracts the maximum element.

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

**Space Complexity:** O(log n) for this implementation because `heapify()` uses recursion. The algorithm performs sorting in-place.

---

## 6. Strassen Matrix Multiplication

Strassen's algorithm divides two matrices into four submatrices and performs seven recursive matrix multiplications.

**Recurrence Relation:**

```text
T(n) = 7T(n/2) + O(n²)
```

Using the Master Theorem:

```text
T(n) = O(n^log₂7)
```

Therefore:

```text
Time Complexity ≈ O(n^2.807)
```

| Case | Time Complexity |
|---|---|
| Best Case | O(n^2.807) |
| Average Case | O(n^2.807) |
| Worst Case | O(n^2.807) |

**Space Complexity:** O(n²) additional space for submatrices and intermediate results.

---

# Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|---|---|---|---|---|
| Binary Search | O(1) | O(log n) | O(log n) | O(log n) |
| Max-Min | O(n) | O(n) | O(n) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) average |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(log n) |
| Strassen Matrix Multiplication | O(n^2.807) | O(n^2.807) | O(n^2.807) | O(n²) |

# Conclusion

The complexity analysis shows how different Divide and Conquer algorithms perform based on input size and problem structure. Binary Search is highly efficient for searching sorted data, while Merge Sort and Heap Sort provide consistent O(n log n) sorting performance. Quick Sort has an efficient average case but can degrade to O(n²). Strassen's algorithm improves the asymptotic performance of matrix multiplication compared with the conventional O(n³) approach.