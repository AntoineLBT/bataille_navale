class Cell:
    def __init__(self, x_position: int, y_position: int):
        self.x_position = x_position
        self.y_position = y_position
        self.ship_class = None
        self.is_touched = False
        self.is_empty = True
        self.color = "#ffffff"
