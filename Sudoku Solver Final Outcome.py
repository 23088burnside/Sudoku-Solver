import tkinter as tk
from tkinter import messagebox

#Backtracking Algorithm
def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

#Is the number valid in its cell?
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for r in range(9):
        if board[r][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

#Empty Spots
def find_empty(board):
    for r in range (9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def on_solve():
    #Get Board from entrygrid
    try:
        board = []
        user_inputs = []
        for row in range(9):
            row_data = []
            user_row_data = []
            for col in range(9):
                value = entry_widgets[row][col].get()
                if value =="":
                    row_data.append(0)
                    user_row_data.append(False)
                else:
                    row_data.append(int(value))
                    user_row_data.append(True)
            board.append(row_data)
            user_inputs.append(user_row_data)
        
        #Update the grid with solution (if solved)
        if solve_sudoku(board):
            for row in range(9):
                for col in range(9):
                    entry_widgets[row][col].delete(0, tk.END)
                    entry_widgets[row][col].insert(0, str(board[row][col]))
                    
                    if board[row][col] != 0 and not user_inputs[row][col]:
                        entry_widgets[row][col].config(fg="skyblue")
                    else:
                        entry_widgets[row][col].config(fg="black")
        else:
            messagebox.showinfo("No Soluion", "No Solution Exsists For The Give Sudoku Puzzle.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please Enter Only Numbers 1 To 9 Or Leave The Cells Empty.")

#Tkinter Window
root = tk.Tk()
root.title("Sudoku Solver")

# Entry Grid (9 by 9 grid)
entry_widgets = []
for row in range(9):
    entry_row = []
    for col in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        entry.grid(row=row, column=col, padx=5, pady=5)
        entry_row.append(entry)
    entry_widgets.append(entry_row)

# Create a 'Solve' button
solve_button = tk.Button(root, text="Solve", font=('Arial', 14), command=on_solve)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

# Event loop
root.mainloop()