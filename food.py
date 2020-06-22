from random import *
from tkinter import *
from PIL import ImageTk, Image
from math import *
class Food():
    def __init__(self, name):
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

        allFoods = {"apple": [apple, apple_big, 10, 0.05, True],
                    "apple2": [apple2, apple_big2, 10, 0.05, True],
                    "bear": [bear, bear_big, 10, 0.055, True],
                    "borshch": [borshch, borshch_big, 50, 0.035, True],
                    "cheese": [cheese, cheese_big, 25, 0.04, True],
                    "chocolate": [chocolate, chocolate_big, 25, 0.045, True],
                    "close_pan": [close_pan, close_pan_big, 25, 0.01, True],
                    "egg": [egg, egg_big, 15, 0.04, True],
                    "empty_pan": [empty_pan, empty_pan_big, 0, 0, False],
                    "fish": [fish, fish_big, 20, 0.035, True],
                    "honey": [honey, honey_big, 25, 0, False],
                    "kiwi": [kiwi, kiwi_big, 15, 0.03, True],
                    "lemon": [lemon, lemon_big, 10, 0.02, True],
                    "mushroom": [mushroom, mushroom_big, 20, 0.04, False],
                    "orange": [orange, orange_big, 10, 0.04, True],
                    "pizza": [pizza, pizza_big, 20, 0.025, True],
                    "varenics": [varenics, varenics_big, 50, 0.04, True],
                    "watermelon": [watermelon, watermelon_big, 15, 0.035, True],
                    "meat": [meat, meat_big, 20, 0.04, True]}
        self.skin = allFoods[name][0]
        self.name = name
        self.uses = "food"
        self.coords = {}
        self.coords["x"] = 0
        self.coords["y"] = 0
        self.rotten = 0
        self.allFoods = allFoods
        self.rottenness = allFoods[name][4]
        self.coefficient = allFoods[name][3]
        self.isEaten = False
        self.value = randint(floor(0.7 * allFoods[self.name][2]), floor(1.3 * allFoods[self.name][2]))

    def eaten(self):
        self.value = 0
        self.isEaten = True

    def rottenness(self):
        if self.rottenness and self.rotten + self.value * self.coefficient >= 100:
            self.eaten()
            return
        elif self.rottenness and self.rotten + self.value * self.coefficient < 100:
            self.rotten += self.value * self.coefficient