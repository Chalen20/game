from random import *

allMonsters = {"name1": ["skin", "dead_skin", "bot_skin", "health", "speed", "arr_attack"]}

class Monster():
    def __init__(self, name,tile):
        self.lifespan = 10
        self.skin = allMonsters[name][0]
        self.name = name
        self.speed = allMonsters[name][4]
        self.health = allMonsters[name][3]
        self.died_skin = allMonsters[name][1]
        self.faced_north = True
        self.faced_east = False
        self.bot_skin = allMonsters[name][2]
        self.coords = {}
        self.coords.x = tile.real.x+10
        self.coords.y = tile.real.y+10
        self.isDied = False
        self.tile = False
        
    def attack(self):
        attack_value = randint(0.7 * allMonsters[self.name][5], 1.3 * allMonsters[self.name][5])
        return attack_value

    def die(self):
        self.health = 0
        self.skin = self.died_skin
        self.isDied = True
    def view(self):
        
    def idle(self):
        
    def move(self,targetx,targety):
        
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
        if self.health < damage:
            self.die()
            return
        else:
            self.health -= damage
class primitiveMonster(Monster):
    def __init__(self,name,tile):
        Monster.__init__(self,tile):
        self.skin=
            
class MonsterCollectiveBrain():
    def __init__(self,canvas,hero):
        self.canvas=canvas
        self.hero=hero
        self.monsters=monster[]
    def countFieldOfView   
        
    
