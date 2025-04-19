from random import randint
import time
from cell import Cell
from maze import Maze
from window import Window

def main():
    num_rows = 75  # Increased number of rows for a bigger maze
    num_cols = 100  # Increased number of columns for a bigger maze
    margin = 50
    screen_x = 1920  # Increased screen size to accommodate the larger maze
    screen_y = 1080  # Increased screen size to accommodate the larger maze
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = randint(0, 1000)  # Random seed for maze generation
    # Generate the maze
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed, speed=0.0001)  # Adjusted speed for smoother animation
    
    # Save the canvas to an image after the maze is created
    win.save_canvas_as_image("maze.ps")  # Save the canvas as a .ps file and convert to .png
    maze.reset_cells_visited()  # Reset visited status for all cells
    #maze.solve()  # Solve the maze
    maze.solve_bfs()  # Solve the maze using BFS
    win.save_canvas_solution_as_image("sol.ps")  # Save the solved maze as a .ps file and convert to .png
    # Optionally, solve the maze using BFS
    time.sleep(2)  # Wait for a moment before solving with BFS
    win.clear()  # Clear the canvas for BFS solution
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed,speed = 0.0001)  # Recreate the maze
    maze.reset_cells_visited()  # Reset visited status for all cells
    maze.solve_bfs()  # Solve the maze using BFS

    # Wait for the window to be closed
    win.wait_for_close()

if __name__ == "__main__":
    main()
