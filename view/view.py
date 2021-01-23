import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from controller.grid import Grid
from controller.cell import Cell


class View:

    SIZE_CHOICE = ["", "15x15", "20x20", "25x25", "30x30"]
    GRID_WIDTH = 600
    GRID_HEIGHT = 700
    CELL_SIZE = 20

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x900+900+10")
        self.root.maxsize(1000, 900)
        self.root.title("Bataille Navale")
        self.root.config(bg="skyblue")

        self.button_frame = tk.Frame(self.root, bg="skyblue")
        self.button_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        load = Image.open(
            "/home/antoine/PycharmProjects/bataille_navale/view/reshape_bg.jpg"
        )
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.button_frame, image=render)
        img.image = render
        img.pack()

        self.list_combo = ttk.Combobox(self.button_frame, values=View.SIZE_CHOICE)
        self.list_combo.current(0)
        self.list_combo.pack(padx=5, pady=5)
        self.list_combo.bind("<<ComboboxSelected>>", self.action)
        tk.Button(self.button_frame, text="Generate", command=self.generate_grid).pack(
            padx=5, pady=5
        )

        self.chosen_size = None

        self.grid_frame = tk.Frame(
            self.root, bg="skyblue", width=View.GRID_WIDTH, height=View.GRID_HEIGHT
        )
        self.grid_frame.pack(fill=tk.BOTH, expand=1)

        self.grid_object = Grid(0, 0)

    def action(self, event):
        size = self.list_combo.get()
        if len(size) == 0:
            self.popup()
            return None
        size_list = size.split("x")

        self.chosen_size = (int(size_list[0]), int(size_list[1]))
        print(self.chosen_size)

    def popup(self):
        pop_up = tk.Toplevel()
        pop_up.title("Attention")
        tk.Label(
            pop_up,
            text="Choisissez une dimension de grille valide\ndans la liste déroulante ci-dessus.",
        ).pack(padx=10, pady=10)
        tk.Button(pop_up, text="OK", command=pop_up.destroy).pack(padx=10, pady=10)
        pop_up.transient(self.root)
        pop_up.grab_set()
        self.root.wait_window(pop_up)

    def generate_grid(self):
        if self.chosen_size is None:
            self.popup()
            return None

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(
            self.grid_frame,
            width=View.GRID_WIDTH,
            height=View.GRID_HEIGHT,
            bg="skyblue",
        )

        x_start_grid, y_start_grid = self.calculate_grid_position()
        x_start_grid = int(x_start_grid)
        y_start_grid = int(y_start_grid)

        self.initialize_grid_object()

        for x, x_in_px in enumerate(
            range(
                x_start_grid,
                (self.chosen_size[0] * View.CELL_SIZE) + x_start_grid,
                View.CELL_SIZE,
            )
        ):
            for y, y_in_px in enumerate(
                range(
                    y_start_grid,
                    (self.chosen_size[1] * View.CELL_SIZE) + y_start_grid,
                    View.CELL_SIZE,
                )
            ):

                cell = self.grid_object.grid[y][x]
                canvas.create_rectangle(
                    x_in_px,
                    y_in_px,
                    x_in_px + View.CELL_SIZE,
                    y_in_px + View.CELL_SIZE,
                    fill=cell.color,
                )
                print(x_in_px, y_in_px)
        canvas.pack(fill=tk.BOTH, padx=5, pady=5)

    def calculate_grid_position(self):

        grid_width = self.chosen_size[0] * View.CELL_SIZE
        x_start_grid = (View.GRID_WIDTH - grid_width) / 2

        grid_height = self.chosen_size[1] * View.CELL_SIZE
        y_start_grid = (View.GRID_HEIGHT - grid_height) / 2

        return x_start_grid, y_start_grid

    def initialize_grid_object(self):

        self.grid_object = Grid(self.chosen_size[0], self.chosen_size[1])
        self.grid_object.create_empty_grid()
        self.grid_object.fill_grid()