# Unit 3 - Greedy Method: Algorithm Flowcharts

## 1. Fractional Knapsack

```mermaid
flowchart TD
    A([Start]) --> B[/Input items, profits, weights and capacity/]
    B --> C[Calculate profit-to-weight ratio]
    C --> D[Sort items by decreasing ratio]
    D --> E{Items remaining and capacity available?}
    E -- Yes --> F{Complete item fits?}
    F -- Yes --> G[Add complete item]
    F -- No --> H[Add required fraction of item]
    G --> I[Update capacity and total profit]
    H --> I
    I --> E
    E -- No --> J[/Display maximum profit/]
    J --> K([End])
```

---

## 2. Job Sequencing with Deadlines

```mermaid
flowchart TD
    A([Start]) --> B[/Input jobs, deadlines and profits/]
    B --> C[Sort jobs by decreasing profit]
    C --> D[Find maximum deadline]
    D --> E[Create empty time slots]
    E --> F{More jobs available?}
    F -- Yes --> G[Select next highest-profit job]
    G --> H{Free slot available before deadline?}
    H -- Yes --> I[Schedule job in latest available slot]
    H -- No --> J[Skip job]
    I --> F
    J --> F
    F -- No --> K[/Display scheduled jobs and maximum profit/]
    K --> L([End])
```

---

## 3. Prim's Algorithm

```mermaid
flowchart TD
    A([Start]) --> B[/Input vertices and weighted edges/]
    B --> C[Select starting vertex]
    C --> D[Add starting vertex to priority queue]
    D --> E{Priority queue empty?}
    E -- No --> F[Select minimum-weight edge]
    F --> G{Vertex already visited?}
    G -- Yes --> E
    G -- No --> H[Add edge to MST]
    H --> I[Mark vertex as visited]
    I --> J[Add unvisited neighbors to priority queue]
    J --> E
    E -- Yes --> K{All vertices visited?}
    K -- Yes --> L[/Display MST and total cost/]
    K -- No --> M[Graph is disconnected]
    L --> N([End])
    M --> N
```

---

## 4. Kruskal's Algorithm

```mermaid
flowchart TD
    A([Start]) --> B[/Input vertices and weighted edges/]
    B --> C[Sort all edges by increasing weight]
    C --> D[Create Disjoint Set]
    D --> E{More edges available?}
    E -- Yes --> F[Select minimum-weight edge]
    F --> G{Does edge create a cycle?}
    G -- Yes --> H[Discard edge]
    G -- No --> I[Add edge to MST and union sets]
    H --> J{MST has V - 1 edges?}
    I --> J
    J -- Yes --> K[/Display MST and total cost/]
    J -- No --> E
    E -- No --> L[Graph is disconnected]
    K --> M([End])
    L --> M
```

---

## Conclusion

These flowcharts represent the working process of all algorithms implemented in Unit 3 using the Greedy Method.