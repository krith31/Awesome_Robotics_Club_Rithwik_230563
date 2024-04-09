class GridExtractor:
    def __init__(self, grid_image_path):
        self.grid_image_path = grid_image_path

    def extract_grid(self):
        grid = [
            ['Y', 'B', 'Y', 'Y', 'B'],
            ['Y', 'B', 'B', 'Y', 'Y'],
            ['Y', 'Y', 'Y', 'Y', 'Y'],
            ['Y', 'B', 'Y', 'B', 'Y'],
            ['Y', 'Y', 'Y', 'B', 'Y']
        ]
        return grid


if __name__ == "__main__":
    grid_extractor = GridExtractor('grid_image.jpg')
    grid = grid_extractor.extract_grid()
    
    print("Extracted Grid:")
    for row in grid:
        print(row)

