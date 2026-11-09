# Sum of Subsets Problem using Backtracking

def find_subsets(numbers, target, index=0, current_subset=None, current_sum=0):
    if current_subset is None:
        current_subset = []

    # If target sum is found
    if current_sum == target:
        print("Subset found:", current_subset)
        return

    # Stop if sum exceeds target or all elements are checked
    if current_sum > target or index == len(numbers):
        return

    # Include the current number
    find_subsets(
        numbers,
        target,
        index + 1,
        current_subset + [numbers[index]],
        current_sum + numbers[index]
    )

    # Exclude the current number
    find_subsets(
        numbers,
        target,
        index + 1,
        current_subset,
        current_sum
    )


# Input set and target sum
numbers = [3, 4, 5, 2]
target = 7

print("Subsets with sum", target, ":")
find_subsets(numbers, target)