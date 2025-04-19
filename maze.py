from cell import Cell
import time
import random
from collections import deque
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        if seed is not None:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)  # Start breaking walls from the first cell
        self.reset_cells_visited()  # Reset visited status for all cells
        if self.win is not None:
            self.win.redraw()

    def create_cells(self):
        self.cells = []
        for i in range(self.num_rows):  # Loop through rows
            row = []
            for j in range(self.num_cols):  # Loop through columns
                cell = Cell(self.win, True, True, True, True, self.cell_size_x)
                row.append(cell)
            self.cells.append(row)
        # Now draw all cells with proper coordinates
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(j, i)

    def draw_cell(self, i, j):
        if(self.win is None):
            return
        cell = self.cells[i][j]
        cell.x1 = self.x1 + j * self.cell_size_x
        cell.y1 = self.y1 + i * self.cell_size_y
        cell.x2 = cell.x1 + self.cell_size_x
        cell.y2 = cell.y1 + self.cell_size_y
        cell.draw()
        self.animate()

    def animate(self):
        if(self.win is None):
            return
        # Redraw window to update the animation
        self.win.redraw()
        time.sleep(0.001)  # Add delay for animation smoothness

    def break_entrance_and_exit(self):
        # Break the entrance and exit walls of the maze
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].draw()

        self.cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].draw()

    def break_walls_r(self, start_row, start_col):
        stack = [(start_row, start_col)]  # Use a stack to track the cells
        self.cells[start_row][start_col].visited = True

        while stack:
            row, col = stack[-1]  # Get the current cell from the stack

            # Get a list of unvisited neighbors
            neighbors = []
            if row > 0 and not self.cells[row - 1][col].visited:  # Up
                neighbors.append((row - 1, col))
            if row < self.num_rows - 1 and not self.cells[row + 1][col].visited:  # Down
                neighbors.append((row + 1, col))
            if col > 0 and not self.cells[row][col - 1].visited:  # Left
                neighbors.append((row, col - 1))
            if col < self.num_cols - 1 and not self.cells[row][col + 1].visited:  # Right
                neighbors.append((row, col + 1))

            if neighbors:
                nrow, ncol = random.choice(neighbors)

                # Break the wall between the current cell and the chosen neighbor
                if nrow < row:
                    self.cells[row][col].has_top_wall = False
                    self.cells[nrow][ncol].has_bottom_wall = False
                elif nrow > row:
                    self.cells[row][col].has_bottom_wall = False
                    self.cells[nrow][ncol].has_top_wall = False
                elif ncol < col:
                    self.cells[row][col].has_left_wall = False
                    self.cells[nrow][ncol].has_right_wall = False
                elif ncol > col:
                    self.cells[row][col].has_right_wall = False
                    self.cells[nrow][ncol].has_left_wall = False

                # Mark the neighbor as visited and push it onto the stack
                self.cells[nrow][ncol].visited = True
                stack.append((nrow, ncol))

                # Draw the current cell and animate
                self.cells[row][col].draw()
                self.animate()
            else:
                # No unvisited neighbors, pop the current cell from the stack
                stack.pop()

        # Once the stack is empty, the maze is fully created
        self.cells[start_row][start_col].draw()
        self.animate()
    
    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False