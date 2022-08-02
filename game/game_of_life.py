from tkinter import *

root = Tk()
root_width, root_height = 800, 800
root.geometry(f"{str(root_width)}x{str(root_height)}")
canvas = Canvas(root)

cell_width, cell_height = 80, 80

class Cell:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.color = "BLACK"
        self.cell_width, self.cell_height = 80, 80

        self.cell_label = Label(canvas, bg=self.color, width=int(root_width/cell_width), height=int(root_width/cell_width))
        self.cell_label.place(x=80*posx, y=80*posy)

cell_map = [Cell(posx, posy) for posy in range(cell_height) for posx in range(cell_width)]


def close_win():
    root.destroy()
root.bind("<Escape>", lambda: close_win())


root.mainloop()
