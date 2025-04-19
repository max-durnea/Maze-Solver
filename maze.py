from cell import Cell
import time
import random
from collections import deque
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None,speed=0.02):
        if seed is not None:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.speed = speed
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
        time.sleep(self.speed)  # Add delay for animation smoothness

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
    def solve(self):
        """
        Public method to solve the maze starting from the top-left corner (0,0)
        Returns True if maze is solvable, False otherwise
        """
        # Start solving from the top-left cell
        return self._solve_r(0, 0)

    def _solve_r(self, row, col):
        """
        Recursive helper method that implements depth-first search to solve the maze
        Returns True if a path to the goal is found, False otherwise
        """
        # Animate the solving process
        self.animate()
        
        # Mark current cell as visited
        self.cells[row][col].visited = True
        solved = False
        # Check if we've reached the goal (bottom-right corner)
        if row == self.num_rows - 1 and col == self.num_cols - 1:
            solved = True
        
        # Try each direction: right, down, left, up
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nrow = row + direction[0]
            ncol = col + direction[1]
            
            # Check if the next cell is valid and not visited
            if (0 <= nrow < self.num_rows and 
                0 <= ncol < self.num_cols and 
                not self.cells[nrow][ncol].visited and 
                not self.is_wall_between(row, col, nrow, ncol)):
                
                # Draw a move from current cell to next cell
                self.cells[row][col].draw_move(self.cells[nrow][ncol], False)  # False means draw in red
                
                # Recursively try to solve from the next cell
                if self._solve_r(nrow, ncol):
                    solved = True
                    


                else:
                    self.cells[row][col].draw_move(self.cells[nrow][ncol],True)
        # If no direction leads to the goal, return False
        return solved

    def is_wall_between(self, row1, col1, row2, col2):
        """
        Check if there is a wall between two adjacent cells
        Returns True if there is a wall, False otherwise
        """
        # Moving up
        if row2 == row1 - 1 and col2 == col1:
            return self.cells[row1][col1].has_top_wall
        # Moving right
        elif row2 == row1 and col2 == col1 + 1:
            return self.cells[row1][col1].has_right_wall
        # Moving down
        elif row2 == row1 + 1 and col2 == col1:
            return self.cells[row1][col1].has_bottom_wall
        # Moving left
        elif row2 == row1 and col2 == col1 - 1:
            return self.cells[row1][col1].has_left_wall
        # Cells are not adjacent
        else:
            return True
                        
    def solve_bfs(self):
        """
        Solve the maze using breadth-first search starting from the top-left corner
        Shows exploration to all cells and highlights the final path
        Returns True if maze is solvable, False otherwise
        """
        # Reset all cells' visited status
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False
        
        # Start point and goal point
        start = (0, 0)
        goal = (self.num_rows - 1, self.num_cols - 1)
        
        # Use a queue for BFS
        queue = deque([start])
        
        # Dictionary to keep track of path predecessors for each cell
        predecessors = {start: None}
        
        # Mark start as visited
        self.cells[start[0]][start[1]].visited = True
        
        # Track if we found the goal
        found_goal = False
        
        # BFS loop - explore all reachable cells
        while queue:
            # Get the next cell to examine
            current = queue.popleft()
            row, col = current
            
            # Draw path to this cell from its predecessor (except for start)
            if current != start:
                prev_row, prev_col = predecessors[current]
                self.cells[prev_row][prev_col].draw_move(self.cells[row][col], True)
                self.animate()
            
            # Check if we've reached the goal
            if current == goal:
                found_goal = True
                # Continue exploring the rest of the maze
            
            # Try each direction: right, down, left, up
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nrow = row + direction[0]
                ncol = col + direction[1]
                next_cell = (nrow, ncol)
                
                # Check if the next cell is valid and not visited
                if (0 <= nrow < self.num_rows and 
                    0 <= ncol < self.num_cols and 
                    not self.cells[nrow][ncol].visited and 
                    not self.is_wall_between(row, col, nrow, ncol)):
                    
                    # Mark as visited and add to queue
                    self.cells[nrow][ncol].visited = True
                    queue.append(next_cell)
                    
                    # Record the predecessor
                    predecessors[next_cell] = current
        
        # After exploring the whole maze, highlight the path to goal in red if found
        if found_goal:
            self._highlight_path_to_goal(predecessors, start, goal)
            return True
        
        # If we've exhausted all cells and haven't found the goal, the maze is unsolvable
        return False

    def _highlight_path_to_goal(self, predecessors, start, goal):
        """
        Highlights the final path from start to goal in red
        """
        # Start from the goal and work backwards to the start
        current = goal
        path = []
        
        # Reconstruct the path
        while current != start:
            path.append(current)
            current = predecessors[current]
        
        # Add the start cell
        path.append(start)
        
        # Reverse the path to go from start to goal
        path.reverse()
        
        # Highlight the final path in red
        for i in range(len(path) - 1):
            row, col = path[i]
            next_row, next_col = path[i + 1]
            
            # Draw a red move from current cell to next cell (indicating the solution path)
            # To draw in red, we first erase the gray line by drawing in white, then draw in red
            self.cells[row][col].draw_move(self.cells[next_row][next_col], False)  # True means draw in red
            self.animate()
                    
    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False