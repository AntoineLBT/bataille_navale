from controller.grid import Grid

if __name__ == "__main__":
    grid = Grid(20, 20)
    grid.create_empty_grid()
    grid.fill_grid()
    print(grid)
