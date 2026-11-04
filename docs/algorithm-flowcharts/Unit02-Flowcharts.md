# Unit 2 - Divide and Conquer: Algorithm Flowcharts

## 1. Binary Search

```mermaid
flowchart TD
    A([Start]) --> B[/Input sorted array and target/]
    B --> C[Set low = 0 and high = n - 1]
    C --> D{low <= high?}
    D -- No --> E[Return -1]
    D -- Yes --> F[Calculate mid]
    F --> G{arr[mid] equals target?}
    G -- Yes --> H[Return mid]
    G -- No --> I{arr[mid] < target?}
    I -- Yes --> J[Search right half recursively]
    I -- No --> K[Search left half recursively]
    J --> D
    K --> D
```

## 2. Maximum and Minimum

```mermaid
flowchart TD
    A([Start]) --> B[/Input array/]
    B --> C{One element?}
    C -- Yes --> D[Return element as Max and Min]
    C -- No --> E{Two elements?}
    E -- Yes --> F[Compare elements and return Max and Min]
    E -- No --> G[Divide array into two halves]
    G --> H[Find Max and Min in left half]
    G --> I[Find Max and Min in right half]
    H --> J[Combine results]
    I --> J
    J --> K[/Display Maximum and Minimum/]
    D --> K
    F --> K
    K --> L([End])
```

## 3. Merge Sort

```mermaid
flowchart TD
    A([Start]) --> B[/Input array/]
    B --> C{Array has more than one element?}
    C -- No --> D[Return]
    C -- Yes --> E[Divide array into two halves]
    E --> F[Sort left half recursively]
    E --> G[Sort right half recursively]
    F --> H[Merge sorted halves]
    G --> H
    H --> I[/Display sorted array/]
    I --> J([End])
```

## 4. Quick Sort

```mermaid
flowchart TD
    A([Start]) --> B[/Input array/]
    B --> C{low < high?}
    C -- No --> D[Return]
    C -- Yes --> E[Select pivot]
    E --> F[Partition array]
    F --> G[Sort left subarray recursively]
    G --> H[Sort right subarray recursively]
    H --> I[/Display sorted array/]
    I --> J([End])
```

## 5. Heap Sort

```mermaid
flowchart TD
    A([Start]) --> B[/Input array/]
    B --> C[Build Max Heap]
    C --> D{Heap size > 1?}
    D -- Yes --> E[Swap root with last element]
    E --> F[Reduce heap size]
    F --> G[Heapify root]
    G --> D
    D -- No --> H[/Display sorted array/]
    H --> I([End])
```

## 6. Strassen Matrix Multiplication

```mermaid
flowchart TD
    A([Start]) --> B[/Input two square matrices/]
    B --> C[Pad matrices if required]
    C --> D{Matrix size = 1?}
    D -- Yes --> E[Multiply elements]
    D -- No --> F[Divide matrices into four submatrices]
    F --> G[Calculate seven recursive products]
    G --> H[Calculate four result matrices]
    H --> I[Combine result matrices]
    E --> J[Remove padding if required]
    I --> J
    J --> K[/Display result matrix/]
    K --> L([End])
```