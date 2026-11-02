# Unit 1 - Algorithm Pseudocode

## 1. Basic Array Operations

**Problem:** Perform display, insertion, deletion and searching operations on an array.

### Pseudocode

```text
START

INPUT n
CREATE empty array

FOR i = 0 TO n-1
    INPUT element
    INSERT element into array
END FOR

REPEAT

    DISPLAY "1. Display Array"
    DISPLAY "2. Insert Element"
    DISPLAY "3. Delete Element"
    DISPLAY "4. Search Element"
    DISPLAY "5. Exit"

    INPUT choice

    IF choice = 1 THEN
        DISPLAY array

    ELSE IF choice = 2 THEN
        INPUT element
        INPUT position

        IF position >= 0 AND position <= length(array) THEN
            INSERT element at position
        ELSE
            DISPLAY "Invalid position"
        END IF

    ELSE IF choice = 3 THEN
        INPUT position

        IF position >= 0 AND position < length(array) THEN
            DELETE element at position
        ELSE
            DISPLAY "Invalid position"
        END IF

    ELSE IF choice = 4 THEN
        INPUT target
        SET found = FALSE

        FOR i = 0 TO length(array)-1
            IF array[i] = target THEN
                DISPLAY "Element found at index", i
                SET found = TRUE
                BREAK
            END IF
        END FOR

        IF found = FALSE THEN
            DISPLAY "Element not found"
        END IF

    ELSE IF choice = 5 THEN
        DISPLAY "Program terminated"

    ELSE
        DISPLAY "Invalid choice"
    END IF

UNTIL choice = 5

END
```

---

## 2. Iterative Binary Search

**Problem:** Search for an element in a sorted array using an iterative approach.

### Pseudocode

```text
START

INPUT sorted array
INPUT target

SET low = 0
SET high = n - 1

WHILE low <= high

    SET mid = (low + high) // 2

    IF array[mid] = target THEN
        RETURN mid

    ELSE IF array[mid] < target THEN
        SET low = mid + 1

    ELSE
        SET high = mid - 1

    END IF

END WHILE

RETURN -1

END
```

---

## 3. Recursive Binary Search

**Problem:** Search for an element in a sorted array using recursion.

### Pseudocode

```text
FUNCTION BinarySearch(array, low, high, target)

    IF low > high THEN
        RETURN -1
    END IF

    SET mid = (low + high) // 2

    IF array[mid] = target THEN
        RETURN mid

    ELSE IF array[mid] < target THEN
        RETURN BinarySearch(array, mid+1, high, target)

    ELSE
        RETURN BinarySearch(array, low, mid-1, target)

    END IF

END FUNCTION

START

INPUT sorted array
INPUT target

SET result = BinarySearch(array, 0, n-1, target)

IF result = -1 THEN
    DISPLAY "Element not found"
ELSE
    DISPLAY "Element found at index", result
END IF

END
```

---

## Conclusion

The pseudocode describes the logical steps of three algorithms implemented in Unit 1. It provides a language-independent representation of their working and helps in understanding algorithm design.