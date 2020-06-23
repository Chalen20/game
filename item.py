from random import *
from PIL import Image, ImageTk

class Food:
    def __init__(self, skin, bigSkin, name, satiety, item, *args):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name
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
            Food(self.getImage("img/food/apple.png", False), self.getImage("img/food/apple.png", True),
                 "apple", 10, "food", 0.05),
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
        a = canvas.create_image(pers_x, pers_y, image=self.possibleItems[x].skin)

#class Armor(Item):
#class Weapon(Item):
#class Poitions(Item):