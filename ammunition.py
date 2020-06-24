from tkinter import *
from math import *
from PIL import Image, ImageTk
class Ammunition:
    def __init__(self, root, canvas, pers, x, y):
        self.amunition = []
        self.x = x
        self.y = y
        self.root = root
        self.canvas = canvas
        self.pers = pers

    def build_amunition(self):
        self.frame = Frame(self.root, width=600, height=600, bg="red")
        self.frame.place(x=100, y=100)
        self.canvas2 = Canvas(self.frame, width=400, height=600, bg="lightblue")
        self.canvas2.place(x=0, y=0)
        self.canvas3 = Canvas(self.frame, width=200, height=200, bg="white")
        self.canvas3.place(x=400, y=100)
        if len(self.amunition) > 24:
            self.canvas2.configure(scrollregion=(0, 0, 400, ceil(len(self.amunition) / 4 * 100 + 100)))
            self.canvas2.bind("<ButtonPress-1>", self.scroll_start)
            self.canvas2.bind("<B1-Motion>", self.scroll_move)
        if len(self.amunition) > 24:
            for i in range(4):
                if ceil(len(self.amunition) / 4) < 100:
                    for j in range(ceil(len(self.amunition) / 4)):
                        self.canvas2.create_rectangle(i * 100 + 5, j * 100 + 5, i * 100 + 95,
                                                          j * 100 + 95, fill="orange", tag="rect")
            else:
                for i in range(4):
                    for j in range(6):
                        self.canvas2.create_rectangle(i * 100 + 5, j * 100 + 5, i * 100 + 95,
                                                      j * 100 + 95, fill="orange", tag="rect")
            self.canvas2.lift("rect")

    def scroll_start(self, event):
        self.canvas2.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas2.scan_dragto(event.x, event.y, gain=1)