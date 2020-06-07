from random import *
from time import *

allPers = {"name1": ["skin", "dead_skin", "bot_skin"]}

class Pers():
    def __init__(self, name):
        self.skin = allPers[name][0]
        self.items = []
        self.speed = 20
        self.health = 100
        self.satiety = 100
        self.speed_of_hunger_change = 5
        self.armor = 0
        self.equipment = {}
        self.equipment.weapon = None
        self.equipment.armor = None
        self.died_skin = allPers[name][1]
        self.coords = {}
        self.coords.x = 0
        self.coords.y = 0
        self.faced_north = True
        self.faced_east = False
        self.bot_skin = allPers[name][2]
        self.speed_of_hunger_change_timer = 13
        self.isDied = False
        while True:
            sleep(self.speed_of_hunger_change_timer)
            self.starvation()

    def attack(self):
        if not self.equipment["weapon"]:
            attack_value = randint(1, 5)
        else:
            attack_value = randint(1, 5 + self.equipment["weapon"]["value"])
        return attack_value

    def eat(self, item):
        if "food" in item["uses"]:
            self.hunger -= item["eating_value"]

    def equip(self, item):
        if "weapon" in item["uses"]:
            self.equipment["weapon"] = item
        elif "armor" in item["uses"]:
            self.equipment['armor'] = item
            self.armor += item["value"]

    def die(self):
        self.health = 0
        self.hunger = 100
        self.skin = self.died_skin
        self.isDied = True

    def move_left(self):
        if self.faced_east:
            pass
        self.coords["x"] -= 1

    def move_right(self):
        if not self.faced_east:
            pass
        self.coords['x'] += 1

    def move_top(self):
        if not self.faced_north:
            self.faced_north = True
            revert = self.bot_skin
            self.bot_skin = self.skin
            self.skin = revert
        self.coords['y'] += 1

    def move_bot(self):
        if self.faced_north:
            self.faced_north = False
            revert = self.bot_skin
            self.bot_skin = self.skin
            self.skin = revert
        self.coords['y'] -= 1

    def take_damage(self, damage):
        if self.health + self.armor < damage:
            self.die()
            return
        elif self.armor != 0 and self.armor < damage:
            self.armor = 0
            self.health -= damage - self.armor
        elif self.armor != 0 and self.armor > damage:
            self.armor -= damage
        else:
            self.health -= damage

    def starvation(self):
        if self.hunger < self.speed_of_hunger_change:
            self.die()
            return
        self.hunger += self.speed_of_hunger_change
        if self.hunger > 70:
            self.speed_of_hunger_change_timer = 13
        elif self.hunger > 40:
            self.speed_of_hunger_change_timer = 26
        elif self.hunger > 10:
            self.speed_of_hunger_change_timer = 39
        else:
            self.speed_of_hunger_change_timer = 52