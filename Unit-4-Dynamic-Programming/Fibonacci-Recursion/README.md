# Fibonacci Using Recursion

## 1. Aim

To implement the Fibonacci Series using the recursive approach.

## 2. Problem Statement

Given a positive integer `n`, generate the first `n` terms of the Fibonacci Series using recursion.

## 3. Algorithm / Approach

1. Define a recursive function `fibonacci(n)`.
2. If `n` is 0 or 1, return `n`.
3. Otherwise, return the sum of `fibonacci(n - 1)` and `fibonacci(n - 2)`.
4. Take the number of terms as input.
5. Call the recursive function for each term.
6. Display the Fibonacci Series.

## 4. Pseudocode

```text
FUNCTION Fibonacci(n)

    IF n <= 1 THEN
        RETURN n
    END IF

    RETURN Fibonacci(n - 1) + Fibonacci(n - 2)

END FUNCTION


INPUT n

FOR i = 0 TO n - 1
    PRINT Fibonacci(i)
END FOR
```

## 5. Time Complexity

The basic recursive approach has a time complexity of **O(2ⁿ)** because the same Fibonacci values are calculated repeatedly.

## 6. Space Complexity

The space complexity is **O(n)** because of the recursive function call stack.

## 7. Sample Input

```text
Enter the number of terms: 10
```

## 8. Sample Output

```text
Fibonacci Series:
0 1 1 2 3 5 8 13 21 34
```

## 9. Learning Outcomes

- Understood recursion and recursive function calls.
- Implemented the Fibonacci Series using recursion.
- Observed the limitations of repeated calculations in recursive solutions.