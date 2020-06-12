from random import *

allWeapons = {"ax1": [PhotoImage(file='img/weapon/Ax.png'), 10, 0.05],
              "ax2": [PhotoImage(file='img/weapon/Ax2.png'), 11, 0.051],
              "sword1": [PhotoImage(file='img/weapon/Sword1.png'), 5, 0.1],
              "sword2": [PhotoImage(file='img/weapon/Sword2.png'), 11, 0.051}

class Weapon():
    def __init__(self, name):
        self.skin = allWeapons[name][0]
        self.name = name
        self.uses = "weapon"
        self.coords = {}
        self.coords.x = 0
        self.coords.y = 0
        self.fracture_of_weapon = 0
        self.coefficient = allWeapons[name][3]
        self.isBroken = False
        self.value = randint(0.7 * allWeapons[self.name][1], 1.3 * allWeapons[self.name][1])

    def broke(self):
        self.value = 0
        self.fracture_of_weapon = 100
        self.isBroken = True

    def fracture(self):
        if self.fracture_of_weapon + self.value * self.coefficient >= 100:
            self.broke()
            return
        else:
            self.fracture_of_weapon += self.value * self.coefficient