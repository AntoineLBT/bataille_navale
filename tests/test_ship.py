from controller.ship import Ship, Cruiser, Escort, Torpedo, SubMarine
import pytest


@pytest.fixture(scope="function")
def vertical():
    return "vertical"


@pytest.fixture(scope="function")
def horizontal():
    return "horizontal"


class TestShip:
    @staticmethod
    def test_ship_constructor():

        # GIVEN
        attributes = ["size", "x_position", "y_position", "orientation", "color"]

        # WHEN
        ship = Ship(4, 1, 5, "vertical")

        # ASSERT
        for attribute in attributes:
            assert attribute in ship.__dict__


class TestOtherShips:
    @staticmethod
    @pytest.mark.parametrize(
        "ship_class, color",
        [
            (Cruiser, "#ff0000"),
            (Escort, "#33cc33"),
            (Torpedo, "#e6e600"),
            (SubMarine, "#0000ff"),
        ],
    )
    def test_inheritance(vertical, ship_class, color):

        # GIVEN
        ship = ship_class(2, 10, vertical)

        # ASSERT
        assert issubclass(ship_class, Ship)
        assert ship.x_position == 2
        assert ship.y_position == 10
        assert ship.orientation == vertical
        assert ship.color == color
