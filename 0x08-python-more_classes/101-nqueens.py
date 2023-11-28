#!/usr/bin/python3
# 101-nqueens.py
#Abdulmalik Sani <thepersian82@gmail.com>
"""A puzzle calculator.

find all possible quwwn placement.

a coll function

a base 16 position.

Attributes:
    board (list): A 2d list.
    solutions (list):possible soln.

a r x c soln .
"""
import sys


def init_board(n):
    """initialize the board."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """duplicate board."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """list of solution."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """the out of the board.

    non valid position are marked off.

    Args:
        board (list): possible position.
        row (int): forward loc.
        col (int): trans position.
    """
    # X out the fomakerd
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out non retreat
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out invalid
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all the top
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all the diag move
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all hypotanus csanclled
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots hyp right conor
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots buttom conor
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """a recursive soln.

    Args:
        board (list): active cells.
        row (int): active row.
        queens (int): 2d rep of queens.
        solutions (list): possible valid.
    Returns:
        correct placement
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
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
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
