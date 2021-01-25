from controller.grid import Grid
from controller.cell import Cell
from controller.ship import Cruiser, Escort, Torpedo, SubMarine, Ship
import pytest


class TestGrid:
    @staticmethod
    @pytest.fixture(scope="function")
    def height():
        return 50

    @staticmethod
    @pytest.fixture(scope="function")
    def width():
        return 50

    @staticmethod
    def test_constructor(height, width):

        # GIVEN
        attributes = [
            "height",
            "width",
            "cruisers",
            "escorts",
            "torpedos",
            "submarines",
            "grid",
        ]

        # WHEN
        grid = Grid(width, height)

        # ASSERT
        for attribute in attributes:
            assert attribute in grid.__dict__
        assert grid.height == height
        assert grid.width == width

    @staticmethod
    def test_create_empty_grid_dimension(height, width):

        # GIVEN
        grid = Grid(width, height)

        # WHEN
        grid.create_empty_grid()

        # ASSERT
        assert len(grid.grid) == height
        assert len(grid.grid[0]) == width

    @staticmethod
    def test_create_empty_grid_with_cell(height, width):

        # GIVEN
        grid = Grid(width, height)

        # WHEN
        grid.create_empty_grid()

        # ASSERT
        assert isinstance(grid.grid[0][0], Cell)

    @staticmethod
    @pytest.fixture(scope="function")
    def grid(height, width):
        return Grid(width, height)

    @staticmethod
    @pytest.mark.parametrize(
        "ship_type,length",
        [("cruisers", 1), ("escorts", 2), ("torpedos", 3), ("submarines", 4)],
    )
    def test_fill_grid_create_list_of_ship(grid, ship_type, length):

        # GIVEN
        grid.create_empty_grid()

        # WHEN
        grid.fill_grid()

        # ASSERT
        assert len(grid.__getattribute__(ship_type)) == length

    @staticmethod
    @pytest.fixture(scope="function")
    def fishing_boat():
        class FishingBoat(Ship):
            SIZE = 5
            COLOR = "#aa2b3e"

            def __init__(size: int, x_position: int, y_position: int, orientation: str):
                super().__init__(
                    FishingBoat.SIZE,
                    x_position,
                    y_position,
                    orientation,
                    FishingBoat.COLOR,
                )

        return FishingBoat

    @staticmethod
    def test_create_ships_length_ok(grid, fishing_boat):

        # GIVEN
        grid.create_empty_grid()
        number_of_fishing_boat = 3

        # WHEN
        result = grid.create_ships(fishing_boat, number_of_fishing_boat)

        # ASSERT
        assert len(result) == number_of_fishing_boat
        assert isinstance(result[0], fishing_boat)

    @staticmethod
    def test_create_ships_have_different_position(grid, fishing_boat):
        # GIVEN
        grid.create_empty_grid()
        number_of_fishing_boat = 8

        # WHEN
        result = grid.create_ships(fishing_boat, number_of_fishing_boat)
        positions = [(ship.x_position, ship.y_position) for ship in result]
        # ASSERT

        for position in positions:
            assert positions.count(position) == 1
