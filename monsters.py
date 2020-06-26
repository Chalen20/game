from random import *
from math import*
from PIL import Image, ImageTk
from backpack import Backpack
from copy import copy, deepcopy
from time import sleep
class allMonsters():
    def __init__(self):
        front_skin1 = Image.open("img/Orc2.png")
        front_skin1 = front_skin1.resize((100, 100), Image.ANTIALIAS)
        front_skin2 = Image.open("img/Orc3.png")
        front_skin2 = front_skin2.resize((100, 100), Image.ANTIALIAS)

        front_skin1_animation = Image.open("img/Orc2_animation1.png")
        front_skin1_animation = front_skin1_animation.resize((100, 100), Image.ANTIALIAS)
        front_skin2_animation = Image.open("img/Orc3_animation1.png")
        front_skin2_animation = front_skin2_animation.resize((100, 100), Image.ANTIALIAS)

        front_skin1_animation2 = Image.open("img/Orc2_animaion2.png")
        front_skin1_animation2 = front_skin1_animation2.resize((100, 100), Image.ANTIALIAS)
        front_skin2_animation2 = Image.open("img/Orc3_animation2.png")
        front_skin2_animation2 = front_skin2_animation2.resize((100, 100), Image.ANTIALIAS)

        front_skin4 = Image.open("img/portal.png")
        front_skin4 = front_skin4.resize((100, 100), Image.ANTIALIAS)
        
        front_skin5 = Image.open("img/Orc1.png")
        front_skin5 = front_skin5.resize((100, 100), Image.ANTIALIAS)

        front_skin6 = Image.open("img/Orc5.png")
        front_skin6 = front_skin6.resize((100, 100), Image.ANTIALIAS)

        front_skin7 = Image.open("img/portal.png")
        front_skin7 = front_skin7.resize((20, 20), Image.ANTIALIAS)

        front_skin8 = Image.open("img/Orc4.png")
        front_skin8 = front_skin8.resize((120, 120), Image.ANTIALIAS)

        front_skin3 = Image.open("img/full_chest.png")
        front_skin3 = front_skin3.resize((100, 100), Image.ANTIALIAS)


        self.allMonsters = {"deathMonster": [ImageTk.PhotoImage(front_skin1), "dead_skin", 30, 30, 0.8, 10,
                                        ImageTk.PhotoImage(front_skin1_animation),
                                        ImageTk.PhotoImage(front_skin1_animation2), False],
                       'deadlyMonster':[ImageTk.PhotoImage(front_skin2), "dead_skin", 30, 5, 1.6, 5,
                                        ImageTk.PhotoImage(front_skin2_animation),
                                        ImageTk.PhotoImage(front_skin2_animation2), False],
                       'chest':[ImageTk.PhotoImage(front_skin3), "dead_skin", 0, 1, 0, 0,
                                ImageTk.PhotoImage(front_skin3), ImageTk.PhotoImage(front_skin3), False],
                       'portal':[ImageTk.PhotoImage(front_skin4), "dead_skin", 30, 100000, 0, 0,
                                 ImageTk.PhotoImage(front_skin4), ImageTk.PhotoImage(front_skin4), False],
                       'death':[ImageTk.PhotoImage(front_skin5), "dead_skin", 20, 1, 0.6, 50,
                                 ImageTk.PhotoImage(front_skin5), ImageTk.PhotoImage(front_skin5), False],
                       'mage':[ImageTk.PhotoImage(front_skin6), "dead_skin", 200, 1, 0.6, 0,
                                 ImageTk.PhotoImage(front_skin6), ImageTk.PhotoImage(front_skin6), False],
                       'fireball':[ImageTk.PhotoImage(front_skin7), "dead_skin", 30, 1, 2, 5,
                                 ImageTk.PhotoImage(front_skin7), ImageTk.PhotoImage(front_skin7), True],
                       'miniboss':[ImageTk.PhotoImage(front_skin8), "dead_skin", 200, 100, 0.6, 0,
                                 ImageTk.PhotoImage(front_skin8), ImageTk.PhotoImage(front_skin8), False]
        }
