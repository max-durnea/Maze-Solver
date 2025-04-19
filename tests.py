import unittest
from maze import Maze
from window import Window
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertFalse(
                    m1.cells[i][j].visited,
                    f"Cell ({i}, {j}) should not be visited before resetting",
                )
        
if __name__ == "__main__":
    unittest.main()