from random import *
from PIL import Image, ImageTk
from copy import deepcopy

class Food:
    def __init__(self, skin, bigSkin, name, item, satiety, *args):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name
        self.rottness = 100
        self.satiety = satiety
        self.item = item
        if (len(args) > 0):
            self.canRott = True
            self.rotteRate = args[0]
        else:
            self.canRott = False
            self.rotteRate = 0

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
                 "apple", "food", 10, 0.05),
            Food(self.getImage("img/food/Food_apple2.png", False), self.getImage("img/food/Food_apple2.png", True),
                 "apple2", "food", 10, 0.05),
            Food(self.getImage("img/food/Food_bear.png", False), self.getImage("img/food/Food_bear.png", True),
                 "bear", "food", 10, 0.055),
            Food(self.getImage("img/food/Food_borshch.png", False), self.getImage("img/food/Food_borshch.png", True),
                 "borshch", "food", 50, 0.035),
            Food(self.getImage("img/food/Food_cake.png", False), self.getImage("img/food/Food_cake.png", True),
                 "cheese", "food", 25, 0.04),
            Food(self.getImage("img/food/Food_chocolate.png", False), self.getImage("img/food/Food_chocolate.png", True),
                 "chocolate", "food", 25, 0.045),
            Food(self.getImage("img/food/Food_close_pan.png", False),
                 self.getImage("img/food/Food_close_pan.png", True),
                 "close_pan", "food", 25, 0.01),
            Food(self.getImage("img/food/Food_egg.png", False),
                 self.getImage("img/food/Food_egg.png", True),
                 "egg", "food", 15, 0.04),
            Food(self.getImage("img/food/Food_empty_pan.png", False),
                 self.getImage("img/food/Food_empty_pan.png", True),
                 "empty_pan", "food", 0),
            Food(self.getImage("img/food/Food_fish.png", False),
                 self.getImage("img/food/Food_fish.png", True),
                 "fish", "food",  20, 0.035),
            Food(self.getImage("img/food/Food_honey.png", False),
                 self.getImage("img/food/Food_honey.png", True),
                 "honey", "food", 25),
            Food(self.getImage("img/food/Food_kiwi.png", False),
                 self.getImage("img/food/Food_kiwi.png", True),
                 "kiwi", "food", 15, 0.03),
            Food(self.getImage("img/food/Food_lemon.png", False),
                 self.getImage("img/food/Food_lemon.png", True),
                 "kiwi", "food", 10, 0.02),
            Food(self.getImage("img/food/Food_mushroom.png", False),
                 self.getImage("img/food/Food_mushroom.png", True),
                 "mushroom", "food", 20, 0.04),
            Food(self.getImage("img/food/Food_orange.png", False),
                 self.getImage("img/food/Food_orange.png", True),
                 "orange", "food", 10, 0.04),
            Food(self.getImage("img/food/Food_pizza.png", False),
                 self.getImage("img/food/Food_pizza.png", True),
                 "pizza", "food", 20, 0.025),
            Food(self.getImage("img/food/Food_varenics.png", False),
                 self.getImage("img/food/Food_varenics.png", True),
                 "varenics", "food", 50, 0.04),
            Food(self.getImage("img/food/Food_watermelon.png", False),
                 self.getImage("img/food/Food_watermelon.png", True),
                 "watermelon", "food", 15, 0.035),
            Food(self.getImage("img/food/meat.png", False),
                 self.getImage("img/food/meat.png", True),
                 "meat", "food", 20, 0.04),
            Armor(self.getImage("img/armor/Boot1.png", False),
                 self.getImage("img/armor/Boot1.png", True),
                 "boots1", "boots", 3, 0.03),
            Armor(self.getImage("img/armor/Boot2.png", False),
                  self.getImage("img/armor/Boot2.png", True),
                  "boots2", "boots", 6, 0.03),
            Armor(self.getImage("img/armor/Boot3.png", False),
                  self.getImage("img/armor/Boot3.png", True),
                  "boots3", "boots", 9, 0.03),
            Armor(self.getImage("img/armor/Boot4.png", False),
                  self.getImage("img/armor/Boot4.png", True),
                  "boots4", "boots", 12, 0.03),
            Armor(self.getImage("img/armor/Boot5.png", False),
                  self.getImage("img/armor/Boot5.png", True),
                  "boots5", "boots", 15, 0.03),
            Armor(self.getImage("img/armor/Boot6.png", False),
                  self.getImage("img/armor/Boot6.png", True),
                  "boots6", "boots", 18, 0.03),
            Armor(self.getImage("img/armor/Boot7.png", False),
                  self.getImage("img/armor/Boot7.png", True),
                  "boots7", "boots", 21, 0.03),
            Armor(self.getImage("img/armor/Hand1.png", False),
                  self.getImage("img/armor/Hand1.png", True),
                  "hand1", "hands", 9, 0.03),
            Armor(self.getImage("img/armor/Hand1_1.png", False),
                  self.getImage("img/armor/Hand1_1.png", True),
                  "hand1_1", "hands", 3, 0.03),
            Armor(self.getImage("img/armor/Hand1_2.png", False),
                  self.getImage("img/armor/Hand1_2.png", True),
                  "hand1_2", "hands", 6, 0.03),
            Armor(self.getImage("img/armor/Hand1_3.png", False),
                  self.getImage("img/armor/Hand1_3.png", True),
                  "hand1_3", "hands", 12, 0.03),
            Armor(self.getImage("img/armor/Hand1_4.png", False),
                  self.getImage("img/armor/Hand1_4.png", True),
                  "hand1_4", "hands", 15, 0.03),
            Armor(self.getImage("img/armor/Hand2.png", False),
                  self.getImage("img/armor/Hand2.png", True),
                  "hand2", "hands", 15, 0.03),
            Armor(self.getImage("img/armor/Hand1_5.png", False),
                  self.getImage("img/armor/Hand1_5.png", True),
                  "hand1_5", "hands", 18, 0.03),
            Armor(self.getImage("img/armor/Hand3.png", False),
                  self.getImage("img/armor/Hand3.png", True),
                  "hand3", "hands", 18, 0.03),
            Armor(self.getImage("img/armor/Hand1_6.png", False),
                  self.getImage("img/armor/Hand1_6.png", True),
                  "hand1_6", "hands", 21, 0.03),
            Armor(self.getImage("img/armor/Hand4.png", False),
                  self.getImage("img/armor/Hand4.png", True),
                  "hand4", "hands", 21, 0.03),
            Armor(self.getImage("img/armor/Hand1_7.png", False),
                  self.getImage("img/armor/Hand1_7.png", True),
                  "hand1_7", "hands", 24, 0.03),
            Armor(self.getImage("img/armor/Hand5.png", False),
                  self.getImage("img/armor/Hand5.png", True),
                  "hand5", "hands", 24, 0.03),
            Armor(self.getImage("img/armor/Helmet.png", False),
                  self.getImage("img/armor/Helmet.png", True),
                  "helmet1", "helmet", 5, 0.03),
            Armor(self.getImage("img/armor/Helmet2.png", False),
                  self.getImage("img/armor/Helmet2.png", True),
                  "helmet2", "helmet", 10, 0.03),
            Armor(self.getImage("img/armor/Helmet3.png", False),
                  self.getImage("img/armor/Helmet3.png", True),
                  "helmet3", "helmet", 15, 0.03),
            Armor(self.getImage("img/armor/Helmet4.png", False),
                  self.getImage("img/armor/Helmet4.png", True),
                  "helmet4", "helmet", 20, 0.03),
            Armor(self.getImage("img/armor/Helmet5.png", False),
                  self.getImage("img/armor/Helmet5.png", True),
                  "helmet5", "helmet", 25, 0.03),
            Armor(self.getImage("img/armor/Helmet6.png", False),
                  self.getImage("img/armor/Helmet6.png", True),
                  "helmet6", "helmet", 30, 0.03),
            Armor(self.getImage("img/armor/Helmet7.png", False),
                  self.getImage("img/armor/Helmet7.png", True),
                  "helmet7", "helmet", 35, 0.03),
            Armor(self.getImage("img/armor/Mail1.png", False),
                  self.getImage("img/armor/Mail1.png", True),
                  "mail1", "mail", 7, 0.03),
            Armor(self.getImage("img/armor/Mail2.png", False),
                  self.getImage("img/armor/Mail2.png", True),
                  "mail2", "mail", 14, 0.03),
            Armor(self.getImage("img/armor/Mail3.png", False),
                  self.getImage("img/armor/Mail3.png", True),
                  "mail3", "mail", 21, 0.03),
            Armor(self.getImage("img/armor/Mail4.png", False),
                  self.getImage("img/armor/Mail4.png", True),
                  "mail4", "mail", 28, 0.03),
            Armor(self.getImage("img/armor/Mail5.png", False),
                  self.getImage("img/armor/Mail5.png", True),
                  "mail5", "mail", 35, 0.03),
            Armor(self.getImage("img/armor/Mail6.png", False),
                  self.getImage("img/armor/Mail6.png", True),
                  "mail6", "mail", 42, 0.03),
            Armor(self.getImage("img/armor/Mail7.png", False),
                  self.getImage("img/armor/Mail7.png", True),
                  "mail7", "mail", 49, 0.03),
            Armor(self.getImage("img/armor/shield1.png", False),
                  self.getImage("img/armor/shield1.png", True),
                  "shield1", "shield", 11, 0.03),
            Armor(self.getImage("img/armor/shield2.png", False),
                  self.getImage("img/armor/shield2.png", True),
                  "shield2", "shield", 22, 0.03),
            Armor(self.getImage("img/armor/shield3.png", False),
                  self.getImage("img/armor/shield3.png", True),
                  "shield3", "shield", 33, 0.03),
            Armor(self.getImage("img/armor/shield4.png", False),
                  self.getImage("img/armor/shield4.png", True),
                  "shield4", "shield", 44, 0.03),
            Armor(self.getImage("img/armor/shield5.png", False),
                  self.getImage("img/armor/shield5.png", True),
                  "shield5", "shield", 55, 0.03),
            Armor(self.getImage("img/armor/shield6.png", False),
                  self.getImage("img/armor/shield6.png", True),
                  "shield6", "shield", 66, 0.03),
            Armor(self.getImage("img/armor/shield7.png", False),
                  self.getImage("img/armor/shield7.png", True),
                  "shield7", "shield", 77, 0.03),
            Armor(self.getImage("img/armor/shield8.png", False),
                  self.getImage("img/armor/shield8.png", True),
                  "shield8", "shield", 88, 0.03),
            Armor(self.getImage("img/armor/shield9.png", False),
                  self.getImage("img/armor/shield9.png", True),
                  "shield9", "shield", 99, 0.03),
            Armor(self.getImage("img/armor/shield10.png", False),
                  self.getImage("img/armor/shield10.png", True),
                  "shield10", "shield", 110, 0.03),
            Armor(self.getImage("img/armor/shield11.png", False),
                  self.getImage("img/armor/shield11.png", True),
                  "shield11", "shield", 121, 0.03),
            Poitions(self.getImage("img/Potions/Potion_blue1.png", False),
                  self.getImage("img/Potions/Potion_blue1.png", True),
                  "potion_blue1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_blue4.png", False),
                     self.getImage("img/Potions/Potion_blue4.png", True),
                     "potion_blue4", "poition"),
            Poitions(self.getImage("img/Potions/Potion_darkgreen1.png", False),
                     self.getImage("img/Potions/Potion_darkgreen1.png", True),
                     "potion_darkgreen1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_darkgreen4.png", False),
                     self.getImage("img/Potions/Potion_darkgreen4.png", True),
                     "potion_darkgreen4", "poition"),
            Poitions(self.getImage("img/Potions/Potion_green1.png", False),
                     self.getImage("img/Potions/Potion_green1.png", True),
                     "potion_green1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_green4.png", False),
                     self.getImage("img/Potions/Potion_green4.png", True),
                     "potion_green4", "poition"),
            Poitions(self.getImage("img/Potions/Potion_orange1.png", False),
                     self.getImage("img/Potions/Potion_orange1.png", True),
                     "potion_orange1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_orange4.png", False),
                     self.getImage("img/Potions/Potion_orange4.png", True),
                     "potion_orange4", "poition"),
            Poitions(self.getImage("img/Potions/Potion_red_1.png", False),
                     self.getImage("img/Potions/Potion_red_1.png", True),
                     "potion_red1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_red4.png", False),
                     self.getImage("img/Potions/Potion_red4.png", True),
                     "potion_red4", "poition"),
            Poitions(self.getImage("img/Potions/Potion_yellow1.png", False),
                     self.getImage("img/Potions/Potion_yellow1.png", True),
                     "potion_yellow1", "poition"),
            Poitions(self.getImage("img/Potions/Potion_yellow4.png", False),
                     self.getImage("img/Potions/Potion_yellow4.png", True),
                     "potion_yellow4", "poition"),
            Poitions(self.getImage("img/Potions/Potion1.png", False),
                     self.getImage("img/Potions/Potion1.png", True),
                     "potion1", "poition"),
            Poitions(self.getImage("img/Potions/Potion2.png", False),
                     self.getImage("img/Potions/Potion2.png", True),
                     "potion2", "poition"),
            Poitions(self.getImage("img/Potions/Potion3.png", False),
                     self.getImage("img/Potions/Potion3.png", True),
                     "potion3", "poition"),
            Poitions(self.getImage("img/Potions/Potion4.png", False),
                     self.getImage("img/Potions/Potion4.png", True),
                     "potion4", "poition"),
            Poitions(self.getImage("img/Potions/Potion5.png", False),
                     self.getImage("img/Potions/Potion5.png", True),
                     "potion5", "poition"),
            Weapon(self.getImage("img/weapon/Weapon1.png", False),
                  self.getImage("img/weapon/Weapon1.png", True),
                  "weapon1", "weapon", 3, 0.03),
            Weapon(self.getImage("img/weapon/Ax.png", False),
                   self.getImage("img/weapon/Ax.png", True),
                   "ax", "weapon", 13, 0.03),
            Weapon(self.getImage("img/weapon/Ax2.png", False),
                   self.getImage("img/weapon/Ax2.png", True),
                   "ax2", "weapon", 15, 0.03),
            Weapon(self.getImage("img/weapon/Sword1.png", False),
                   self.getImage("img/weapon/Sword1.png", True),
                   "sword1", "weapon", 5, 0.03),
            Weapon(self.getImage("img/weapon/Sword2.png", False),
                   self.getImage("img/weapon/Sword2.png", True),
                   "sword2", "weapon", 20, 0.03),
            Weapon(self.getImage("img/weapon/Sword3.png", False),
                   self.getImage("img/weapon/Sword3.png", True),
                   "sword3", "weapon", 18, 0.03),
            Weapon(self.getImage("img/weapon/Sword4.png", False),
                   self.getImage("img/weapon/Sword4.png", True),
                   "sword4", "weapon", 8, 0.03),
            Weapon(self.getImage("img/weapon/Sword5.png", False),
                   self.getImage("img/weapon/Sword5.png", True),
                   "sword5", "weapon", 10, 0.03),
        ]

    def getImage(self, name, big):
        img = Image.open(name)
        if big:
            img = img.resize((200, 200), Image.ANTIALIAS)

        else:
            img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def get(self):
        x = randint(0, len(self.possibleItems)-1)
        if self.possibleItems[x].item == "food":
            return [self.possibleItems[x].skin, self.possibleItems[x].bigSkin,
                    self.possibleItems[x].name, self.possibleItems[x].item,
                    self.possibleItems[x].satiety, self.possibleItems[x].rotteRate,
                    self.possibleItems[x].canRott]
        elif self.possibleItems[x].item == "poition":
            return [self.possibleItems[x].skin, self.possibleItems[x].bigSkin,
                    self.possibleItems[x].name, self.possibleItems[x].item]
        elif self.possibleItems[x].item == "weapon":
            return[self.possibleItems[x].skin, self.possibleItems[x].bigSkin,
                  self.possibleItems[x].name, self.possibleItems[x].item,
                  self.possibleItems[x].attack_value, self.possibleItems[x].brokeRate]
        else:
            return[self.possibleItems[x].skin, self.possibleItems[x].bigSkin,
                  self.possibleItems[x].name, self.possibleItems[x].item,
                  self.possibleItems[x].block_value, self.possibleItems[x].brokeRate]

    def getAll(self):
        a = {}
        for i in self.possibleItems:
            if i.item == "food":
                a[i.name] = [i.skin, i.bigSkin, i.name, i.item, i.satiety, i.rotteRate, i.canRott]
            elif i.item == "poition":
                a[i.name] = [i.skin, i.bigSkin, i.name, i.item]
            elif i.item == "weapon":
                a[i.name] = [i.skin, i.bigSkin, i.name, i.item, i.attack_value, i.brokeRate]
            else:
                a[i.name] = [i.skin, i.bigSkin, i.name, i.item, i.block_value, i.brokeRate]
        return a

