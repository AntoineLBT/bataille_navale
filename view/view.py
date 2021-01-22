import tkinter as tk


class View:
    def __init__(self):
        self.root = tk.Tk()

        c = tk.Canvas(self.root, height=100, width=100, bg="white")
        c.pack(fill=tk.BOTH, expand=True)
