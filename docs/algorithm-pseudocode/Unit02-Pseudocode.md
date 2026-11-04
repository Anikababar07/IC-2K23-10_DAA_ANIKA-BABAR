# Unit 2 - Divide and Conquer: Algorithm Pseudocode

## 1. Binary Search

```text
FUNCTION BinarySearch(arr, low, high, target)

    IF low > high THEN
        RETURN -1
    END IF

    mid = (low + high) // 2

    IF arr[mid] == target THEN
        RETURN mid
    ELSE IF arr[mid] < target THEN
        RETURN BinarySearch(arr, mid + 1, high, target)
    ELSE
        RETURN BinarySearch(arr, low, mid - 1, target)
    END IF

END FUNCTION
```

---

## 2. Maximum and Minimum

```text
FUNCTION FindMaxMin(arr, low, high)

    IF low == high THEN
        RETURN arr[low], arr[low]
    END IF

    IF high == low + 1 THEN
        IF arr[low] > arr[high] THEN
            RETURN arr[low], arr[high]
        ELSE
            RETURN arr[high], arr[low]
        END IF
    END IF

    mid = (low + high) // 2

    leftMax, leftMin = FindMaxMin(arr, low, mid)
    rightMax, rightMin = FindMaxMin(arr, mid + 1, high)

    maximum = MAX(leftMax, rightMax)
    minimum = MIN(leftMin, rightMin)

    RETURN maximum, minimum

END FUNCTION
```

---

## 3. Merge Sort

```text
FUNCTION MergeSort(arr, left, right)

    IF left < right THEN

        mid = (left + right) // 2

        MergeSort(arr, left, mid)
        MergeSort(arr, mid + 1, right)

        Merge(arr, left, mid, right)

    END IF

END FUNCTION


FUNCTION Merge(arr, left, mid, right)

    Create left and right temporary arrays

    Compare elements from both arrays

    Copy the smaller element into the original array

    Copy remaining elements

END FUNCTION
```

---

## 4. Quick Sort

```text
FUNCTION QuickSort(arr, low, high)

    IF low < high THEN

        pivotIndex = Partition(arr, low, high)

        QuickSort(arr, low, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, high)

    END IF

END FUNCTION


FUNCTION Partition(arr, low, high)

    pivot = arr[high]
    i = low - 1

    FOR j = low TO high - 1

        IF arr[j] <= pivot THEN
            i = i + 1
            SWAP arr[i] and arr[j]
        END IF

    END FOR

    SWAP arr[i + 1] and arr[high]

    RETURN i + 1

END FUNCTION
```

---

## 5. Heap Sort

```text
FUNCTION HeapSort(arr)

    n = length(arr)

    FOR i = n/2 - 1 DOWNTO 0
        Heapify(arr, n, i)
    END FOR

    FOR i = n - 1 DOWNTO 1

        SWAP arr[0] and arr[i]

        Heapify(arr, i, 0)

    END FOR

END FUNCTION


FUNCTION Heapify(arr, n, root)

    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    IF left < n AND arr[left] > arr[largest] THEN
        largest = left
    END IF

    IF right < n AND arr[right] > arr[largest] THEN
        largest = right
    END IF

    IF largest != root THEN
        SWAP arr[root] and arr[largest]
        Heapify(arr, n, largest)
    END IF

END FUNCTION
```

---

## 6. Strassen Matrix Multiplication

```text
FUNCTION Strassen(A, B)

    n = size of matrix

    IF n == 1 THEN
        RETURN A[0][0] * B[0][0]
    END IF

    Divide A into A11, A12, A21, A22
    Divide B into B11, B12, B21, B22

    M1 = (A11 + A22) × (B11 + B22)
    M2 = (A21 + A22) × B11
    M3 = A11 × (B12 - B22)
    M4 = A22 × (B21 - B11)
    M5 = (A11 + A12) × B22
    M6 = (A21 - A11) × (B11 + B12)
    M7 = (A12 - A22) × (B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    Combine C11, C12, C21 and C22

    RETURN result

END FUNCTION
```

---

## Conclusion

This document contains the language-independent pseudocode for all six algorithms implemented in Unit 2 using Divide and Conquer and related algorithmic techniques.