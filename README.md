# 🧩 Maze Solver with DFS and BFS Animation

This project visualizes maze generation and solving using two classic graph traversal algorithms: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**. It creates a random maze, animates its generation, then solves it first with DFS and then with BFS, showcasing how the two approaches differ in pathfinding.

## ✨ Features

- ✅ **Random Maze Generation** with adjustable seed  
- 🎨 **Animated Visualization** using Tkinter  
- 🧠 **DFS-based Solver** (recursive backtracking)  
- 🔍 **BFS-based Solver** (shortest path finder)  
- 💾 **Automatic Screenshot Saving** of the maze and solution  
- 🔁 **Reinitialization** to allow comparison between DFS and BFS on the same maze  

## 🧠 What I Learned

While working on this project, I gained practical experience with:

- Recursion and iterative approaches for graph traversal (DFS and BFS)
- Maze generation using a randomized DFS-based algorithm
- GUI programming and real-time drawing using Tkinter
- Saving canvas content as images using Pillow and PostScript
- Working with classes and modular code design in Python
- Understanding the visual difference between **DFS (non-optimal paths)** and **BFS (optimal shortest paths)**

## 🛠 Requirements

Before running the project, make sure you have the following:

- Python 3
- Pillow (`pip install pillow`)
- Ghostscript (for converting PostScript images to PNG)

To install Ghostscript on Ubuntu/Debian-based systems:
```bash
sudo apt-get install ghostscript
```
## ▶️ How to Run

1. Clone the repository or download the source files.
2. Ensure all required dependencies are installed.
3. Run the main script:
    ```bash
    python3 main.py
    ```

## 🧪 What Happens When You Run It

1. A random maze is generated and animated.
2. The maze is saved as an image (`mazeX.png` in the `maze/` folder).
3. The maze is solved using **Depth-First Search (DFS)** and the path is animated.
4. The DFS solution is saved as an image (`maze_solutionX.png`).
5. The maze is regenerated using the same seed.
6. The maze is solved again using **Breadth-First Search (BFS)** and the shortest path is shown.

## 📁 Output

All saved images will appear in the `maze/` directory:

- `maze1.png`, `maze2.png`, etc. – Generated maze
- `maze_solution1.png`, `maze_solution2.png`, etc. – Solution paths

## 📦 Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt