from random import *
from tkinter import *
allFoods = {"apple": [PhotoImage(file='img/food/Food_apple.png'), 10, 0.05, True],
            "apple2": [PhotoImage(file="img/food/Food_apple2.png"), 10, 0.05, True],
            "bear": [PhotoImage(file="img/food/Food_bear.png"), 10, 0.055, True],
            "borshch": [PhotoImage(file="img/food/Food_borshch.png"), 50, 0.035, True],
            "cheese": [PhotoImage(file="img/food/Food_cake.png"), 25, 0.04, True],
            "chocolate": [PhotoImage(file="img/food/Food_chocolate.png"), 25, 0.045, True],
            "close_pan": [PhotoImage(file="img/food/Food_close_pan.png"), 25, 0.01, True],
            "egg": [PhotoImage(file="img/food/Food_egg.png"), 15, 0.04, True],
            "empty_pan": [PhotoImage(file="img/food/Food_empty_pan.png"), 0, 0, False],
            "fish": [PhotoImage(file="img/food/Food_fish.png"), 20, 0.035, True],
            "honey": [PhotoImage(file="img/food/Food_honey.png"), 25, 0, False],
            "kiwi": [PhotoImage(file="img/food/Food_kiwi.png"), 15, 0.03, True],
            "lemon": [PhotoImage(file="img/food/Food_lemon.png"), 10, 0.02, True],
            "mushroom": [PhotoImage(file="img/food/Food_mushroom.png"), 20, 0.04, False],
            "orange": [PhotoImage(file="img/food/Food_orange.png"), 10, 0.04, True],
            "pizza": [PhotoImage(file="img/food/Food_pizza.png"), 20, 0.025, True],
            "varenics": [PhotoImage(file="img/food/Food_varenics.png"), 50, 0.04, True],
            "watermelon": [PhotoImage(file="img/food/Food_watermelon.png"), 15, 0.035, True],
            "meat": [PhotoImage(file="img/food/meat.png"), 20, 0.04, True]}

class Food():
    def __init__(self, name):
        self.skin = allFoods[name][0]
        self.name = name
        self.uses = "food"
        self.coords = {}
        self.coords.x = 0
        self.coords.y = 0
        self.rotten = 0
        self.rottenness = allFoods[name][3]
        self.coefficient = allFoods[name][2]
        self.isEaten = False
        self.value = randint(0.7 * allFoods[self.name][1], 1.3 * allFoods[self.name][1])

    def eaten(self):
        self.value = 0
        self.isEaten = True

    def rottenness(self):
        if self.rottenness and self.rotten + self.value * self.coefficient >= 100:
            self.eaten()
            return
        elif self.rottenness and self.rotten + self.value * self.coefficient < 100:
            self.rotten += self.value * self.coefficient