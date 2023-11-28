#!/usr/bin/python3
"""chess puzzle

defination of chess puzzle

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candidates (list) of (list) of (list) of (int): list of all successful
        solutions for given amount of columns checked

"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """a function representing the board.

    Args:
        board (list) of (list) of (int): dimension of the board.

    Returns:
        board of a given size

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Add a a player option.

    Args:
        board (list) of (list) of (int): list matrix of board.
        row (int): dimensioin a
        col (int): dimension b

    """
    board[row][col] = 1


def new_queen_safe(board, row, col):
    """the placement of queen on the board.

    Args:
        board (list) of (list) of (int): the index position to place.
        row (int): row
        col (int):column

    Returns:
        True or false if possible

    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # verify placing
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # verify placing
            if board[x][y - i]:
                return False
            # verify down
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """chanhe to row and column.

    Args:
    candidates (list) of (list) of (list) of (int): convert 2

    Attributes:
        holberton (list) of (list) of (int): the vector space

    Returns:
        the corresponding pos

    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton

# create a caniddate list


candidates = []


candidates.append(board_column_gen())

# transverse across cell
for col in range(N):
    # the row transverse
    new_candidates = []
    # the individusl cell
    for matrix in candidates:
        # the row to te right
        for row in range(N):
            # check if occupied
            if new_queen_safe(matrix, row, col):
                # check validity
                temp = [line[:] for line in matrix]
                # do successfull
                add_queen(temp, row, col)
                # and otherwise,
                if col < N - 1:
                    # make new initialize
                    board_column_gen(temp)
                # palce where valid
                new_candidates.append(temp)
    # move to next
    candidates = new_candidates

# return to defult mode
for item in coordinate_format(candidates):
    print(item)
