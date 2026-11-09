# Unit 06 - Backtracking: Algorithm Flowcharts

## 1. General Backtracking Technique

```text
Start
  |
Create Current Solution
  |
Is Solution Complete?
 / \
Yes  No
 |     |
Display Try Next Choice
       |
       Backtrack
          |
       Repeat
```

---

## 2. 4-Queens Problem

```text
Start
  |
Create 4 × 4 Chessboard
  |
Try to Place Queen
  |
Is Position Safe?
 / \
No  Yes
 |     |
Try Next Place Queen
Column     |
          |
    Next Row
          |
  All Queens Placed?
       / \
     Yes  No
      |     |
 Display    Backtrack
 Solution     |
      \______/
         |
        End
```

---

## 3. 8-Queens Problem

```text
Start
  |
Create 8 × 8 Chessboard
  |
Try Safe Position
  |
Place Queen
  |
Move to Next Row
  |
All 8 Queens Placed?
 / \
Yes  No
 |     |
Display Backtrack
Solution   |
    \_____/
       |
      End
```

---

## 4. N-Queens Problem

```text
Start
  |
Input N
  |
Create N × N Board
  |
Try Safe Position
  |
Place Queen
  |
Move to Next Row
  |
All Queens Placed?
 / \
Yes  No
 |     |
Display Backtrack
Solution   |
    \_____/
       |
      End
```

---

## 5. Sum of Subsets

```text
Start
  |
Select an Element
  |
Include Element
  |
Is Target Sum Reached?
 / \
Yes  No
 |     |
Display Try Next Element
Subset    |
     \____/
        |
   Also Try Excluding Element
        |
      Backtrack
        |
       End
```

---

# Conclusion

These flowcharts represent the basic decision-making and backtracking process used in the algorithms implemented in Unit 06.