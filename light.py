import tkinter as tk
import random
from tkinter import messagebox

class LightsOut:
    def __init__(self, master, size=5):
        self.master = master
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.steps = 0

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.master, text="Steps: 0", font=("Arial", 14))
        self.label.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="New Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.frame, width=4, height=2)
                button.config(command=lambda x=i, y=j: self.toggle(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.reset_game()

    def toggle(self, x, y):
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.board[nx][ny] ^= 1
        self.steps += 1
        self.update_board()
        if self.check_win():
            self.label.config(text=f"You won in {self.steps} steps!")
            messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.steps} steps!")
        else:
            self.label.config(text=f"Steps: {self.steps}")

    def update_board(self):
        for i in range(self.size):
            for j in range(self.size):
                color = "yellow" if self.board[i][j] else "black"
                self.buttons[i][j].config(bg=color)

    def reset_game(self):
        self.steps = 0
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = random.randint(0, 1)
        self.update_board()
        self.label.config(text="Steps: 0")

    def check_win(self):
        return all(cell == 0 for row in self.board for cell in row)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lights Out")
    app = LightsOut(root)
    root.mainloop()
