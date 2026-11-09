# Unit 06 - Backtracking: Complexity Analysis

## 1. General Backtracking Technique

The algorithm generates all possible binary strings of length n.

- **Time Complexity:** O(2ⁿ)
- **Space Complexity:** O(n)

---

## 2. 4-Queens Problem

The algorithm tries different positions for queens and backtracks when a position is not valid.

- **Time Complexity:** O(N!)
- **Space Complexity:** O(N²)

For this program, N = 4.

---

## 3. 8-Queens Problem

The algorithm recursively places eight queens while checking valid positions.

- **Time Complexity:** O(N!)
- **Space Complexity:** O(N²)

For this program, N = 8.

---

## 4. N-Queens Problem

The algorithm explores possible queen positions using recursion and backtracking.

- **Time Complexity:** O(N!)
- **Space Complexity:** O(N²)

---

## 5. Sum of Subsets

The algorithm explores possible combinations by including or excluding each element.

- **Time Complexity:** O(2ⁿ)
- **Space Complexity:** O(n)

---

# Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| General Backtracking | O(2ⁿ) | O(n) |
| 4-Queens | O(N!) | O(N²) |
| 8-Queens | O(N!) | O(N²) |
| N-Queens | O(N!) | O(N²) |
| Sum of Subsets | O(2ⁿ) | O(n) |

---

# Conclusion

Backtracking algorithms explore multiple possible solutions and undo choices when a path does not lead to a valid solution. Their time complexity can be high because they may explore many possible combinations.