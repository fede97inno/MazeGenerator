import tkinter as tk
from tkinter import messagebox
from maze_generator import MazeGenerator

# root is the window where we want to add the widgets

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Generator App")

        # Label and input for maze stats
        # Label create the field with text
        # Entry create the field where you can add text
        # Grid is used to put the widget in the window

        self.width_label = tk.Label(root, text = "Width : ")
        self.width_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.width_entry = tk.Entry(root, width = 5)
        self.width_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.height_label = tk.Label(root, text = "Height : ")
        self.height_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.height_entry = tk.Entry(root, width = 5)
        self.height_entry.grid(row = 0, column = 3, padx = 10, pady = 10)

        # Button for generating the maze
        self.generate_button = tk.Button(root, text = "Generate", command = self.generate_maze)
        self.generate_button.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)

        # Canvas widget for drawing the maze
        self.maze_canvas = tk.Canvas(root, width = 400, height = 400, bg = "black")
        self.maze_canvas.grid(row = 1, column = 4, columnspan = 2, padx = 10, pady = 10)

    def generate_maze(self):
        width = self.width_entry.get()
        height = self.height_entry.get()

        if not width.isdigit() and not height.isdigit():
            messagebox.showinfo("ERROR", f"ERROR: Insert digit only!")
            return

        generator = MazeGenerator(int(width), int(height))
        maze = generator.generate_maze()

        self.maze_canvas.delete("all")
        self.draw_maze(maze)

    def draw_maze(self, maze):
        cell_size = 20      # Cell dimension in pixels

        rows = len(maze)
        cols = len(maze[0])

        for r in range(rows):
            for c in range(cols):
                x1 = c * cell_size
                x2 = x1 + cell_size
                y1 = r * cell_size
                y2 = y1 + cell_size

                if maze[r][c] == 1:
                    self.maze_canvas.create_rectangle(x1, y1, x2, y2, fill = "white")
                elif maze[r][c] == 0:
                    self.maze_canvas.create_rectangle(x1, y1, x2, y2, fill = "black")

        
            