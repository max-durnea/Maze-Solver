class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    # takes 2 points
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, color="black"):
        # Use exactly the same width for both black and white lines
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)

class Cell():
    def __init__(self, window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, size=20):
        # top left corner
        self.size = size
        self.x1 = 0
        self.y1 = 0
        # bottom right corner
        self.x2 = self.x1 + size
        self.y2 = self.y1 + size
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
        self.win = window
        self.visited = False
    
    def draw(self):
        if self.win is None:
            return
        
        # Use the exact same coordinates for all lines to ensure perfect overlap
        
        # Left wall
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line)
        else:
            # Draw background color line with precise coordinates
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line, "white")
        
        # Right wall
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line, "white")
        
        # Top wall
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line, "white")
        
        # Bottom wall
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
            
        my_center = Point(self.x1 + self.size // 2, self.y1 + self.size // 2)
        to_center = Point(to_cell.x1 + to_cell.size // 2, to_cell.y1 + to_cell.size // 2)
        line = Line(my_center, to_center)
        
        if not undo:
            line.draw(self.win.canvas, "red")
        else:
            line.draw(self.win.canvas, "gray")