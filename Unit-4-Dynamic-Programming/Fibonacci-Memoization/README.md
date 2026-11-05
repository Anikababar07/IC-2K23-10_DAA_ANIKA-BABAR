# Fibonacci Using Memoization

## 1. Aim

To implement the Fibonacci Series using recursion with memoization.

## 2. Problem Statement

Given a positive integer `n`, generate the first `n` terms of the Fibonacci Series using memoization to avoid repeated calculations.

## 3. Algorithm / Approach

1. Create a memoization array initialized with `-1`.
2. Define a recursive function `fibonacci(n, memo)`.
3. If `n` is 0 or 1, return `n`.
4. If the value is already stored in the memo array, return the stored value.
5. Otherwise, calculate the Fibonacci value recursively.
6. Store the calculated value in the memo array.
7. Display the first `n` Fibonacci terms.

## 4. Pseudocode

```text
FUNCTION Fibonacci(n, memo)

    IF n <= 1 THEN
        RETURN n
    END IF

    IF memo[n] is already calculated THEN
        RETURN memo[n]
    END IF

    memo[n] = Fibonacci(n - 1, memo) + Fibonacci(n - 2, memo)

    RETURN memo[n]

END FUNCTION


INPUT n

Create memo array of size n

FOR i = 0 TO n - 1
    PRINT Fibonacci(i, memo)
END FOR
```

## 5. Time Complexity

With memoization, each Fibonacci value is calculated only once.

**Time Complexity: O(n)**

## 6. Space Complexity

**O(n)** for the memoization array and recursive call stack.

## 7. Sample Input

```text
Enter the number of terms: 10
```

## 8. Sample Output

```text
Fibonacci Series using Memoization:
0 1 1 2 3 5 8 13 21 34
```

## 9. Learning Outcomes

- Understood the concept of Dynamic Programming.
- Implemented memoization to store previously calculated values.
- Compared recursive computation with optimized memoized computation.
- Reduced repeated calculations and improved efficiency.