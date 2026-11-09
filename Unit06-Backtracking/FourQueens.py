# 4-Queens Problem using Backtracking

N = 4


def print_solution(board):
    print("Solution:")
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col):
    # Check the column
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
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    # All queens have been placed
    if row == N:
        print_solution(board)
        return True

    # Try placing a queen in each column
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"

            if solve_queens(board, row + 1):
                return True

            # Backtrack
            board[row][col] = "."

    return False


# Create the chessboard
board = [["." for _ in range(N)] for _ in range(N)]

if not solve_queens(board, 0):
    print("No solution exists.")