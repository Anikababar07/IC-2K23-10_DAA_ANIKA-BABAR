# Algorithm Performance Analyzer

## Problem Statement

Develop an Algorithm Performance Analyzer to compare theoretical and experimental time complexity of Iterative and Recursive Binary Search algorithms.

## Algorithms Used

1. Iterative Binary Search
2. Recursive Binary Search

## Approach

1. Generate sorted arrays of different input sizes.
2. Execute both searching algorithms.
3. Test Best, Average and Worst cases.
4. Measure execution time using Python's `time.perf_counter()`.
5. Verify the correctness of search results.
6. Store experimental results in a CSV file.
7. Generate a graph comparing algorithm performance.

## Pseudocode

```text
START

DEFINE input sizes

FOR each input size:
    GENERATE sorted array

    FOR each algorithm:
        TEST best case
        TEST average case
        TEST worst case

        MEASURE execution time
        VERIFY search result
        STORE results

SAVE results in CSV file

GENERATE performance graph

DISPLAY completion message

END
```

## Theoretical Complexity Analysis

### Iterative Binary Search

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Space Complexity: O(1)

### Recursive Binary Search

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

Space Complexity: O(log n), due to recursive call stack.

## Experimental Analysis

The program tests the following input sizes:

- 1,000
- 5,000
- 10,000
- 50,000
- 100,000
- 200,000

Execution time is measured for both algorithms under three test cases.

## Experimental Results

The program generates:

- `performance_results.csv` – stores execution time measurements.
- `performance_graph.png` – visualizes the comparison between iterative and recursive Binary Search.

## Theoretical vs Experimental Comparison

Both algorithms have O(log n) average and worst-case time complexity.

The iterative algorithm uses O(1) auxiliary space, whereas the recursive algorithm uses O(log n) stack space.

Actual execution times may vary depending on the system, Python interpreter and runtime environment.

## Learning Outcomes

- Implemented performance measurement using Python.
- Compared iterative and recursive Binary Search.
- Analyzed best, average and worst-case complexity.
- Generated experimental results using CSV.
- Visualized algorithm performance using Matplotlib.
- Compared theoretical and empirical performance.