class Monster():

    def __init__(self, name,tile,gui,*args):
        self.gui=gui
        if(len(args)>0):
            self.lvl=args[0]
        else:
            self.lvl=0
        allMonsters=gui.allMonsters.allMonsters
        self.tile = tile
        self.skin = allMonsters[name][0]
        self.name = name
        self.speed = allMonsters[name][4]*(1+self.lvl*0.05)
        self.health = allMonsters[name][3]
        self.died_skin = allMonsters[name][1]
        self.faced_north = True
        self.faced_east = False
        self.attackRange = allMonsters[name][2]
        self.x = tile.realx+50+random()*13
        self.y = tile.realy+50+random()*13
        self.missile=allMonsters[name][8]
        self.skin_animation = allMonsters[name][6]
        self.skin_animation2 = allMonsters[name][7]
        self.power=allMonsters[name][5]
        self.isDied = False
        self.target = None
        self.image = False
        self.lifespan=0
        self.recharge=0
        self.counter = 0
        #self.attack=5
        self.q = name=='portal'
        self.tag=False
        
    def attack(self,pers,mcb):
        class Point:
            def __init__(self,x,y):
                self.x=x
                self.y=y
        if self.name == 'mage':
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x),copy(pers.y))
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y
            
        if self.name == 'miniboss':
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x),copy(pers.y))
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y
        
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x)+30,copy(pers.y))
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y
        
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x),copy(pers.y)+30)
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y
        
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x)-30,copy(pers.y))
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y
        
            mcb.monsters.append(Monster('fireball',self.tile,self.gui,self.lvl))
                    #print(con)
            mcb.monsters[-1].target=Point(copy(pers.x),copy(pers.y)-30)
            mcb.monsters[-1].x=self.x
            mcb.monsters[-1].y=self.y

            
        attack_value = self.power + randint(0,self.lvl)*(1+self.lvl*0.7)
        return attack_value

    def die(self):
        meat = Image.open("img/food/meat.png")
        meat = meat.resize((100, 100), Image.ANTIALIAS)
        meat_big = meat.resize((200, 200), Image.ANTIALIAS)
        meat_big = ImageTk.PhotoImage(meat_big)
        meat = ImageTk.PhotoImage(meat)
        
        self.health = 0
        self.skin = self.died_skin
        self.isDied = True
        if self.name=='chest':
            ic = self.gui.allItems
            item = ic.get()
            self.gui.items.append(item)
            if item[3] != "food" and item[3] != "poition":
                self.gui.ammunition.append(item)

    def move_toward(self,x,y,*args):
        if(sqrt((x-self.x)**2+(y-self.y)**2)<self.attackRange-3):
            if(self.missile):
                self.die()
            else:
                if(not len(args)>0):
                    return
        gui=self.gui
        velx=x - self.x
        vely=y - self.y
        const=1
        if self.speed<sqrt(velx**2+vely**2):
            const=self.speed/sqrt(velx**2+vely**2)

        velx*=const#+random()*0.01
        vely*=const#+random()*0.01
        tile=self.tile
        self.x+=velx
        self.y+=vely
        try:
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
        except:
            print(self.name,self.tile)
            


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
                print('error')
        try:
            if self.counter % 8 < 4:
                self.image = canvas.create_image(self.x,self.y,image = self.skin)
            elif self.counter % 16 <= 8:
                self.image = canvas.create_image(self.x, self.y, image=self.skin_animation)
            elif self.counter % 16 >= 8:
                self.image = canvas.create_image(self.x, self.y, image=self.skin_animation2)
        except:
            pass
        if(self.isDied):
            canvas.delete(self.image)

