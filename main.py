from maze_generator import MazeGenerator

if __name__ == '__main__':
    print("Hi! Welcome to the ultimate Maze generator system (unless you choose even numbers)")

    rows = int(input("Insert number of Rows : "))
    columns = int(input("Insert number of Columns : "))

    generator = MazeGenerator(rows, columns)
    generator.generate_maze()

    generator.print_maze()

    input()