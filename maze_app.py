import tkinter as tk
from tkinter import messagebox

# root is the window where we want to add the widgets

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Generator App")

        # Label and input for maze stats
        self.width_label = tk.Label(root, text = "Width : ")
        self.width_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.width_entry = tk.Entry(root, width = 5)
        self.width_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.height_label = tk.Label(root, text = "Height : ")
        self.height_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.height_entry = tk.Entry(root, width = 5)
        self.height_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Button for generating the maze
        self.generate_button = tk.Button(root, text = "Generate", command = self.generate_maze)
        self.generate_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

    def generate_maze(self):
        messagebox.showinfo("MAZE", f"Maze will be generated width {self.width_entry.get()} and height {self.height_entry.get()}")