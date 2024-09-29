#!/usr/bin/python3
import sys


def solveNQueens(board, row, coulmn):
    """"""
    for r in range(row):
        if board[r] == coulmn:
            return False

        c = board[r]
        if(row - coulmn) == abs(r - c):
            return False

        if(row + coulmn) == (r + c):
            return False
    return True



if __name__ == "__main__":
    """"""
    if len(sys.argv) != 2:
        print ("Usage: nqueens N")
        sys.exit (1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print ("N must be a number")
        sys.exit (1)

    if n < 4 :
        print("N must be at least 4")
        sys.exit (1)