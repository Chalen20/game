from random import *
from PIL import Image, ImageTk

class Item:
    def __init__(self, skin, bigSkin, name):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name

class Food(Item):
    def __init__(self, skin, bigSkin, name, satiety, item, *args):
        Item(skin, bigSkin, name)
        self.rottness = 100
        self.satiety = satiety
        self.item = item
        if (len(args) > 0):
            self.canRott = True
            self.rotteRate = args[0]
            # self.rottness=100
        else:
            self.canRott = False

    def rotten(self):
        if (self.canRott):
            self.rottness -= self.rotteRate
        if (self.rottness <= 0):
            return True
        return False

class ItemController:
    def __init__(self):
        self.possibleItems = [
            Food(self.getImage("img/food/Food_apple.png", False), self.getImage("img/food/Food_apple.png", True),
                 "apple", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_apple2.png", False), self.getImage("img/food/Food_apple2.png", True),
                 "apple2", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_bear.png", False), self.getImage("img/food/Food_bear.png", True),
                 "bear", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_borshch.png", False), self.getImage("img/food/Food_borshch.png", True),
                 "borshch", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_cake.png", False), self.getImage("img/food/Food_cake.png", True),
                 "cheese", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_close_pan.png", False), self.getImage("img/food/Food_close_pan.png", True),
                 "close_pan", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_chocolate.png", False), self.getImage("img/food/Food_chocolate.png", True),
                 "chocolate", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_egg.png", False), self.getImage("img/food/Food_egg.png", True),
                 "egg", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_empty_pan.png", False), self.getImage("img/food/Food_empty_pan.png", True),
                 "empty_pan", 10, 0.05, "food"),
            Food(self.getImage("img/food/Food_cake.png", False), self.getImage("img/food/Food_cake.png", True),
                 "cheese", 10, 0.05, "food"),
        ]

    def getImage(self, name, big):
        img = Image.open(name)
        if big:
            img = img.resize((200, 200), Image.ANTIALIAS)

        else:
            img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def drop(self, canvas, pers_x, pers_y):
        x = randint(0, len(self.possibleItems)-1)
        canvas.create_image(pers_x, pers_y, image=self.possibleItems[x])

#class Armor(Item):
#class Weapon(Item):
#class Poitions(Item):