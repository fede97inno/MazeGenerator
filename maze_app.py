import tkinter as tk
from tkinter import messagebox, filedialog
from maze_generator import MazeGenerator

"""
    TODO : Try to refactor the code with self.dimensions to prevent using multiple calls to entry.get() -> DONE
         : Add entrance and exit for the maze with a pop up menu when right clicking on the canvas
         : Add a pathfindinf algorithm to resolve the maze given the entrance and the exit
"""
# root is the window where we want to add the widgets

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Generator App")
        self.maze = []
        self.cell_size = 20
        self.width = 0
        self.height = 0

        # Label and input for maze stats
        # Label create the field with text
        # Entry create the field where you can add text
        # Grid is used to put the widget in the window

        self.width_label = tk.Label(root, text = "Width (min 3 - max 100) : ")
        self.width_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.width_entry = tk.Entry(root, width = 5)
        self.width_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.height_label = tk.Label(root, text = "Height (min 3 - max 100) : ")
        self.height_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.height_entry = tk.Entry(root, width = 5)
        self.height_entry.grid(row = 0, column = 3, padx = 10, pady = 10)

        # Button for generating the maze
        self.generate_button = tk.Button(root, text = "Generate", command = self.generate_maze)
        self.generate_button.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)

        # Canvas widget for drawing the maze
        self.maze_canvas = tk.Canvas(root, width = 400, height = 400, bg = "black")
        self.maze_canvas.grid(row = 1, column = 4, columnspan = 2, padx = 10, pady = 10)

        # Event for clicking in the canvas
        self.maze_canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Button for exporting the maze in txt file
        self.export_button = tk.Button(root, text = "Export", command = self.export_maze)
        self.export_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

    def generate_maze(self):
        if not self.width_entry.get().isdigit() or not self.height_entry.get().isdigit():
            messagebox.showinfo("ERROR", f"ERROR: Insert digit only!")
            return
        
        self.width = int(self.width_entry.get())
        self.height = int(self.height_entry.get())

        if self.width > 100 or self.height > 100:
            messagebox.showinfo("ERROR", f"ERROR: Insert numbers less than 100!")
            return

        if self.width < 3 or self.height < 3:
            messagebox.showinfo("ERROR", f"ERROR: Insert numbers grater or equal than 3!")
            return
        
        generator = MazeGenerator(self.width, self.height)
        self.maze = generator.generate_maze()

        self.maze_canvas.delete("all")
        self.draw_maze(self.maze)

    def draw_maze(self, maze):
        rows = len(maze)
        cols = len(maze[0])

        if rows > 20 or cols > 20:
            if rows > cols:
                self.cell_size = 400 / rows
            else:
                self.cell_size = 400 / cols

        for r in range(rows):
            for c in range(cols):
                x1 = c * self.cell_size
                x2 = x1 + self.cell_size
                y1 = r * self.cell_size
                y2 = y1 + self.cell_size

                if maze[r][c] == 1:
                    self.maze_canvas.create_rectangle(x1, y1, x2, y2, fill = "white")
                elif maze[r][c] == 0:
                    self.maze_canvas.create_rectangle(x1, y1, x2, y2, fill = "black")
    
    def on_canvas_click(self, event):
        if len(self.maze) == 0 or len(self.maze[0]) == 0:
            return

        col = int(event.x // self.cell_size)
        row = int(event.y // self.cell_size)

        if 0 < row < self.height and 0 < col < self.width:
            if self.maze[row][col] == 1:
                self.maze[row][col] = 0
                self.maze_canvas.create_rectangle(col * self.cell_size, row * self.cell_size, (col + 1) * self.cell_size, (row + 1) * self.cell_size, fill = "black")
            else:
                self.maze[row][col] = 1
                self.maze_canvas.create_rectangle(col * self.cell_size, row * self.cell_size, (col + 1) * self.cell_size, (row + 1) * self.cell_size, fill = "white")

    def export_maze(self):
        file_path = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Text files", "*.txt")])

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    for i, row in enumerate(self.maze):
                        file.write(' '.join(map(str, row)))

                        if i < len(self.maze) - 1:
                            file.write('\n') 
                
                messagebox.showinfo("Succes", "Maze exported successfully!")
            except Exception as e:
                messagebox.showinfo("Error", f"Failed to export maze: {e}!")