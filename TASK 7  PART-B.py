import cv2

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_valid_cell(self, row, col):
        return self.is_valid_move(row, col) and self.grid[row][col] == 'Y' and (row, col) not in self.visited

    def find_shortest_path(self, start, end):
        queue = [(start, [])]

        while queue:
            (row, col), path = queue.pop(0)
            path.append((row, col))

            if (row, col) == end:
                return path

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid_cell(new_row, new_col):
                    self.visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), path[:]))

        return None



grid = [
    ['Y', 'B', 'Y', 'Y', 'B'],
    ['Y', 'B', 'B', 'Y', 'Y'],
    ['Y', 'Y', 'Y', 'Y', 'Y'],
    ['Y', 'B', 'Y', 'B', 'Y'],
    ['Y', 'Y', 'Y', 'B', 'Y']
]

grid_obj = Grid(grid)
start = (0, 0)  
end = (len(grid) - 1, len(grid[0]) - 1) 
shortest_path = grid_obj.find_shortest_path(start, end)

print("Shortest Path:")
for row, col in shortest_path:
    print(f"({row+1},{col+1})")
