"""
N-Queens Problem - Backtracking

Place N queens on an NxN chessboard so that no two queens attack
each other (same row, column, or diagonal). Uses backtracking:
place queens row by row, undo (backtrack) when a conflict is found.
"""


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    # check column
    for i in range(row):
        if board[i] == col:
            return False
    # check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n):
    """Returns list of solutions; each solution is a list where
    board[row] = column of the queen in that row."""
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # undo (backtrack)

    backtrack(0)
    return solutions


def print_board(solution, n):
    """Print one solution as a chessboard."""
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)


if __name__ == "__main__":
    n = 4
    solutions = solve_nqueens(n)
    print("N-Queens solutions for n =", n, ":", len(solutions))
    print()
    for idx, sol in enumerate(solutions, 1):
        print("Solution", idx, ":")
        print_board(sol, n)
        print()
