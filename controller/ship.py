class Ship:
    def __init__(
        self,
        size: int,
        x_position: int,
        y_position: int,
        orientation: str,
        color: str = "#000000",
    ):

        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = orientation
        self.color = color


class Cruiser(Ship):

    SIZE = 4
    COLOR = "#ff0000"

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(
            Cruiser.SIZE, x_position, y_position, orientation, Cruiser.COLOR
        )


class Escort(Ship):

    SIZE = 3
    COLOR = "#33cc33"

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(Escort.SIZE, x_position, y_position, orientation, Escort.COLOR)


class Torpedo(Ship):

    SIZE = 2
    COLOR = "#e6e600"

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(
            Torpedo.SIZE, x_position, y_position, orientation, Torpedo.COLOR
        )


class SubMarine(Ship):

    SIZE = 1
    COLOR = "#0000ff"

    def __init__(self, x_position: int, y_position: int, orientation: str):
        super().__init__(
            SubMarine.SIZE, x_position, y_position, orientation, SubMarine.COLOR
        )
