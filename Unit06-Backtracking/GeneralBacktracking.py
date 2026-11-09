# General Backtracking Technique
# Example: Generate all binary strings of length n

def generate_binary_strings(n, current=""):
    # Base case: A complete solution is created
    if len(current) == n:
        print(current)
        return

    # Try choice 0
    generate_binary_strings(n, current + "0")

    # Backtrack and try choice 1
    generate_binary_strings(n, current + "1")


# Input length
n = 3

print(f"All binary strings of length {n}:")
generate_binary_strings(n)