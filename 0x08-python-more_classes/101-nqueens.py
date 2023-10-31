#!/usr/bin/python3
"""
solve n queen puzzle
"""
import sys



def nqueens(n):
    """
    Solve the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of all valid solutions to the N Queens problem.

    Raises:
        ValueError: If n is not an integer or n is smaller than 4.
    """
    if not isinstance(n, int):
        raise ValueError("N must be a number")
    if n < 4:
        raise ValueError("N must be at least 4")

    def backtrack(row, cols, diags1, diags2):
        """
        Recursive function to find valid solutions by backtracking.

        Args:
            row (int): The current row being considered.
            cols (list): List of column positions of queens placed so far.
            diags1 (list): List of diagonal positions (/) of queens placed so far.
            diags2 (list): List of diagonal positions (\) of queens placed so far.

        Returns:
            list: A list of valid solutions found so far.
        """
        if row == n:
            return [cols]
        solutions = []
        for col in range(n):
            if col not in cols and row+col not in diags1 and row-col not in diags2:
                solutions += backtrack(row+1, cols+[col], diags1+[row+col], diags2+[row-col])
        return solutions

    return backtrack(0, [], [], [])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print(solution)

