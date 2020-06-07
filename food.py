from random import *

allFoods = {"name1": ["skin", "arr_nutritional_value", "rotten_skin", "coefficient_of_rotten", "rottenness (є продукти, які взагалі не псуються)"]}

class Food():
    def __init__(self, name):
        self.skin = allFoods[name][0]
        self.name = name
        self.uses = "food"
        self.coords = {}
        self.coords.x = 0
        self.coords.y = 0
        self.rotten_skin = allFoods[name][2]
        self.rottenness = allFoods[name][4]
        self.coefficient = allFoods[name][3]
        self.isEaten = False
        self.value = randint(0.7 * allFoods[self.name][1], 1.3 * allFoods[self.name][1])

    def eaten(self):
        self.value = 0
        self.isEaten = True

    def rottenness(self):
        if self.rottenness + self.value * self.coefficient >= 100:
            self.eaten()
            return
        else:
            self.rottenness += self.value * self.coefficient