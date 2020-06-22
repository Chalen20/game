from random import *
from PIL import Image, ImageTk

class Item:
    def __init__(self, skin, bigSkin, name):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name

class Food(Item):
    def __init__(self, skin, bigSkin, name, satiety, *args):
        Item(skin, bigSkin, name)
        self.rottness = 100
        self.satiety = satiety
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
                 "apple", 10, 0.05)]

    def getImage(self, name, big):
        img = Image.open(name)
        if big:
            img = img.resize((200, 200), Image.ANTIALIAS)

        else:
            img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def drop(self, canvas, pers_x, pers_y):
        canvas.create_image(pers_x, pers_y, image=self.possibleItems[0])

#class Armor(Item):
#class Weapon(Item):
#class Poitions(Item):