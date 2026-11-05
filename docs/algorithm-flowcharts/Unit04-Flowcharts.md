# Unit 4 - Dynamic Programming: Algorithm Flowcharts

## 1. Fibonacci Using Recursion

```mermaid
flowchart TD
    A([Start]) --> B[/Input number of terms n/]
    B --> C[Call Fibonacci function]
    C --> D{n <= 1?}
    D -- Yes --> E[Return n]
    D -- No --> F[Return Fibonacci n-1 + Fibonacci n-2]
    E --> G[/Display Fibonacci result/]
    F --> G
    G --> H([End])
```

---

## 2. Fibonacci Using Memoization

```mermaid
flowchart TD
    A([Start]) --> B[/Input number of terms n/]
    B --> C[Create memo array]
    C --> D[Call Fibonacci function]
    D --> E{n <= 1?}
    E -- Yes --> F[Return n]
    E -- No --> G{Value already in memo?}
    G -- Yes --> H[Return stored value]
    G -- No --> I[Calculate Fibonacci n-1 + Fibonacci n-2]
    I --> J[Store result in memo]
    J --> K[Return result]
    F --> L[/Display Fibonacci series/]
    H --> L
    K --> L
    L --> M([End])
```

---

## 3. 0/1 Knapsack

```mermaid
flowchart TD
    A([Start]) --> B[/Input items, weights, profits and capacity/]
    B --> C[Create DP table]
    C --> D[Initialize table with 0]
    D --> E{More items?}
    E -- Yes --> F{Item weight <= current capacity?}
    F -- Yes --> G[Calculate include and exclude values]
    G --> H[Store maximum value]
    F -- No --> I[Copy value from previous row]
    H --> J[Move to next capacity/item]
    I --> J
    J --> E
    E -- No --> K[/Display maximum profit/]
    K --> L([End])
```

---

## 4. Multistage Graph

```mermaid
flowchart TD
    A([Start]) --> B[Initialize graph and cost array]
    B --> C[Set destination cost to 0]
    C --> D[Process vertices from right to left]
    D --> E{More adjacent vertices?}
    E -- Yes --> F[Calculate path cost]
    F --> G{New cost is smaller?}
    G -- Yes --> H[Update minimum cost and path]
    G -- No --> E
    H --> E
    E -- No --> I[Move to previous vertex]
    I --> J{All vertices processed?}
    J -- No --> D
    J -- Yes --> K[/Display minimum cost and shortest path/]
    K --> L([End])
```

---

## 5. Floyd-Warshall Algorithm

```mermaid
flowchart TD
    A([Start]) --> B[Initialize distance matrix]
    B --> C[Select intermediate vertex k]
    C --> D[Select source vertex i]
    D --> E[Select destination vertex j]
    E --> F{Path through k is shorter?}
    F -- Yes --> G[Update distance i to j]
    F -- No --> H[Keep existing distance]
    G --> I{More destination vertices?}
    H --> I
    I -- Yes --> E
    I -- No --> J{More source vertices?}
    J -- Yes --> D
    J -- No --> K{More intermediate vertices?}
    K -- Yes --> C
    K -- No --> L[/Display shortest distance matrix/]
    L --> M([End])
```

---

## 6. Single-Source Shortest Path (Dijkstra's Algorithm)

```mermaid
flowchart TD
    A([Start]) --> B[Initialize all distances to infinity]
    B --> C[Set source distance to 0]
    C --> D[Add source to priority queue]
    D --> E{Priority queue empty?}
    E -- No --> F[Remove vertex with minimum distance]
    F --> G{Distance entry outdated?}
    G -- Yes --> E
    G -- No --> H[Check all neighboring vertices]
    H --> I{New distance is shorter?}
    I -- Yes --> J[Update distance and add to queue]
    I -- No --> H
    J --> H
    H --> E
    E -- Yes --> K[/Display shortest distances/]
    K --> L([End])
```

---

## 7. Traveling Salesperson Problem

```mermaid
flowchart TD
    A([Start]) --> B[Start from city 0]
    B --> C[Mark starting city as visited]
    C --> D{All cities visited?}
    D -- Yes --> E[Return cost to starting city]
    D -- No --> F[Select an unvisited city]
    F --> G[Calculate travel cost recursively]
    G --> H[Store result using memoization]
    H --> I[Choose minimum cost]
    I --> D
    E --> J[/Display minimum tour cost/]
    J --> K([End])
```

---

## Conclusion

These flowcharts represent the working process of all algorithms implemented in Unit 4 using Dynamic Programming.