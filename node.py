class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.neighbours = []