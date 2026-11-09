# N-Queens Problem using Backtracking

def print_solution(board):
    print("\nSolution:")
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    # Try every column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = "."

    return False


# Change this value to solve for different board sizes
n = 5

# Create the chessboard
board = [["." for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print(f"Solution for {n}-Queens Problem:")
    print_solution(board)
else:
    print("No solution exists.")