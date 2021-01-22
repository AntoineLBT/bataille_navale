from controller.grid import Grid
from view.view import View

if __name__ == "__main__":
    grid = Grid(20, 20)
    grid.create_empty_grid()
    grid.fill_grid()
    print(grid)
    view = View()
    view.root.mainloop()