class MonsterCollectiveBrain:
    #possible = ['deathMonster','deadlyMonster','deathMonster']
    def __init__(self,gui):
        self.monsters=[]
        self.monsters.append(Monster('portal',gui.maze.getTile(4,3,0),gui))
        self.monsters[-1].target=gui.maze.getTile(4,3,0)
        self.monsters[-1].q=True
        #self.monsters.append(Monster('portal',gui.maze.getTile(4,3,1),gui))
        #self.monsters[-1].target=gui.maze.getTile(4,3,1)
        #self.monsters[-1].q=True
        #self.monsters=[]
        self.pers=gui.pers
        self.maze=gui.maze
        self.monsterCount=0
        #self.monsters.append(Monster("deathMonster",self.maze.getTile(3,3,0),gui))
        self.monsters[-1].target=self.monsters[-1].tile
        #print(self.monsters[-1].target.x,self.monsters[-1].target.y)
    def addPortal(self,tile,gui,lvl):
        self.monsters.append(Monster('portal',tile,gui,lvl))
        self.monsters[-1].target=tile
        self.monsters[-1].q=True
    def loop(self,gui):
        lvl=self.pers.tile.chunk.z
        possible = {0:['deathMonster','deadlyMonster','mage'],
                    1:['deathMonster','deadlyMonster','death','deathMonster','mage'],
                    2:['deathMonster','deadlyMonster','death','mage','deadlyMonster','miniboss'],
                    3:['deathMonster','deadlyMonster','death','mage','deadlyMonster','miniboss'],
                    4:['deathMonster','deadlyMonster','death','mage','deadlyMonster','miniboss'],
                    5:['deathMonster','deadlyMonster','death','mage','deadlyMonster','miniboss']
                    }
        
        if(lvl>5):
            possible=possible[5]
        else:
            possible=possible[lvl]
        #print(self.monsterCount)
        if(not self.monsterCount>3+lvl):
            #print(self.monsterCount)
            #self.monsterCount+=1
            if len(gui.visible[1])-1>0:
                #print(self.monsterCount)
                tile = gui.visible[1][randint(0, floor(len(gui.visible[1])-1))]
                con=tile.connections[randint(0,3)]
                if con and not con in gui.visible[0]:
                    #sleep(0.01)
                    self.monsterCount+=1
                    self.monsters.append(Monster(possible[randint(0,len(possible)-1)],con,gui,lvl))
                    #print(con)
                    self.monsters[-1].target=tile
                    pass
        if self.pers.tile.room  and self.pers.tile.room.isFree:
            #print(1
            self.pers.tile.room.monsters=[]
            for i in self.pers.tile.room.tiles:
                #print(1)
                self.pers.tile
                if(random()<0.4):
                    #print(2)
                    #self.monsterCount+=1
                    #self.pers.tile.room.monsters=[]
                    self.monsters.append(Monster(possible[randint(0,len(possible)-1)],i,gui,lvl))
                    self.monsters[-1].target=i
                    self.monsters[-1].q=True
                    self.monsters[-1].tag=self.pers.tile.room
                    #self.pers.tile.room.monsters.append(self.monsters[-1])
                    if(random()<0.5):
                        self.monsters.append(Monster('chest',i,gui,lvl))
                        self.monsters[-1].target=i
                        self.monsters[-1].q=True
                    #print(con)
                    #self.monsters[-1].target=i
                    

                   
            self.pers.tile.room.isFree=False
        for i in self.monsters:
            if i.lvl != lvl:
                continue
            if i.lifespan>2:
                i.die()
            if i.isDied:
                #print(i.missile)
                self.monsters.remove(i)
                gui.canvas.delete(i.image)
                if(not i.q and not i.missile):
                    self.monsterCount-=1
                if(i.missile):
                    if(sqrt((i.x-self.pers.x)**2+(i.y-self.pers.y)**2)<i.attackRange+5): 
                        attack= i.attack(self.pers,self)     
                        self.pers.take_damage(attack)
                        
                        now_health = self.pers.health
                        gui.health.change(now_health)
                #if(i.tag):
                #    i.tag.monsters.remove(i)
                #    if len(i.tag.monsters)==0:
                #        i.tag.chunk.cleared=True
                #        print(i.tag.chunk.x,i.tag.chunk.y,'cleared')
            elif i.tile in gui.visible[0]:
                #print('1')
                if(i.missile):
                    i.move_toward(i.target.x,i.target.y)
                else:
                    i.move_toward(self.pers.x, self.pers.y)
                i.redraw(gui.canvas)
                i.counter += 1
            else:
                if(i.missile):
                    i.move_toward(i.target.x,i.target.y)
                else:
                    target=i.target
                    i.move_toward(target.realx+50,target.realy+50,True)
                #target=i.target
                #i.move_toward(target.realx+50,target.realy+50)
                if(not i.q):
                    i.lifespan+=0.01
            if(sqrt((i.x-self.pers.x)**2+(i.y-self.pers.y)**2)<i.attackRange and i.recharge<=0):
                if(i.name =='portal'):
                    print(1)
                    value = i.lvl
                    self.monsterCount=0
                    #if(value<4):
                    gui.level(value+1)
                        #else:
                        #self.pers.speed=0
                        #gui.paused=True
                        
                attack= i.attack(self.pers,self)     
                self.pers.take_damage(attack)
                i.recharge=2
                now_health = self.pers.health
                gui.health.change(now_health)
            if(i.recharge!=0):
                i.recharge-=0.01
                
            #i.redraw(gui.canvas)

