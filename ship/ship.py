class Ship:
    def __init__(self, size: int, x_position: int, y_position: int, orientation: str):

        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = orientation


class Cruiser(Ship):

    SIZE = 4

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(Cruiser.SIZE, x_position, y_position, orientation)


class Escort(Ship):

    SIZE = 3

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(Escort.SIZE, x_position, y_position, orientation)


class Torpedo(Ship):

    SIZE = 2

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(Torpedo.SIZE, x_position, y_position, orientation)


class SubMarine(Ship):

    SIZE = 1

    def __init__(self, x_position: int, y_position: int, orientation: bool):
        super().__init__(SubMarine.SIZE, x_position, y_position, orientation)
