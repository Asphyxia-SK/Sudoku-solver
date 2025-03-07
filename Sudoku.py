@ -0,0 +1,74 @@
def is_valid(arr, row, col, num):
    # Check if num is in the same row
    if num in arr[row]:
        return False

    # Check if num is in the same column
    for i in range(9):
        if arr[i][col] == num:
            return False

    # Check if num is in the 3x3 subgrid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[start_row + i][start_col + j] == num:
                return False

    return True


def sudoku(arr, row=0, col=0):
    # If we reach row 9, the board is solved
    if row == 9:
        return True

    # If we reach column 9, move to the next row
    if col == 9:
        return sudoku(arr, row + 1, 0)

    # If the current cell is already filled, move to the next column
    if arr[row][col] != 0:
        return sudoku(arr, row, col + 1)

    # Try placing numbers 1 to 9
    for i in range(1, 10):
        if is_valid(arr, row, col, i):
            arr[row][col] = i  # Place the number
            if sudoku(arr, row, col + 1):  # Recurse to the next cell
                return True
            arr[row][col] = 0  # Backtrack if placement fails

    return False  # No valid number found, trigger backtracking


# Function to take Sudoku input from user
def get_sudoku_input():
    board = []
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = list(
                    map(int, input(f"Enter row {i + 1} (space-separated 9 numbers): ").split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row):
                    print("Invalid input! Enter exactly 9 numbers between 0 and 9.")
                    continue
                board.append(row)
                break
            except ValueError:
                print("Invalid input! Enter only numbers.")

    return board


# Get Sudoku input from the user
board = get_sudoku_input()  # <-- Fixed: Call the function to get board before solving

# Solve the Sudoku puzzle
if sudoku(board):
    print("\nSolved Sudoku Board:")
    for row in board:
        print(row)
else:
    print("No solution exists")
