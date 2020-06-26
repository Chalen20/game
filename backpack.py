from tkinter import *
from math import *
from PIL import Image, ImageTk
from ammunition import Ammunition
class Backpack:
    def __init__(self, root, pers, satiety, gui, allItems):
        self.items = gui.items
        self.gui = gui
        self.allItems = allItems

        throw_out = Image.open("img/throw_out.png")
        throw_out = throw_out.resize((100, 50), Image.ANTIALIAS)
        self.throw_out = ImageTk.PhotoImage(throw_out)

        eat = Image.open("img/eat.png")
        eat = eat.resize((50, 25), Image.ANTIALIAS)
        self.eater = ImageTk.PhotoImage(eat)

        equip = Image.open("img/equip.png")
        equip = equip.resize((75, 25), Image.ANTIALIAS)
        self.equiper = ImageTk.PhotoImage(equip)

        self.allItems = allItems
        self.root = root
        self.pers = pers
        self.satiety = satiety
        self.is_Open = False

    def start(self):
        self.build_backpack()
        self.buildItems()
        self.is_Open = True

    def build_backpack(self):
        self.frame = Frame(self.root, width=600, height=600, bg="green")
        self.frame.place(x=100, y=100)
        self.canvas2 = Canvas(self.frame, width=400, height=600, bg="red")
        self.canvas2.place(x=0, y=0)
        self.canvas3 = Canvas(self.frame, width=200, height=200, bg="white")
        self.canvas3.place(x=400, y=100)
        self.canvas4 = Canvas(self.frame, width=200, height=100)
        self.canvas4.place(x=400, y=400)
        if len(self.items) > 24:
            self.canvas2.configure(scrollregion=(0, 0, 400, ceil(len(self.items)/4*100 + 100)))
            self.canvas2.bind("<ButtonPress-1>", self.scroll_start)
            self.canvas2.bind("<B1-Motion>", self.scroll_move)
        if len(self.items) > 24:
            for i in range(4):
                if ceil(len(self.items)/4) < 100:
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
        self.is_Open = False

    def buildItems(self):
        if len(self.items) <= 4:
            for i in range(len(self.items)):
                self.canvas2.create_image(i * 100 + 50, 50, image=self.items[i][0], tag=self.items[i][2])
                self.canvas2.tag_bind(self.items[i][2], "<Button-1>",
                                      lambda event, x=i: self.select_item(event, x))
        else:
            for i in range(4):
                for j in range(floor(len(self.items)/4)):
                    self.canvas2.create_image(i * 100 + 50, j * 100 + 50,
                                              image=self.items[4*(j-1)+i][0], tag=self.items[4*(j-1)+i][2])
                    self.canvas2.tag_bind(self.items[4*(j-1)+i][2], "<Button-1>",
                                          lambda event, x=4*(j-1)+i: self.select_item(event, x))
            if len(self.items)/4 > floor(len(self.items)/4):
                x = int(4 * (len(self.items)/4 - floor(len(self.items)/4)))
                for i in range(x):
                    self.canvas2.create_image(i * 100 + 50, floor(len(self.items)/4) * 100 + 50,
                                              image=self.items[len(self.items)-i-5][0],
                                              tag=self.items[len(self.items)-i-5][2])
                    self.canvas2.tag_bind(self.items[len(self.items)-i-1][2], "<Button-1>",
                                          lambda event, x=len(self.items)-i-1: self.select_item(event, x))
        self.item = self.canvas3.create_rectangle(0, 0, 0, 0)

    def select_item(self, event, x):
        
        self.canvas3.delete(self.item)
        y = self.items[x][2]
        #print(y)
        image = self.allItems[y][1]
        self.item = self.canvas3.create_image(100, 100, image=image)
        throw_out = self.canvas4.create_image(50, 50, image=self.throw_out)
        self.canvas4.create_image(150, 50, image=self.eater, tag="eat")
        self.canvas4.delete("eat")
        self.canvas4.create_image(150, 50, image=self.equiper, tag="equip")
        self.canvas4.delete("equip")
        self.canvas4.create_text(150, 50, text="use", font="Impact 25", tag="use")
        self.canvas4.delete("use")
        if self.allItems[y][3] == "food":
            self.eat = self.canvas4.create_image(150, 50, image=self.eater, tag="eat")
            self.canvas4.tag_bind(self.eat, "<Button-1>", lambda event, z=x: self.eat_func(event, z))
        elif self.allItems[y][3] == "helmet" or self.allItems[y][3] == "mail" or self.allItems[y][3] == "hands" or\
                self.allItems[y][3] == "boots" or self.allItems[y][3] == "shield" or self.allItems[y][3] == "weapon":
            self.equip = self.canvas4.create_image(150, 50, image=self.equiper, tag="equip")
            self.canvas4.tag_bind(self.equip, "<Button-1>", lambda event, z=x: self.equip_func(event, z))
        elif self.allItems[y][3] == "poition":
            self.use = self.canvas4.create_text(150, 50, text="use", font="Impact 25", tag="use")
            self.canvas4.tag_bind(self.use, "<Button-1>", lambda event, z=x: self.use_func(event, z))
        self.canvas4.tag_bind(throw_out, "<Button-1>", lambda event, z=x: self.throw_out_func(event, z))

    def equip_func(self, event, x):
        self.armor_window = Ammunition(self.root, self.gui, self.allItems)
        self.gui.equipment[self.items[x][3]] = self.items[x]

    def use_func(self, event, x):
        if self.items[x][2] == "potion_red1":
            self.pers.health += 10
            self.gui.health.change(self.pers.health)
            self.throw_out_func(event, x)
        if self.items[x][2] == "potion_red4":
            self.pers.health += 25
            self.gui.health.change(self.pers.health)
            self.throw_out_func(event, x)
        if self.items[x][2] == "potion_blue1":
            self.pers.speed += 5
            self.gui.speed += 5
            self.throw_out_func(event, x)
            self.gui.canvas.after(15000, self.return_speed1)
        if self.items[x][2] == "potion_blue4":
            self.pers.speed += 10
            self.gui.speed += 10
            self.throw_out_func(event, x)
            self.gui.canvas.after(30000, self.return_speed4)
        if self.items[x][2] == "potion_orange1":
            self.pers.power += 5
            print(self.pers.power)
            self.throw_out_func(event, x)
            self.gui.canvas.after(15000, self.return_power1)
        if self.items[x][2] == "potion_orange4":
            self.pers.power += 10
            self.throw_out_func(event, x)
            self.gui.canvas.after(30000, self.return_power4)
        if self.items[x][2] == "potion2":
            
            self.gui.minimap.lifter()
            self.throw_out_func(event, x)
            self.gui.canvas.after(120000, self.return_Pause)

    def return_speed1(self):
        self.pers.speed -= 5
        self.gui.speed -= 5

    def return_speed4(self):
        self.pers.speed -= 10
        self.gui.speed -= 10

    def return_power1(self):
        self.pers.power -= 5
        print(self.pers.power)

    def return_power4(self):
        self.pers.power -= 10
        print(self.pers.power)

    def return_Pause(self):
        self.gui.minimap.lowerer()

    def throw_out_func(self, event, x):
        del self.items[x]
        self.remove()
        self.build_backpack()
        self.buildItems()

    def eat_func(self, event, x):
        self.pers.satiety += self.allItems[self.items[x][2]][4]
        self.satiety.change(self.pers.satiety)
        self.throw_out_func(event, x)
