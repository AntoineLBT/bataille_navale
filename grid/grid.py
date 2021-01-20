from .cell import Cell


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []

    def create_empty_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append(Cell(x, y))
