from controller.cell import Cell


class TestCell:
    @staticmethod
    def test_constructor():

        # WHEN
        cell = Cell(2, 10)

        # ASSERT
        assert cell.x_position == 2
        assert cell.y_position == 10
        assert cell.ship_class is None
        assert cell.is_empty is True
        assert cell.color == "#ffffff"
