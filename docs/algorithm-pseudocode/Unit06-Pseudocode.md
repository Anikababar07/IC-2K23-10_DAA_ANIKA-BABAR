# Unit 06 - Backtracking: Algorithm Pseudocode

## 1. General Backtracking Technique

```text
FUNCTION GenerateBinaryStrings(n, current)

    IF length of current equals n THEN
        DISPLAY current
        RETURN
    END IF

    CALL GenerateBinaryStrings(n, current + "0")
    CALL GenerateBinaryStrings(n, current + "1")

END FUNCTION
```

---

## 2. 4-Queens Problem

```text
FUNCTION SolveQueens(board, row)

    IF row equals 4 THEN
        DISPLAY the board
        RETURN TRUE
    END IF

    FOR each column in the current row
        IF position is safe THEN
            PLACE queen at the position

            IF SolveQueens(board, row + 1) is TRUE THEN
                RETURN TRUE
            END IF

            REMOVE queen from the position
        END IF
    END FOR

    RETURN FALSE

END FUNCTION
```

---

## 3. 8-Queens Problem

```text
FUNCTION SolveQueens(board, row)

    IF row equals 8 THEN
        RETURN TRUE
    END IF

    FOR each column in the current row
        IF position is safe THEN
            PLACE queen

            IF SolveQueens(board, row + 1) is TRUE THEN
                RETURN TRUE
            END IF

            REMOVE queen
        END IF
    END FOR

    RETURN FALSE

END FUNCTION
```

---

## 4. N-Queens Problem

```text
FUNCTION SolveNQueens(board, row, n)

    IF row equals n THEN
        RETURN TRUE
    END IF

    FOR each column from 0 to n - 1
        IF position is safe THEN
            PLACE queen at current position

            IF SolveNQueens(board, row + 1, n) is TRUE THEN
                RETURN TRUE
            END IF

            REMOVE queen from current position
        END IF
    END FOR

    RETURN FALSE

END FUNCTION
```

---

## 5. Sum of Subsets

```text
FUNCTION FindSubsets(numbers, target, index, subset, currentSum)

    IF currentSum equals target THEN
        DISPLAY subset
        RETURN
    END IF

    IF currentSum is greater than target OR index equals number of elements THEN
        RETURN
    END IF

    INCLUDE numbers[index] in subset
    CALL FindSubsets with next index

    EXCLUDE numbers[index] from subset
    CALL FindSubsets with next index

END FUNCTION
```

---

# Conclusion

This document contains the pseudocode for the Backtracking algorithms implemented in Unit 06.