# Unit 07 - NP-Hard, NP-Complete & Advanced Optimization: Complexity Analysis

## 1. Exhaustive Search

The program checks every element in the list.

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## 2. 0/1 Knapsack using Branch and Bound

In the worst case, the algorithm may explore all possible subsets.

- **Time Complexity:** O(2ⁿ)
- **Space Complexity:** O(2ⁿ)

---

## 3. TSP using Branch and Bound

The worst-case scenario may explore all possible tours.

- **Time Complexity:** O(n!)
- **Space Complexity:** O(n²)

---

## 4. 0/1 Knapsack Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Dynamic Programming | O(n × W) | O(n × W) |
| Branch and Bound | O(2ⁿ) worst case | O(n) |

Where `W` is the knapsack capacity.

---

## 5. TSP Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Dynamic Programming | O(n² × 2ⁿ) | O(n × 2ⁿ) |
| Branch and Bound | O(n!) worst case | O(n²) |

---

# Conclusion

Dynamic Programming solves problems by storing intermediate results, while Branch and Bound reduces unnecessary search by pruning non-promising solutions.