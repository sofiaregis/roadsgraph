import csv
from PIL import Image

class Grid:
    def __init__(self, rows=0, cols=0):
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]
        self.warehouse = []
    
    def load_from_csv(self, file_path):
        """Reads a CSV file and populates the grid."""
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.grid = [[int(cell) if cell.isdigit() else cell for cell in row] for row in reader]
    
    def display(self):
        """Prints the grid to the console in a readable format."""
        for row in self.grid:
            print(" ".join([str(cell) if isinstance(cell, int) else cell for cell in row]))

    def save_grid_as_image(self, verbose, filename):
        """Creates an image representation of the grid."""
        height, width = len(self.grid), len(self.grid[0])
        img = Image.new("RGB", (width, height), "white")
        pixels = img.load()
        
        for r in range(height):
            for c in range(width):
                if isinstance(self.grid[r][c], int):  # Buildings
                    pixels[c, r] = (0, 0, 255)  # Blue
                elif self.grid[r][c] == "R":  # Roads
                    pixels[c, r] = (255, 0, 0)  # Red
                else:  # Empty space
                    pixels[c, r] = (255, 255, 255)  # White
        
        img = img.resize((width * 10, height * 10), Image.NEAREST)
        img.save(filename)
        if verbose:
            print(f"Grid image saved as {filename}")
            img.show()
