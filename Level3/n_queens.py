# Level 3 - Task 3
# N-Queens Problem using Backtracking
# Codveda Python Internship

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")


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
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            solve_n_queens(board, row + 1, n)
            board[row][col] = "."  # Backtrack

    return False


def main():
    n = int(input("Enter the value of N: "))

    if n < 4:
        print("N must be at least 4 to have a solution.")
        return

    board = [["." for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

main()
