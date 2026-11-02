
import time
import csv
import matplotlib.pyplot as plt


def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)


def measure_time(search_function, arr, target, repetitions=500):
    start = time.perf_counter()

    for _ in range(repetitions):
        search_function(arr, target)

    end = time.perf_counter()

    return (end - start) / repetitions


def main():
    sizes = [1000, 5000, 10000, 50000, 100000, 200000]

    results = []

    for n in sizes:
        arr = list(range(n))

        best_target = arr[n // 2]
        average_target = arr[n // 3]
        worst_target = -1

        cases = {
            "Best": best_target,
            "Average": average_target,
            "Worst": worst_target
        }

        print(f"\nTesting input size: {n}")

        for algorithm_name, search_function in [
            ("Iterative", lambda a, t: iterative_binary_search(a, t)),
            ("Recursive", lambda a, t: recursive_binary_search(a, 0, len(a) - 1, t))
        ]:

            row = {
                "Algorithm": algorithm_name,
                "Input Size": n
            }

            for case_name, target in cases.items():

                result = search_function(arr, target)

                expected = -1 if target == -1 else target

                if result != expected:
                    raise RuntimeError("Search verification failed!")

                execution_time = measure_time(
                    search_function, arr, target
                )

                row[case_name + " Time (seconds)"] = execution_time

                print(
                    f"{algorithm_name} {case_name}: "
                    f"{execution_time:.10f} seconds"
                )

            results.append(row)

    # Save experimental results in CSV file
    with open("performance_results.csv", "w", newline="") as file:
        fieldnames = [
            "Algorithm",
            "Input Size",
            "Best Time (seconds)",
            "Average Time (seconds)",
            "Worst Time (seconds)"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nExperimental results saved successfully!")

    # Generate performance graph
    plt.figure(figsize=(10, 6))

    for algorithm in ["Iterative", "Recursive"]:
        algorithm_results = [
            row for row in results
            if row["Algorithm"] == algorithm
        ]

        input_sizes = [row["Input Size"] for row in algorithm_results]

        average_times = [
            row["Average Time (seconds)"]
            for row in algorithm_results
        ]

        plt.plot(
            input_sizes,
            average_times,
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Iterative vs Recursive Binary Search Performance")
    plt.legend()
    plt.grid(True)

    plt.savefig("performance_graph.png", dpi=300)
    plt.show()

    print("Performance graph generated successfully!")
    print("Performance analysis completed!")


if __name__ == "__main__":
    main()
