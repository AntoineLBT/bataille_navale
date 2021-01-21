from .cell import Cell
from ship.ship import Cruiser, Escort, Torpedo, SubMarine
from random import randrange


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cruisers = []
        self.escorts = []
        self.torpedos = []
        self.submarines = []
        self.grid = []

    def create_empty_grid(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Cell(x, y))
            self.grid.append(row)

    def fill_grid(self):
        self.cruisers = self.create_ships(Cruiser, 1)
        self.escorts = self.create_ships(Escort, 2)
        self.torpedos = self.create_ships(Torpedo, 3)
        self.submarines = self.create_ships(SubMarine, 4)

    def create_ships(
        self, ship_class: [Cruiser, Escort, Torpedo, SubMarine], number_of_ship: int
    ) -> list:
        # Determine horizontal or vertical orientation
        ships = []
        for i in range(number_of_ship):

            orientation, x_pos, y_pos = self.create_a_ship(ship_class)

            while not self.check_cells_are_available(
                orientation, ship_class.SIZE, x_pos, y_pos
            ):
                orientation, x_pos, y_pos = self.create_a_ship(ship_class)

            self.allocate_cells(ship_class.SIZE, x_pos, y_pos, orientation)

            ships.append(ship_class(x_pos, y_pos, orientation))
        return ships

    def create_a_ship(self, ship_class):
        orientation = randrange(2)
        if orientation:
            orientation = "vertical"
            x_pos = randrange(self.width)
            y_pos = randrange(self.height - ship_class.SIZE)
        else:
            orientation = "horizontal"
            x_pos = randrange(self.width - ship_class.SIZE)
            y_pos = randrange(self.height)
        return orientation, x_pos, y_pos

    def allocate_cells(
        self, ship_size: int, x_pos_start: int, y_pos_start: int, orientation: str
    ):
        for cell in self.select_cells(orientation, ship_size, x_pos_start, y_pos_start):
            self.grid[cell[0]][cell[1]].is_empty = False

    def check_cells_are_available(
        self, orientation, ship_size, x_pos_start, y_pos_start
    ):
        cells_available = True
        cells_to_check = self.select_cells(
            orientation, ship_size, x_pos_start, y_pos_start
        )  # list of tuple : (y,x)

        for cell_to_check in cells_to_check:

            y_out_of_bound_condition = (
                cell_to_check[0] < 0 or cell_to_check[0] >= self.height
            )
            x_out_of_bound_condition = (
                cell_to_check[1] < 0 or cell_to_check[1] >= self.width
            )

            if y_out_of_bound_condition or x_out_of_bound_condition:
                continue

            if not self.grid[cell_to_check[0]][cell_to_check[1]].is_empty:
                cells_available = False
                break
        return cells_available

    @staticmethod
    def select_cells(orientation, ship_size, x_pos_start, y_pos_start):

        cells_to_check = []

        if orientation == "vertical":
            for y in range(y_pos_start - 1, y_pos_start + ship_size + 1):
                cells_to_check.append((y, x_pos_start - 1))
                cells_to_check.append((y, x_pos_start))
                cells_to_check.append((y, x_pos_start + 1))
        else:
            for x in range(x_pos_start - 1, x_pos_start + ship_size + 1):
                cells_to_check.append((y_pos_start - 1, x))
                cells_to_check.append((y_pos_start, x))
                cells_to_check.append((y_pos_start + 1, x))

        return cells_to_check
