from random import *
from math import*
from PIL import Image, ImageTk
class Monster():

    def __init__(self, name,tile,gui):
        self.gui=gui
        front_skin1 = Image.open("img/Orc2.png")
        front_skin1 = front_skin1.resize((100, 100), Image.ANTIALIAS)
        allMonsters = {"deathMonster": [ImageTk.PhotoImage(front_skin1), "dead_skin", "bot_skin", "health", 0.2, "arr_attack"]}
        self.tile = tile
        self.skin = allMonsters[name][0]
        self.name = name
        self.speed = allMonsters[name][4]
        self.health = allMonsters[name][3]
        self.died_skin = allMonsters[name][1]
        self.faced_north = True
        self.faced_east = False
        self.bot_skin = allMonsters[name][2]
        self.x = tile.realx+50+random()*13
        self.y = tile.realy+50+random()*13
        self.isDied = False
        self.target = None
        self.image = False
        self.lifespan=0
    def attack(self):
        attack_value = randint(0.7 * allMonsters[self.name][5], 1.3 * allMonsters[self.name][5])
        return attack_value

    def die(self):
        self.health = 0
        self.skin = self.died_skin
        self.isDied = True

    def move_toward(self,x,y):
        gui=self.gui
        velx=x - self.x
        vely=y - self.y
        const=1
        if self.speed<sqrt(velx**2+vely**2):
            const=self.speed/sqrt(velx**2+vely**2)

        velx*=const+random()*0.01
        vely*=const+random()*0.01
        tile=self.tile
        self.x+=velx
        self.y+=vely
        if (tile.realy + gui.size  < self.y):
                if (tile.connections[3]):

                    self.tile = self.tile.connections[3]
                    #print(self.tile.x,self.tile.y)
        if (tile.realy > self.y):
                if (tile.connections[0]):

                    self.tile = self.tile.connections[0]
                    #print(self.tile.x,self.tile.y)
        if (tile.realx + gui.size < self.x):
                if (tile.connections[2]):

                    self.tile = self.tile.connections[2]
                    #print(self.tile.x,self.tile.y)
        if (tile.realx > self.x):
                if (tile.connections[1]):

                    self.tile = self.tile.connections[1]
                    #print(self.tile.x,self.tile.y)


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
    def redraw(self,canvas):
        if(self.image):
            try:
                canvas.delete(self.image)
            except:
                pass
        try:
            self.image = canvas.create_image(self.x,self.y,image = self.skin)
        except:
            pass

class MonsterCollectiveBrain:
    def __init__(self,gui):
        self.monsters=[]
        self.pers=gui.pers
        self.maze=gui.maze
        self.monsterCount=0
        self.monsters.append(Monster("deathMonster",self.maze.getTile(3,3,0),gui))
        self.monsters[-1].target=self.monsters[-1].tile
        #print(self.monsters[-1].target.x,self.monsters[-1].target.y)
    def loop(self,gui):
        #print(self.monsterCount)
        if(not self.monsterCount>3):
            #print(self.monsterCount)
            #self.monsterCount+=1
            if len(gui.visible[1])-1>0:
                tile = gui.visible[1][randint(0, floor(len(gui.visible[1])/2-1))]
                con=tile.connections[randint(0,3)]
                if con and not con in gui.visible[0]:
                    self.monsterCount+=1
                    self.monsters.append(Monster("deathMonster",con,gui))
                    #print(con)
                    self.monsters[-1].target=tile
        for i in self.monsters:
            if i.lifespan>2:
                i.die()
            if i.isDied:
                self.monsters.remove(i)
                self.monsterCount-=1
            if i.tile in gui.visible[0]:
                #print('1')
                i.move_toward(self.pers.x, self.pers.y)
                i.redraw(gui.canvas)
            else:
                target=i.target
                i.move_toward(target.realx+50,target.realy+50)
                i.lifespan+=0.01
            #i.redraw(gui.canvas)
