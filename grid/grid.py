from .cell import Cell
from ship.ship import Cruiser, Escort, Torpedo, SubMarine


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []

    def create_empty_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append(Cell(x, y))

    def fill_grid(self):
        self.create_ships(Cruiser, 1)
        self.create_ships(Escort, 2)
        self.create_ships(Torpedo, 3)
        self.create_ships(SubMarine, 4)

    def create_ships(self, ship_class: object, number_of_ship: int):
        pass

    def allocate_cells(self, ship_size: int, x_pos_start: int, y_pos_start):
        pass
