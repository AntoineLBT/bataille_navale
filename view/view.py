import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class View:

    SIZE_CHOICE = ["15x15", "20x20", "25x25", "30x30"]

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.maxsize(1000, 800)
        self.root.title("Bataille Navale")
        self.root.config(bg="skyblue")

        button_frame = tk.Frame(self.root, bg="grey").pack(fill="both", padx=5, pady=5)
        load = Image.open(
            "/home/antoine/PycharmProjects/bataille_navale/view/reshape_bg.jpg"
        )
        render = ImageTk.PhotoImage(load)
        img = tk.Label(button_frame, image=render)
        img.image = render
        img.pack()

        ttk.Combobox(button_frame, values=View.SIZE_CHOICE).pack(padx=5, pady=5)
        tk.Button(button_frame, text="Generate").pack(padx=5, pady=5)
