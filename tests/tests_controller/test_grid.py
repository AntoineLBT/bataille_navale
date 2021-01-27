from controller.grid import Grid
from controller.cell import Cell
from controller.ship import Ship
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

    @staticmethod
    def test_generate_ship_data_in_grid_range(grid, fishing_boat):

        # WHEN
        orientation, x_pos, y_pos = grid.generate_ship_data(fishing_boat)

        #
        assert 0 <= x_pos < grid.width - fishing_boat.SIZE
        assert 0 <= y_pos < grid.height - fishing_boat.SIZE

    @staticmethod
    def test_generate_ship_data_orientation(grid, fishing_boat):

        # WHEN
        orientation, x_pos, y_pos = grid.generate_ship_data(fishing_boat)

        # ASSERT
        assert orientation in ["vertical", "horizontal"]

    @staticmethod
    def test_allocate_perimeter_change_cell_state(grid, fishing_boat):

        # GIVEN
        grid.create_empty_grid()

        orientation = "vertical"
        x_pos = 2
        y_pos = 4

        cell_to_assert = [
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (1, 8),
            (1, 9),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (2, 7),
            (2, 8),
            (2, 9),
            (3, 3),
            (3, 4),
            (3, 5),
            (3, 6),
            (3, 7),
            (3, 8),
            (3, 9),
        ]

        # WHEN
        grid.allocate_perimeter(fishing_boat, x_pos, y_pos, orientation)

        # ASSERT
        for cell in cell_to_assert:
            assert grid.grid[cell[1]][cell[0]].is_empty is False
        assert grid.grid[2][2].is_empty is True
        assert grid.grid[4][0].is_empty is True

    @staticmethod
    def test_define_ship_cells_change_cell_attributes(grid, fishing_boat):

        # GIVEN
        grid.create_empty_grid()

        orientation = "vertical"
        x_pos = 2
        y_pos = 4

        # WHEN
        grid.define_ship_cells(fishing_boat, x_pos, y_pos, orientation)

        # ASSERT
        assert grid.grid[4][2].ship_type == fishing_boat
        assert grid.grid[4][2].color == "#aa2b3e"
        assert grid.grid[2][2].ship_class is None
        assert grid.grid[2][2].color == "#ffffff"

    @staticmethod
    def test_select_ship_cells_return_only_ship_cell(grid, fishing_boat):

        # GIVEN
        vertical = "vertical"
        horizontal = "horizontal"
        x_pos = 2
        y_pos = 4

        # WHEN
        result_vertical = grid.select_ship_cells(vertical, fishing_boat, x_pos, y_pos)
        result_horizontal = grid.select_ship_cells(
            horizontal, fishing_boat, x_pos, y_pos
        )

        # ASSERT
        assert len(result_horizontal) == fishing_boat.SIZE
        assert result_horizontal.count((4, 1)) == 0
        assert result_horizontal.count((4, 2)) == 1

        assert len(result_vertical) == fishing_boat.SIZE
        assert result_vertical.count((3, 2)) == 0
        assert result_vertical.count((5, 2)) == 1

    @staticmethod
    def test_check_perimeter_is_available_return_bool(grid, fishing_boat):

        # GIVEN
        grid.create_empty_grid()
        fishing_boat = grid.create_ships(fishing_boat, 1)[0]

        # WHEN
        result = grid.check_perimeter_is_available(
            fishing_boat.orientation,
            fishing_boat.SIZE,
            fishing_boat.x_position,
            fishing_boat.y_position,
        )

        assert isinstance(result, bool)
        assert not result

    @staticmethod
    def test_select_perimeter_return_all_cells(grid, fishing_boat):

        # GIVEN
        real_cells_to_check = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 1),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
            (5, 0),
            (5, 1),
            (5, 2),
            (6, 0),
            (6, 1),
            (6, 2),
        ]

        # WHEN
        result = grid.select_perimeter("vertical", fishing_boat.SIZE, 1, 1)

        # ASSERT
        assert result == real_cells_to_check
        assert (7, 0) not in real_cells_to_check

    @staticmethod
    def test_filter_invalid_cells_remove_invalid_cells(grid):

        # GIVEN
        cells_to_filter = [(-1, 2), (50, 2), (2, 4), (23, 4), (3, -2), (10, 56)]

        # WHEN
        result = grid.filter_invalid_cells(cells_to_filter)

        # ASSERT
        assert len(result) == 2
        assert result == [(2, 4), (23, 4)]
