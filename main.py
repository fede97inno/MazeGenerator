from maze_generator import MazeGenerator
import tkinter as tk
from maze_app import MazeApp

if __name__ == '__main__':

    # ---- Console App ----
    """
    print("Hi! Welcome to the ultimate Maze generator system (unless you choose even numbers)")

    rows = int(input("Insert number of Rows : "))
    columns = int(input("Insert number of Columns : "))

    generator = MazeGenerator(rows, columns)
    generator.generate_maze()

    generator.print_maze()

    input()
    """
    # ---- GUI App ----

    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()