class Armor():
    def __init__(self, skin, bigSkin, name, item, block_value, brokeRate):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name
        self.brokeRate = brokeRate
        self.item = item
        self.block_value = block_value
        self.fracture_of_armor = 0
        self.isBroken = False

    def broke(self):
        self.block_value = 0
        self.fracture_of_armor = 100
        self.isBroken = True

    def fracture(self):
        if self.fracture_of_armor + self.block_value * self.brokeRate >= 100:
            self.broke()
            return
        else:
            self.fracture_of_armor += self.block_value * self.brokeRate

class Weapon:
    def __init__(self, skin, bigSkin, name, item,  attack_value, brokeRate):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name
        self.brokeRate = brokeRate
        self.item = item
        self.attack_value = attack_value
        self.fracture_of_weapon = 0
        self.isBroken = False

    def broke(self):
        self.attack_value = 0
        self.fracture_of_weapon = 100
        self.isBroken = True

    def fracture(self):
        if self.fracture_of_weapon + self.attack_value * self.brokeRate >= 100:
            self.broke()
            return
        else:
            self.fracture_of_weapon += self.attack_value * self.brokeRate

class Poitions():
    def __init__(self, skin, bigSkin, name, item):
        self.skin = skin
        self.bigSkin = bigSkin
        self.name = name
        self.item = item
        self.fracture_of_weapon = 0
        self.isBroken = False