import tkinter as tk
import tkinter.messagebox
import random

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return True

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True

    return False

def button_click(row, col):
    global board, current_player
    if board[row][col] == 0:
        board[row][col] = current_player
        buttons[row][col]['text'] = 'X' if current_player == 1 else 'O'
        if check_win(board):
            tkinter.messagebox.showinfo("Game Over", "Player " + str(current_player) + " wins!")
            root.quit()
        else:
            current_player = 3 - current_player

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = 1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        random_color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        buttons[i][j] = tk.Button(root, text=' ', width=18, height=9, 
                                  command=lambda row=i, col=j: button_click(row, col),
                                  bg=random_color, font=('Helvetica', '24', 'bold'))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
