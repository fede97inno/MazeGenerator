from node import Node
import random

class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.nodes = []

        for r in range(rows):
            row = []                    # temporary list for the current row
            for c in range(cols):
                row.append(Node(r, c))  # append a new node at the row
            self.nodes.append(row)      # append the row to the nodes matrix of the maze generator

        self.directions = [(2,0), (-2,0), (0,2), (0,-2)] # initialization of the direction where i want to move
        
        self.maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def define_neighbours(self):
        for r in range(1, self.rows - 1):
            for c in range(1, self.cols - 1):
                for delta_row, delta_col in self.directions:
                    new_row, new_col = r + delta_row, c + delta_col
                    if 1 <= new_row < self.rows - 1 and  1 <= new_col < self.cols - 1:
                        self.nodes[r][c].neighbours.append(self.nodes[new_row][new_col])
    
    def generate_maze(self):
        self.define_neighbours()
        self.generate_maze_recursive(self.nodes[1][1])
        return self.maze
    
    def generate_maze_recursive(self, current_node):
        current_node.visited = True
        self.maze[current_node.row][current_node.col] = 0
        
        neighbours = current_node.neighbours.copy()
        random.shuffle(neighbours)

        for neighbour in neighbours:
            if not neighbour.visited:
                self.remove_wall(current_node, neighbour)
                self.generate_maze_recursive(neighbour)
    
    def remove_wall(self, current_node, neighbour):
        wall_row = (current_node.row + neighbour.row) // 2
        wall_col = (current_node.col + neighbour.col) // 2

        self.maze[wall_row][wall_col] = 0

    def print_maze(self):
        for row in self.maze:
            print(' '.join(str(cell) for cell in row))