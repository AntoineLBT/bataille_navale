from .cell import Cell
from controller.ship import Cruiser, Escort, Torpedo, SubMarine
from random import randrange


class Grid:

    CRUISER_NUMBER = 1
    ESCORT_NUMBER = 2
    TORPEDO_NUMBER = 3
    SUBMARINE_NUMBER = 4

    def __init__(self, width, height):
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
        self.cruisers = self.create_ships(Cruiser, Grid.CRUISER_NUMBER)
        self.escorts = self.create_ships(Escort, Grid.ESCORT_NUMBER)
        self.torpedos = self.create_ships(Torpedo, Grid.TORPEDO_NUMBER)
        self.submarines = self.create_ships(SubMarine, Grid.SUBMARINE_NUMBER)

    def create_ships(
        self, ship_class: [Cruiser, Escort, Torpedo, SubMarine], number_of_ship: int
    ) -> list:
        # Determine horizontal or vertical orientation
        ships = []
        for _ in range(number_of_ship):

            orientation, x_pos, y_pos = self.generate_ship_data(ship_class)

            while not self.check_perimeter_is_available(
                orientation, ship_class.SIZE, x_pos, y_pos
            ):
                orientation, x_pos, y_pos = self.generate_ship_data(ship_class)

            self.allocate_perimeter(ship_class, x_pos, y_pos, orientation)
            self.define_ship_cells(ship_class, x_pos, y_pos, orientation)
            ships.append(ship_class(x_pos, y_pos, orientation))
        return ships

    def generate_ship_data(self, ship_class):
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

    def allocate_perimeter(
        self,
        ship_class: [Cruiser, Escort, Torpedo, SubMarine],
        x_pos_start: int,
        y_pos_start: int,
        orientation: str,
    ):
        for cell in self.select_perimeter(
            orientation, ship_class.SIZE, x_pos_start, y_pos_start
        ):

            self.grid[cell[0]][cell[1]].is_empty = False

    def define_ship_cells(
        self,
        ship_class: [Cruiser, Escort, Torpedo, SubMarine],
        x_pos_start: int,
        y_pos_start: int,
        orientation: str,
    ):

        ship_cells = self.select_ship_cells(
            orientation, ship_class, x_pos_start, y_pos_start
        )

        for cell in ship_cells:
            self.grid[cell[0]][cell[1]].ship_type = ship_class
            self.grid[cell[0]][cell[1]].color = ship_class.COLOR

    @staticmethod
    def select_ship_cells(orientation, ship_class, x_pos_start, y_pos_start):
        if orientation == "vertical":
            positions_ships = [
                (y, x_pos_start)
                for y in range(y_pos_start, y_pos_start + ship_class.SIZE, 1)
            ]
        else:
            positions_ships = [
                (y_pos_start, x)
                for x in range(x_pos_start, x_pos_start + ship_class.SIZE, 1)
            ]
        return positions_ships

    def check_perimeter_is_available(
        self, orientation, ship_size, x_pos_start, y_pos_start
    ):
        is_cells_available = True
        cells_to_check = self.select_perimeter(
            orientation, ship_size, x_pos_start, y_pos_start
        )  # list of tuple : (y,x)

        for cell_to_check in cells_to_check:

            if not self.grid[cell_to_check[0]][cell_to_check[1]].is_empty:
                is_cells_available = False
                break
        return is_cells_available

    def select_perimeter(self, orientation, ship_size, x_pos_start, y_pos_start):

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

        cells_to_return = self.filter_invalid_cells(cells_to_check)

        return cells_to_return

    def filter_invalid_cells(self, cells_to_check):
        cells_to_return = []
        for cell in cells_to_check:
            if 0 <= cell[0] < self.height and 0 <= cell[1] < self.width:
                cells_to_return.append(cell)
        return cells_to_return
