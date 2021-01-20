class Ship:
    def __init__(self, size: int, x_position: int, y_position: int):

        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = None


class Cruiser(Ship):
    def __init__(self, x_position: int, y_position: int):
        super().__init__(4, x_position, y_position)


class Escort(Ship):
    def __init__(self, x_position: int, y_position: int):
        super().__init__(3, x_position, y_position)


class Torpedo(Ship):
    def __init__(self, x_position: int, y_position: int):
        super().__init__(2, x_position, y_position)


class SubMarine(Ship):
    def __init__(self, x_position: int, y_position: int):
        super().__init__(1, x_position, y_position)
