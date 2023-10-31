#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""
import sys


def init_board(n):
    """Initialize the chessboard with"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def deepcopy(board):
    """deepcopy"""
    if isinstance(board, list):
        return list(map(deepcopy, board))
    return (board)


def solutionf(board):
    """Return the solution of the chess board"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """chessboard.
    
    Args:
        board (list): The chessboard.
        row (int): The row where a queen played.
        col (int): The column where a queen played.
    """
    
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    
    ci = col + 1
    for r in range(row + 1, len(board)):
        if ci >= len(board):
            break
        board[r][ci] = "x"
        ci += 1
    
    ci = col - 1
    for r in range(row - 1, -1, -1):
        if ci < 0:
            break
        board[r][ci]
        ci -= 1
    
    ci = col + 1
    for r in range(row - 1, -1, -1):
        if ci >= len(board):
            break
        board[r][ci] = "x"
        ci += 1
    
    ci = col - 1
    for r in range(row + 1, len(board)):
        if ci < 0:
            break
        board[r][c] = "x"
        ci -= 1


def recursive(board, row, queens, solutions):
    """solve the N-queens puzzle.
    
    Args:
        board (list): The chessboard.
        row (int): The row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(solutionf(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive(board, 0, 0, [])
    for sol in solutions:
        print(sol)
