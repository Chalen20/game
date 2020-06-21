from tkinter import *
from PIL import Image, ImageTk
from math import *
class Backpack:
    def __init__(self, canvas, x, y):
        self.items = []
        front_skin1 = Image.open("img/Pers1.png")
        front_skin1 = front_skin1.resize((100, 100), Image.ANTIALIAS)
        front_skin1 = ImageTk.PhotoImage(front_skin1)
        for i in range(50):
            self.items.append(front_skin1)
        self.canvas = canvas
        self.x = x
        self.y = y
        self.build_backpack()

    def build_backpack(self):
        self.rect = self.canvas.create_rectangle(self.x+400, self.y, self.x+600, self.y+600, fill="blue")
        self.canvas.lift(self.rect)
        if len(self.items) > 24:
            for i in range(4):
                for j in range(ceil(len(self.items)/4)):
                    self.canvas.create_rectangle(self.x + i * 100 + 5, self.y + j * 100 + 5, self.x + i * 100 + 90,
                                                 self.y + j * 100 + 90, fill="orange", tag="rect")
                    #print(i, j)
        else:
            for i in range(4):
                for j in range(6):
                    self.canvas.create_rectangle(self.x + i * 100 + 5, self.y + j * 100 + 5, self.x + i * 100 + 90,
                                                 self.y + j * 100 + 90, fill="orange", tag="rect")
                    #print(i, j)
    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def remove(self):
        self.canvas.delete(self.rect)
        #self.canvas.delete("rect")

    def buildItems(self):
        for i in range(len(self.items)-1):
            self.canvas.create_image(self.x + i, self.y + i, image=items[i])