def solveNQueens(n):
    result = []

    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue

            # Choose
            board[row][col] = ' Q '
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            # Explore
            backtrack(row + 1, cols, diag1, diag2, board)

            # Un-choose
            board[row][col] = ' _ '
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    empty_board = [[' _ '] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return result

# Example usage
solutions = solveNQueens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()
