# Unit 07 - NP-Hard, NP-Complete & Advanced Optimization: Algorithm Flowcharts

## 1. Exhaustive Search

```text
Start
  |
Input List
  |
Set First Element as Largest
  |
Check Next Element
  |
Is It Greater?
 / \
Yes  No
 |     |
Update  Continue
Largest  |
   \____/
      |
All Elements Checked?
 / \
No   Yes
 |      |
Repeat Display Result
          |
         End
```

---

## 2. 0/1 Knapsack using Branch and Bound

```text
Start
  |
Create Root Node
  |
Select Next Item
  |
Include Item
  |
Within Capacity?
 / \
No   Yes
 |      |
Prune  Calculate Bound
        |
Promising?
 / \
No   Yes
 |      |
Prune Add to Queue
        |
Try Next Item
        |
       End
```

---

## 3. TSP using Branch and Bound

```text
Start
  |
Select Starting City
  |
Visit Next City
  |
Calculate Path Cost
  |
Calculate Lower Bound
  |
Promising Path?
 / \
No   Yes
 |      |
Prune Continue
        |
All Cities Visited?
 / \
No   Yes
 |      |
Repeat Return to Start
           |
      Update Minimum Cost
           |
          End
```

---

## 4. Knapsack Comparison

```text
Start
  |
Input Weights, Profits and Capacity
  |
Run Dynamic Programming
  |
Store Result and Time
  |
Run Branch and Bound
  |
Store Result and Time
  |
Compare Results
  |
Display Comparison
  |
End
```

---

## 5. TSP Comparison

```text
Start
  |
Input Distance Matrix
  |
Run Dynamic Programming
  |
Store Result and Time
  |
Run Branch and Bound
  |
Store Result and Time
  |
Compare Results
  |
Display Comparison
  |
End
```

---

# Conclusion

These flowcharts represent the main workflow of the exhaustive search, Branch and Bound, and algorithm comparison programs implemented in Unit 07.