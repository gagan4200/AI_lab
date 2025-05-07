def is_safe(board, row, col, n):
    for i in range(row):
        # Check if any queen is in the same column or same diagonal
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True
def solve_n_queens(n):
    def solve(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve(row + 1)
                # board[row] = -1  # Backtrack
    result = []
    board = [-1] * n
    solve(0)
    return result
# Input and Output
n = int(input("Enter value of N: "))
solutions = solve_n_queens(n)
print(f"\nSolutions for {n}-Queens:")
for sol in solutions:
    print(sol)
