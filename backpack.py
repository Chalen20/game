from tkinter import *
from math import *
from PIL import Image, ImageTk
class Backpack:
    def __init__(self, root, canvas, x, y):
        self.items = []
        apple = Image.open("img/food/Food_apple.png")
        apple = apple.resize((100, 100), Image.ANTIALIAS)
        apple_big = apple.resize((200, 200), Image.ANTIALIAS)
        apple_big = ImageTk.PhotoImage(apple_big)
        apple = ImageTk.PhotoImage(apple)

        apple2 = Image.open("img/food/Food_apple2.png")
        apple2 = apple2.resize((100, 100), Image.ANTIALIAS)
        apple_big2 = apple2.resize((200, 200), Image.ANTIALIAS)
        apple_big2 = ImageTk.PhotoImage(apple_big2)
        apple2 = ImageTk.PhotoImage(apple2)

        bear = Image.open("img/food/Food_bear.png")
        bear = bear.resize((100, 100), Image.ANTIALIAS)
        bear_big = bear.resize((200, 200), Image.ANTIALIAS)
        bear_big = ImageTk.PhotoImage(bear_big)
        bear = ImageTk.PhotoImage(bear)

        borshch = Image.open("img/food/Food_borshch.png")
        borshch = borshch.resize((100, 100), Image.ANTIALIAS)
        borshch_big = borshch.resize((200, 200), Image.ANTIALIAS)
        borshch_big = ImageTk.PhotoImage(borshch_big)
        borshch = ImageTk.PhotoImage(borshch)

        cheese = Image.open("img/food/Food_cake.png")
        cheese = cheese.resize((100, 100), Image.ANTIALIAS)
        cheese_big = cheese.resize((200, 200), Image.ANTIALIAS)
        cheese_big = ImageTk.PhotoImage(cheese_big)
        cheese = ImageTk.PhotoImage(cheese)

        close_pan = Image.open("img/food/Food_close_pan.png")
        close_pan = close_pan.resize((100, 100), Image.ANTIALIAS)
        close_pan_big = close_pan.resize((200, 200), Image.ANTIALIAS)
        close_pan_big = ImageTk.PhotoImage(close_pan_big)
        close_pan = ImageTk.PhotoImage(close_pan)

        chocolate = Image.open("img/food/Food_chocolate.png")
        chocolate = chocolate.resize((100, 100), Image.ANTIALIAS)
        chocolate_big = chocolate.resize((200, 200), Image.ANTIALIAS)
        chocolate_big = ImageTk.PhotoImage(chocolate_big)
        chocolate = ImageTk.PhotoImage(chocolate)

        empty_pan = Image.open("img/food/Food_empty_pan.png")
        empty_pan = empty_pan.resize((100, 100), Image.ANTIALIAS)
        empty_pan_big = empty_pan.resize((200, 200), Image.ANTIALIAS)
        empty_pan_big = ImageTk.PhotoImage(empty_pan_big)
        empty_pan = ImageTk.PhotoImage(empty_pan)

        egg = Image.open("img/food/Food_egg.png")
        egg = egg.resize((100, 100), Image.ANTIALIAS)
        egg_big = egg.resize((200, 200), Image.ANTIALIAS)
        egg_big = ImageTk.PhotoImage(egg_big)
        egg = ImageTk.PhotoImage(egg)

        fish = Image.open("img/food/Food_fish.png")
        fish = fish.resize((100, 100), Image.ANTIALIAS)
        fish_big = fish.resize((200, 200), Image.ANTIALIAS)
        fish_big = ImageTk.PhotoImage(fish_big)
        fish = ImageTk.PhotoImage(fish)

        honey = Image.open("img/food/Food_honey.png")
        honey = honey.resize((100, 100), Image.ANTIALIAS)
        honey_big = honey.resize((200, 200), Image.ANTIALIAS)
        honey_big = ImageTk.PhotoImage(honey_big)
        honey = ImageTk.PhotoImage(honey)

        kiwi = Image.open("img/food/Food_kiwi.png")
        kiwi = kiwi.resize((100, 100), Image.ANTIALIAS)
        kiwi_big = kiwi.resize((200, 200), Image.ANTIALIAS)
        kiwi_big = ImageTk.PhotoImage(kiwi_big)
        kiwi = ImageTk.PhotoImage(kiwi)

        lemon = Image.open("img/food/Food_lemon.png")
        lemon = lemon.resize((100, 100), Image.ANTIALIAS)
        lemon_big = lemon.resize((200, 200), Image.ANTIALIAS)
        lemon_big = ImageTk.PhotoImage(lemon_big)
        lemon = ImageTk.PhotoImage(lemon)

        mushroom = Image.open("img/food/Food_mushroom.png")
        mushroom = mushroom.resize((100, 100), Image.ANTIALIAS)
        mushroom_big = mushroom.resize((200, 200), Image.ANTIALIAS)
        mushroom_big = ImageTk.PhotoImage(mushroom_big)
        mushroom = ImageTk.PhotoImage(mushroom)

        orange = Image.open("img/food/Food_orange.png")
        orange = orange.resize((100, 100), Image.ANTIALIAS)
        orange_big = orange.resize((200, 200), Image.ANTIALIAS)
        orange_big = ImageTk.PhotoImage(orange_big)
        orange = ImageTk.PhotoImage(orange)

        pizza = Image.open("img/food/Food_pizza.png")
        pizza = pizza.resize((100, 100), Image.ANTIALIAS)
        pizza_big = pizza.resize((200, 200), Image.ANTIALIAS)
        pizza_big = ImageTk.PhotoImage(pizza_big)
        pizza = ImageTk.PhotoImage(pizza)

        varenics = Image.open("img/food/Food_varenics.png")
        varenics = varenics.resize((100, 100), Image.ANTIALIAS)
        varenics_big = varenics.resize((200, 200), Image.ANTIALIAS)
        varenics_big = ImageTk.PhotoImage(varenics_big)
        varenics = ImageTk.PhotoImage(varenics)

        watermelon = Image.open("img/food/Food_watermelon.png")
        watermelon = watermelon.resize((100, 100), Image.ANTIALIAS)
        watermelon_big = watermelon.resize((200, 200), Image.ANTIALIAS)
        watermelon_big = ImageTk.PhotoImage(watermelon_big)
        watermelon = ImageTk.PhotoImage(watermelon)

        meat = Image.open("img/food/meat.png")
        meat = meat.resize((100, 100), Image.ANTIALIAS)
        meat_big = meat.resize((200, 200), Image.ANTIALIAS)
        meat_big = ImageTk.PhotoImage(meat_big)
        meat = ImageTk.PhotoImage(meat)

        allItems = {"apple": [apple, apple_big, "apple", "food"],
                    "apple2": [apple2, apple_big2, "apple2", "food"],
                    "bear": [bear, bear_big, "bear", "food"],
                    "borshch": [borshch, borshch_big, "borshch", "food"],
                    "cheese": [cheese, cheese_big, "cheese", "food"],
                    "chocolate": [chocolate, chocolate_big, "chocolate", "food"],
                    "close_pan": [close_pan, close_pan_big, "close_pan", "food"],
                    "egg": [egg, egg_big, "egg", "food"],
                    "empty_pan": [empty_pan, empty_pan_big, "empty_pan", "food"],
                    "fish": [fish, fish_big, "fish", "food"],
                    "honey": [honey, honey_big, "honey", "food"],
                    "kiwi": [kiwi, kiwi_big, "kiwi", "food"],
                    "lemon": [lemon, lemon_big, "lemon", "food"],
                    "mushroom": [mushroom, mushroom_big, "mushroom", "food"],
                    "orange": [orange, orange_big, "orange", "food"],
                    "pizza": [pizza, pizza_big, "pizza", "food"],
                    "varenics": [varenics, varenics_big, "varenics", "food"],
                    "watermelon": [watermelon, watermelon_big, "watermelon", "food"],
                    "meat": [meat, meat_big, "meat", "food"]}
        for i in range(10):
            self.items.append(allItems["orange"])
        for i in range(10):
            self.items.append(allItems["mushroom"])
        for i in range(10):
            self.items.append(allItems["kiwi"])
        self.canvas = canvas
        self.x = x
        self.y = y
        self.allItems = allItems
        self.root = root
        self.build_backpack()
        self.buildItems()

    def build_backpack(self):
        self.frame = Frame(self.root, width=600, height=600, bg="green")
        self.frame.place(x=100, y=100)
        self.canvas2 = Canvas(self.frame, width=400, height=600, bg="red")
        self.canvas2.place(x=0, y=0)
        self.canvas3 = Canvas(self.frame, width=200, height=200, bg="white")
        self.canvas3.place(x=400, y=100)
        self.canvas4 = Canvas(self.frame, width=200, height=200, bg="white")
        self.canvas4.place(x=400, y=300)
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

    def delete_spaces(self, items):
        items2 = []
        for i in items:
            if i != "":
                items2.append(i)
        return items2

    def buildItems(self):
        if len(self.items) <= 4:
            for i in range(len(self.items)):
                self.canvas2.create_image(i * 100 + 50, 50, image=self.items[i][0], tag=self.items[i][2])
                self.canvas2.tag_bind(self.items[i][2], "<Button-1>",
                                      lambda event, x=self.items[i][2]: self.select_item(event, x))
        else:
            for i in range(4):
                for j in range(floor(len(self.items)/4)):
                    self.canvas2.create_image(i * 100 + 50, j * 100 + 50,
                                              image=self.items[4*(j-1)+i][0], tag=self.items[4*(j-1)+i][2])
                    self.canvas2.tag_bind(self.items[4*(j-1)+i][2], "<Button-1>",
                                          lambda event, x=self.items[4*(j-1)+i][2]: self.select_item(event, x))
            if len(self.items)/4 > floor(len(self.items)/4):
                x = int(4 * (len(self.items)/4 - floor(len(self.items)/4)))
                for i in range(x):
                    self.canvas2.create_image(i * 100 + 50, floor(len(self.items)/4) * 100 + 50,
                                              image=self.items[len(self.items)-i-1][0],
                                              tag=self.items[len(self.items)-i-1][2])
                    self.canvas2.tag_bind(self.items[len(self.items)-i-1][2], "<Button-1>",
                                          lambda event, x=self.items[len(self.items)-i-1][2]: self.select_item(event, x))
        self.item = self.canvas3.create_rectangle(0, 0, 0, 0)

    def select_item(self, event, x):
        self.canvas3.delete(self.item)
        image = self.allItems[x][1]
        throw_out = Image.open("img/throw_out.png")
        throw_out = throw_out.resize((300, 200), Image.ANTIALIAS)
        throw_out = ImageTk.PhotoImage(throw_out)
        throw_out = self.canvas4.create_image(0, 0, image=throw_out)
        self.item = self.canvas3.create_image(100, 100, image=image)