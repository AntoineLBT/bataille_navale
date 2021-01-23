import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


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

        self.size = None

        self.grid_frame = tk.Frame(
            self.root, bg="skyblue", width=View.GRID_WIDTH, height=View.GRID_HEIGHT
        )
        self.grid_frame.pack(fill=tk.BOTH, expand=1)

    def action(self, event):
        size = self.list_combo.get()
        if len(size) == 0:
            self.popup()
            return None
        size_list = size.split("x")

        self.size = (int(size_list[0]), int(size_list[1]))
        print(self.size)

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
        if self.size is None:
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

        for x in range(
            x_start_grid, (self.size[0] * View.CELL_SIZE) + x_start_grid, View.CELL_SIZE
        ):
            for y in range(
                y_start_grid,
                (self.size[1] * View.CELL_SIZE) + y_start_grid,
                View.CELL_SIZE,
            ):
                canvas.create_rectangle(x, y, x + View.CELL_SIZE, y + View.CELL_SIZE)
                print(x, y)
        canvas.pack(fill=tk.BOTH, padx=5, pady=5)

    def calculate_grid_position(self):

        grid_width = self.size[0] * View.CELL_SIZE
        x_start_grid = (View.GRID_WIDTH - grid_width) / 2

        grid_height = self.size[1] * View.CELL_SIZE
        y_start_grid = (View.GRID_HEIGHT - grid_height) / 2

        return x_start_grid, y_start_grid
