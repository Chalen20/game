from tkinter import *
from math import *
from PIL import Image, ImageTk
from item import ItemController
class Ammunition:
    def __init__(self, root, gui, allItems):
        equip = Image.open("img/equip.png")
        equip = equip .resize((150, 50), Image.ANTIALIAS)
        self.equip = ImageTk.PhotoImage(equip)
        self.allItems = allItems
        self.amunition = gui.ammunition
        self.root = root
        self.is_Open = False
        self.allItems = allItems
        self.equiped = gui.equipment

    def start(self):
        self.build_amunition()
        self.is_Open = True
        self.buildItems()
        self.buildEquiped()

    def build_amunition(self):
        self.frame = Frame(self.root, width=600, height=600, bg="red")
        self.frame.place(x=100, y=100)
        self.canvas2 = Canvas(self.frame, width=400, height=600, bg="lightgreen")
        self.canvas2.place(x=0, y=0)
        self.canvas3 = Canvas(self.frame, width=200, height=600, bg="white")
        self.canvas3.place(x=400, y=0)
        self.tiles = []
        if len(self.amunition) > 24:
            self.canvas2.configure(scrollregion=(0, 0, 400, ceil(len(self.amunition) / 4 * 100 + 100)))
            self.canvas2.bind("<ButtonPress-1>", self.scroll_start)
            self.canvas2.bind("<B1-Motion>", self.scroll_move)
        if len(self.amunition) > 24:
            for i in range(4):
                if ceil(len(self.amunition) / 4) < 100:
                    for j in range(ceil(len(self.amunition) / 4)):
                        a = self.canvas2.create_rectangle(i * 100 + 5, j * 100 + 5, i * 100 + 95,
                                                          j * 100 + 95, fill="green", tag="rect")
                        self.tiles.append(a)
        else:
            for i in range(4):
                for j in range(6):
                    a = self.canvas2.create_rectangle(i * 100 + 5, j * 100 + 5, i * 100 + 95,
                                                    j * 100 + 95, fill="green", tag="rect")
                    self.tiles.append(a)
        self.canvas2.lift("rect")

        for i in range(5):
            if i != 2:
                self.canvas3.create_rectangle(55, i * 100 + 5, 145,
                                          i * 100 + 95, fill="lightgreen", tag="equiped")
            else:
                self.canvas3.create_rectangle(5, 205, 95,
                                              295, fill="lightgreen", tag="equiped")
                self.canvas3.create_rectangle(105, 205, 195,
                                              295, fill="lightgreen", tag="equiped")

    def scroll_start(self, event):
        self.canvas2.scan_mark(event.x, event.y)

    def buildItems(self):
        if len(self.amunition) <= 4:
            for i in range(len(self.amunition)):
                self.canvas2.create_image(i * 100 + 50, 50, image=self.amunition[i][0], tag=self.amunition[i][2])
                self.canvas2.tag_bind(self.amunition[i][2], "<Button-1>",
                                      lambda event, x=i: self.select_item(event, x))
        else:
            for i in range(4):
                for j in range(floor(len(self.amunition) / 4)):
                    self.canvas2.create_image(i * 100 + 50, j * 100 + 50,
                                              image=self.amunition[4 * (j - 1) + i][0],
                                              tag=self.amunition[4 * (j - 1) + i][2])
                    self.canvas2.tag_bind(self.amunition[4 * (j - 1) + i][2], "<Button-1>",
                                          lambda event, x=4 * (j - 1) + i: self.select_item(event, x))
            if len(self.amunition) / 4 > floor(len(self.amunition) / 4):
                x = int(4 * (len(self.amunition) / 4 - floor(len(self.amunition) / 4)))
                for i in range(x):
                    self.canvas2.create_image(i * 100 + 50, floor(len(self.amunition) / 4) * 100 + 50,
                                              image=self.amunition[len(self.amunition) - i - 5][0],
                                              tag=self.amunition[len(self.amunition) - i - 5][2])
                    self.canvas2.tag_bind(self.amunition[len(self.amunition) - i - 1][2], "<Button-1>",
                                          lambda event, x=len(self.amunition) - i - 1: self.select_item(event, x))
        self.item = self.canvas3.create_rectangle(0, 0, 0, 0)

    def buildEquiped(self):
        for i in self.equiped:
            if self.equiped[i] != []:
                if i == "weapon":
                    self.canvas3.create_image(50, 250, image=self.equiped[i][0], tag="weapon")
                elif i == "shield":
                    self.canvas3.create_image(150, 250, image=self.equiped[i][0], tag="shield")
                elif i == "helmet":
                    self.canvas3.create_image(100, 50, image=self.equiped[i][0], tag="helmet")
                elif i == "mail":
                    self.canvas3.create_image(100, 150, image=self.equiped[i][0], tag="mail")
                elif i == "hands":
                    self.canvas3.create_image(100, 350, image=self.equiped[i][0], tag="hands")
                elif i == "boots":
                    self.canvas3.create_image(100, 450, image=self.equiped[i][0], tag="boots")

    def select_item(self, event, x):
        equip = self.canvas3.create_image(100, 540, image=self.equip)
        self.canvas3.tag_bind(equip, "<Button-1>", lambda event, z=x: self.equip_func(event, z))

    def equip_func(self, event, x):
        y = self.amunition[x][2]
        image = self.allItems[y][0]
        tag = self.allItems[y][3]
        if tag == "weapon":
            self.canvas3.delete("weapon")
            self.canvas3.create_image(50, 250, image=image, tag="weapon")
            self.equiped['weapon'] = self.allItems[y]
        elif tag == "shield":
            self.canvas3.delete("shield")
            self.canvas3.create_image(150, 250, image=image, tag="shield")
            self.equiped['shield'] = self.allItems[y]
        elif tag == "helmet":
            self.canvas3.delete("helmet")
            self.canvas3.create_image(100, 50, image=image, tag="helmet")
            self.equiped['helmet'] = self.allItems[y]
        elif tag == "mail":
            self.canvas3.delete("mail")
            self.canvas3.create_image(100, 150, image=image, tag="mail")
            self.equiped['mail'] = self.allItems[y]
        elif tag == "hands":
            self.canvas3.delete("hands")
            self.canvas3.create_image(100, 350, image=image, tag="hands")
            self.equiped['hands'] = self.allItems[y]
        elif tag == "boots":
            self.canvas3.delete("boots")
            self.canvas3.create_image(100, 450, image=image, tag="boots")
            self.equiped['boots'] = self.allItems[y]

    def scroll_move(self, event):
        self.canvas2.scan_dragto(event.x, event.y, gain=1)

    def remove(self):
        self.frame.destroy()
        self.is_Open = False