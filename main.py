from grid.grid import Grid

if __name__ == "__main__":
    grid = Grid(10, 5)
    grid.create_empty_grid()
    grid.fill_grid()
    print(grid)
