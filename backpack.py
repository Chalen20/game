from tkinter import *
from PIL import Image, ImageTk
from math import *
class Backpack:
    def __init__(self, root, canvas, x, y):
        self.items = []
        front_skin1 = Image.open("img/Pers1.png")
        front_skin1 = front_skin1.resize((100, 100), Image.ANTIALIAS)
        front_skin1 = ImageTk.PhotoImage(front_skin1)
        for i in range(33):
            self.items.append(front_skin1)
        self.canvas = canvas
        self.x = x
        self.y = y
        self.root = root
        self.build_backpack()
        self.buildItems()

    def build_backpack(self):
        self.frame = Frame(self.root, width=600, height=600, bg="green")
        self.frame.place(x=100, y=100)
        self.canvas2 = Canvas(self.frame, width=400, height=600, bg="red")
        self.canvas2.place(x=0, y=0)
        if len(self.items) > 24:
            self.canvas2.configure(scrollregion=(0, 0, 400, ceil(len(self.items)/4*100 + 100)))
            self.canvas2.bind("<ButtonPress-1>", self.scroll_start)
            self.canvas2.bind("<B1-Motion>", self.scroll_move)
        if len(self.items) > 24:
            for i in range(4):
                for j in range(ceil(len(self.items)/4)):
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

    def remove(self):
        self.frame.destroy()

    def delete_spaces(self, items):
        items2 = []
        for i in items:
            if i != "":
                items2.append(i)
        return items2

    def buildItems(self):
        if len(self.items) <= 4:
            for i in range(len(self.items)):
                self.canvas2.create_image(i * 100 + 50, 50, image=self.items[i])
        else:
            for i in range(4):
                for j in range(floor(len(self.items)/4)):
                    self.canvas2.create_image(i * 100 + 50, j * 100 + 50, image=self.items[i])
            if len(self.items)/4 > floor(len(self.items)/4):
                x = int(4 * (len(self.items)/4 - floor(len(self.items)/4)))
                for i in range(x):
                    self.canvas2.create_image(i * 100 + 50, floor(len(self.items)/4) * 100 + 50, image=self.items[i])