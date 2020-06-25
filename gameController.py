from Labyrynth import Maze
from Renderer import Renderer
from tkinter import *
from pers import Pers
from health import Health
from PIL import Image, ImageTk
from monsters import *
from time import sleep
from backpack import Backpack
from math import *
from ammunition import Ammunition
from item import *
from random import *
options = {
    'intensity': 0.1,
    'lifespan': 8,
    'loopchance': 0.5,
    'cavechance': 1,
    'chunk_size': 18,
    'block_chance': 0,
    'double_entrance': 0.2
}


class GUI:


    def __init__(self, name, visib,on):
        self.size = 150
        self.x = 50000
        self.y = 50000
        self.root = Tk()
        self.root.grab_set()
        self.root.focus_force()
        self.canvas = Canvas(self.root, width=800, height=800)
        #self.canvas.focus_set()
        self.ren = Renderer(self)
        self.time = 0
        self.name = name
        self.visib = visib
        self.isPaused = False
        self.hung_is_stop = True

        self.visibility = []
        self.canvas.configure(scrollregion=(0, 0, 100000, 100000))
        self.canvas.pack()
        #self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        #self.canvas.bind("<B1-Motion>", self.scroll_move)

        options = {
            'intensity': 0.1,
            'lifespan': 8,
            'loopchance': 0.5,
            'cavechance': 1,
            'chunk_size': 18,
            'block_chance': 0.9,
            'double_entrance': 0.2
        }
        self.maze = Maze(options)
        self.maze.addChunk(0, 0, 0)
        self.maze.addChunk(0, -1, 0)
        self.maze.addChunk(1, -1, 0)
        self.maze.addChunk(-1, 0, 0)
        self.maze.addChunk(-1, 1, 0)
        self.maze.addChunk(1, 1, 0)
        self.maze.addChunk(1, 0, 0)
        self.maze.addChunk(0, 1, 0)
        self.maze.addChunk(-1, -1, 0)

        self.maze.addChunk(0, 0, 1)
        self.maze.addChunk(0, -1, 1)
        self.maze.addChunk(1, -1, 1)
        self.maze.addChunk(-1, 0, 1)
        self.maze.addChunk(-1, 1, 1)
        self.maze.addChunk(1, 1, 1)
        self.maze.addChunk(1, 0, 1)
        self.maze.addChunk(0, 1, 1)
        self.maze.addChunk(-1, -1, 1)

        self.canvas.create_rectangle(0, 0, 20, 20, outline="black", fill='black')
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t == 0:
                        self.ren.renderChunk(self.maze.chunks[i][j][t])
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(-50000, -50000, gain=1)
        persTile = self.maze.get(0, 0, 0).tiles[3][3]
        self.pers = Pers(self.name, persTile.realx+50, persTile.realy+50, persTile, self)
        self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.skin)
        pers = self.pers
        speed = pers.speed
        pers.chunk = self.maze.get(0, 0, 0)
        self.right_steps_counter = 0
        if not visib:
            self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
        self.health = Health(self.canvas, pers.health, persTile.realx + 250, persTile.realy - 420, persTile, "red",
                             200, 200,self.pers.health)
        self.satiety = Health(self.canvas, pers.satiety, persTile.realx + 270, persTile.realy - 380, persTile,
                              'yellow', 150, 100,pers.satiety)
        self.menu = Image.open("img/menu_button_game.png")
        self.menu = self.menu.resize((100, 40), Image.ANTIALIAS)
        self.menu = ImageTk.PhotoImage(self.menu)
        self.menu_button = self.canvas.create_image(persTile.realx - 400, persTile.realy - 420, image=self.menu)
        self.pause_icon = self.canvas.create_rectangle(persTile.realx - 400, persTile.realy - 400,
                                                       persTile.realx - 400, persTile.realy - 400)
        self.play_icon = self.canvas.create_rectangle(persTile.realx - 400, persTile.realy - 400,
                                                       persTile.realx - 400, persTile.realy - 400)
        self.back_icon = self.canvas.create_rectangle(persTile.realx - 400, persTile.realy - 400,
                                                       persTile.realx - 400, persTile.realy - 400)
        self.exit_icon = self.canvas.create_rectangle(persTile.realx - 400, persTile.realy - 400,
                                                       persTile.realx - 400, persTile.realy - 400)
        self.paused_icon = self.canvas.create_rectangle(persTile.realx - 400, persTile.realy - 400,
                                                     persTile.realx - 400, persTile.realy - 400)
        
       
        self.armor = Image.open("img/armor.png")
        self.armor = self.armor.resize((75, 75), Image.ANTIALIAS)
        self.armor = ImageTk.PhotoImage(self.armor)
        self.armor_icon = self.canvas.create_image(pers.x - 460, pers.y - 200, image=self.armor)

        meat = Image.open("img/food/meat.png")
        meat = meat.resize((100, 100), Image.ANTIALIAS)
        meat_big = meat.resize((200, 200), Image.ANTIALIAS)
        meat_big = ImageTk.PhotoImage(meat_big)
        meat = ImageTk.PhotoImage(meat)
        self.items = []
        self.items.append([meat, meat_big, "meat", "food", 20, 0.04, True])
        self.items.append([meat, meat_big, "meat", "food", 20, 0.04, True])
        self.items.append([meat, meat_big, "meat", "food", 20, 0.04, True])
        self.allItems = ItemController()
        allItems = self.allItems.getAll()
        item = self.allItems.get()

        self.ammunition = []
        self.equipment = {"weapon": [], "helmet": [], "mail": [], "hands": [], "boots": [], "shield": []}
        self.armor_window = Ammunition(self.root, self, allItems)
        self.backback = Backpack(self.root, self.pers, self.satiety, self, allItems)  
        self.backpack = Image.open("img/back_pack.png")
        self.backpack =  self.backpack.resize((75, 75), Image.ANTIALIAS)
        self.backpack = ImageTk.PhotoImage(self.backpack)
        self.backpack_icon = self.canvas.create_image(pers.x - 460, pers.y, image=self.backpack)
        self.recharge = 0

        #self.backback = Backpack(self.root, self.canvas, self.pers, self.satiety, pers.x-400, pers.y-400,self)
        def backpack_func(event):
            if self.armor_window.is_Open:
                close_armor(event)
            self.root.unbind('<Left>')
            self.root.unbind('<Right>')
            self.root.unbind('<Up>')
            self.root.unbind('<Down>')
            self.isPaused = True
            close_menu(event)
            self.canvas.tag_unbind(self.backpack_icon, "<Button-1>")

            self.backback = Backpack(self.root, self.pers, self.satiety, self, allItems)

            self.backback.start()
            self.canvas.tag_bind(self.backpack_icon, "<Button-1>", close_backpack)

        def close_backpack(event):
            play_func(event)
            
            self.backback.remove()
            self.canvas.tag_unbind(self.backpack_icon, "<Button-1>")
            self.canvas.tag_bind(self.backpack_icon, "<Button-1>", backpack_func)
            self.isPaused = False
        self.canvas.tag_bind(self.backpack_icon, "<Button-1>", backpack_func)
        self.mcb = MonsterCollectiveBrain(self)
        def armor_func(event):
            if self.backback.is_Open:
                close_backpack(event)
            self.root.unbind('<Left>')
            self.root.unbind('<Right>')
            self.root.unbind('<Up>')
            self.root.unbind('<Down>')
            self.isPaused = True
            close_menu(event)
            self.armor_window = Ammunition(self.root, self, allItems)
            self.armor_window.start()
            self.canvas.lift(self.armor_window)
            self.canvas.tag_unbind(self.armor_icon, "<Button-1>")
            self.canvas.tag_bind(self.armor_icon, "<Button-1>", close_armor)

        def close_armor(event):
            play_func(event)
            self.armor_window.remove()
            self.canvas.tag_unbind(self.armor_icon, "<Button-1>")
            self.canvas.tag_bind(self.armor_icon, "<Button-1>", armor_func)
            self.isPaused = False

        self.canvas.tag_bind(self.armor_icon, "<Button-1>", armor_func)
        #self.canvas.tag_bind(self.menu_button,"<Button-1>",
        def close_menu(event):
            self.canvas.delete(self.pause_icon)
            self.canvas.delete(self.play_icon)
            self.canvas.delete(self.back_icon)
            self.canvas.delete(self.exit_icon)
            self.canvas.tag_bind(self.menu_button, "<Button-1>",menu_label)
            
        #self.canvas.tag_bind(self.menu_button, "<Button-1>", menu_label)

        def pause_func(event):
            self.paused = Image.open("img/paused.png")
            self.paused = ImageTk.PhotoImage(self.paused)
            self.paused_icon = self.canvas.create_image(pers.x-70, pers.y-100, image=self.paused)
            self.canvas.lift(self.paused_icon)
            self.root.unbind('<Left>')
            self.root.unbind('<Right>')
            self.root.unbind('<Up>')
            self.root.unbind('<Down>')
            self.isPaused = True
            close_menu(event)
            self.canvas.tag_bind(self.paused_icon, "<Button-1>", play_func)

        def play_func(event):
            close_menu(event)
            self.isPaused = False
            self.canvas.delete(self.paused_icon)
            self.root.bind('<Left>', onKeyLeft)
            self.root.bind('<Right>', onKeyRight)
            self.root.bind('<Up>', onKeyUp)
            self.root.bind('<Down>', onKeyDown)
            self.isPaused = False
        def exit_func(event):
            self.root.destroy()
        def back_func(event):
            #print(self)
            self.root.destroy()
            on()
            #del self
        def menu_label(event):
            self.pause = Image.open("img/pause.png")
            self.pause = self.pause.resize((100, 40), Image.ANTIALIAS)
            self.pause = ImageTk.PhotoImage(self.pause)
            self.pause_icon = self.canvas.create_image(pers.x-340, pers.y-430, image=self.pause)

            self.play = Image.open("img/play2.png")
            self.play = self.play.resize((100, 40), Image.ANTIALIAS)
            self.play = ImageTk.PhotoImage(self.play)
            self.play_icon = self.canvas.create_image(pers.x - 340, pers.y - 470, image=self.play)

            self.back = Image.open("img/back.png")
            self.back = self.back.resize((100, 40), Image.ANTIALIAS)
            self.back = ImageTk.PhotoImage(self.back)
            self.back_icon = self.canvas.create_image(pers.x - 340, pers.y - 390, image=self.back)

            self.exit = Image.open("img/exit.png")
            self.exit = self.exit.resize((100, 40), Image.ANTIALIAS)
            self.exit = ImageTk.PhotoImage(self.exit)
            self.exit_icon = self.canvas.create_image(pers.x - 340, pers.y - 350, image=self.exit)

            self.canvas.lift(self.pause_icon)
            self.canvas.lift(self.play_icon)
            self.canvas.lift(self.back_icon)
            self.canvas.lift(self.exit_icon)
            self.canvas.tag_unbind(self.menu_button, "<Button-1>")
            self.canvas.tag_bind(self.menu_button, "<Button-1>", close_menu)

            self.canvas.tag_bind(self.pause_icon, "<Button-1>", pause_func)
            self.canvas.tag_bind(self.play_icon, "<Button-1>", play_func)
            self.canvas.tag_bind(self.exit_icon, "<Button-1>", exit_func)
            #self.canvas.tag_bind(self.exit_icon, "<Button-1>", exit_func)
            self.canvas.tag_bind(self.back_icon, "<Button-1>", back_func)
       
        self.canvas.tag_bind(self.menu_button, "<Button-1>", menu_label)
            
#----------------------------------------------------------------------------------
        def onKeyLeft(event):
            tile = pers.tile
            move = True
            if (tile.realx > pers.x - speed):

                if (tile.connections[1]):

                    pers.tile = tile.connections[1]
                    if not visib:
                        self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                        self.canvas.lift(self.health.rect)
                        self.canvas.lift(self.health.form)
                        self.canvas.lift(self.satiety.rect)
                        self.canvas.lift(self.satiety.form)
                        self.canvas.lift(self.menu_button)
                        self.canvas.lift(self.armor_icon)
                        self.canvas.lift(self.backpack_icon)
                else:
                    move = False
            if pers.isDied:
                move = False
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
            if move:
                self.canvas.scan_mark(0, 0)
                self.canvas.scan_dragto(int(speed / 10), 0)
                if self.right_steps_counter % 4 == 0:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.back_skin_animation_right_leg)
                elif self.right_steps_counter % 2 == 1:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.bot_skin)
                elif self.right_steps_counter % 4 == 2:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.back_skin_animation_left_leg)
                self.right_steps_counter += 1
                self.canvas.move(self.skin, -speed, 0)
                self.canvas.move(self.health.form, -speed, 0)
                self.canvas.move(self.health.rect, -speed, 0)
                self.canvas.move(self.satiety.form, -speed, 0)
                self.canvas.move(self.satiety.rect, -speed, 0)
                self.canvas.move(self.menu_button, -speed, 0)
                self.canvas.move(self.armor_icon, -speed, 0)
                self.canvas.move(self.backpack_icon, -speed, 0)
                pers.x -= speed
                self.health.x -= speed
                self.satiety.x -= speed
                self.pers.now_skin = self.pers.bot_skin
                self.canvas.delete(self.pause_icon)
                self.canvas.delete(self.play_icon)
                self.canvas.delete(self.back_icon)
                self.canvas.delete(self.exit_icon)
            if (pers.chunk != tile.chunk):
                pers.chunk = tile.chunk
                self.addNeighbours(tile.chunk)
                self.renderNeighbours(tile.chunk)

        def onKeyRight(event):
            move = True
            tile = pers.tile
            if (tile.realx + self.size - pers.size < pers.x + speed):

                if (tile.connections[2]):
                    pers.tile = tile.connections[2]
                    if not visib:
                        self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                        self.canvas.lift(self.health.rect)
                        self.canvas.lift(self.health.form)
                        self.canvas.lift(self.satiety.rect)
                        self.canvas.lift(self.satiety.form)
                        self.canvas.lift(self.menu_button)
                        self.canvas.lift(self.armor_icon)
                        self.canvas.lift(self.backpack_icon)
                else:
                    move = False
            if pers.isDied:
                move = False
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
            if move:
                self.canvas.scan_mark(0, 0)
                self.canvas.scan_dragto(int(-speed / 10), 0)
                if self.right_steps_counter % 4 == 0:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.front_skin_animation_right_leg)
                elif self.right_steps_counter % 2 == 1:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.skin)
                elif self.right_steps_counter % 4 == 2:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.front_skin_animation_left_leg)
                self.right_steps_counter += 1
                self.canvas.move(self.skin, speed, 0)
                self.canvas.move(self.health.form, speed, 0)
                self.canvas.move(self.health.rect, speed, 0)
                self.canvas.move(self.satiety.form, speed, 0)
                self.canvas.move(self.satiety.rect, speed, 0)
                self.canvas.move(self.menu_button, speed, 0)
                self.canvas.move(self.armor_icon, speed, 0)
                self.canvas.move(self.backpack_icon, speed, 0)
                pers.x += speed
                self.health.x += speed
                self.satiety.x += speed
                self.pers.now_skin = self.pers.skin
                self.canvas.delete(self.pause_icon)
                self.canvas.delete(self.play_icon)
                self.canvas.delete(self.back_icon)
                self.canvas.delete(self.exit_icon)
            if (pers.chunk != tile.chunk):
                pers.chunk = tile.chunk

                self.addNeighbours(tile.chunk)
                self.renderNeighbours(tile.chunk)

        def onKeyDown(event):
            move = True
            tile = pers.tile
            if (tile.realy + self.size - pers.size < pers.y + speed):

                if (tile.connections[3]):
                    pers.tile = tile.connections[3]
                    if not visib:
                        self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                        self.canvas.lift(self.health.rect)
                        self.canvas.lift(self.health.form)
                        self.canvas.lift(self.satiety.rect)
                        self.canvas.lift(self.satiety.form)
                        self.canvas.lift(self.menu_button)
                        self.canvas.lift(self.armor_icon)
                        self.canvas.lift(self.backpack_icon)
                else:
                    move = False
            if pers.isDied:
                move = False
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
            if move:
                self.canvas.scan_mark(0, 0)
                self.canvas.scan_dragto(0, int(-speed / 10))
                if self.right_steps_counter % 4 == 0:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.transpose_front_skin_animation_right_leg)
                elif self.right_steps_counter % 2 == 1:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.transpose_skin)
                elif self.right_steps_counter % 4 == 2:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.transpose_front_skin_animation_left_leg)
                self.right_steps_counter += 1
                self.canvas.move(self.skin, 0, speed)
                self.canvas.move(self.health.form, 0, speed)
                self.canvas.move(self.health.rect, 0, speed)
                self.canvas.move(self.satiety.form, 0, speed)
                self.canvas.move(self.satiety.rect, 0, speed)
                self.canvas.move(self.menu_button, 0, speed)
                self.canvas.move(self.armor_icon, 0, speed)
                self.canvas.move(self.backpack_icon, 0, speed)
                pers.y += speed
                self.health.y += speed
                self.satiety.y += speed
                self.pers.now_skin = self.pers.transpose_skin
                self.canvas.delete(self.pause_icon)
                self.canvas.delete(self.play_icon)
                self.canvas.delete(self.back_icon)
                self.canvas.delete(self.exit_icon)
            if (pers.chunk != tile.chunk):
                pers.chunk = tile.chunk

                self.addNeighbours(tile.chunk)
                self.renderNeighbours(tile.chunk)
        
        def onKeyUp(event):
            move = True
            tile = pers.tile
            if (tile.realy > pers.y - speed):

                if (tile.connections[0]):
                    pers.tile = tile.connections[0]
                    if not visib:
                        self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                        self.canvas.lift(self.health.rect)
                        self.canvas.lift(self.health.form)
                        self.canvas.lift(self.satiety.rect)
                        self.canvas.lift(self.satiety.form)
                        self.canvas.lift(self.menu_button)
                        self.canvas.lift(self.armor_icon)
                        self.canvas.lift(self.backpack_icon)
                else:
                    move = False
            if pers.isDied:
                move = False
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
            if move:
                self.canvas.scan_mark(0, 0)
                self.canvas.scan_dragto(0, int(speed / 10))
                if self.right_steps_counter % 4 == 0:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.transpose_back_skin_animation_right_leg)
                elif self.right_steps_counter % 2 == 1:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.bot_transpose_skin)
                elif self.right_steps_counter % 4 == 2:
                    self.canvas.delete(self.skin)
                    self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                         image=self.pers.transpose_back_skin_animation_left_leg)
                self.right_steps_counter += 1
                self.canvas.move(self.skin, 0, -speed)
                self.canvas.move(self.health.form, 0, -speed)
                self.canvas.move(self.health.rect, 0, -speed)
                self.canvas.move(self.satiety.form, 0, -speed)
                self.canvas.move(self.satiety.rect, 0, -speed)
                self.canvas.move(self.menu_button, 0, -speed)
                self.canvas.move(self.armor_icon, 0, -speed)
                self.canvas.move(self.backpack_icon, 0, -speed)
                pers.y -= speed
                self.health.y -= speed
                self.satiety.y -= speed
                self.pers.now_skin = self.pers.bot_transpose_skin
                self.canvas.delete(self.pause_icon)
                self.canvas.delete(self.play_icon)
                self.canvas.delete(self.back_icon)
                self.canvas.delete(self.exit_icon)
            if (pers.chunk != tile.chunk):
                pers.chunk = tile.chunk

                self.addNeighbours(tile.chunk)
                self.renderNeighbours(tile.chunk)
#----------------------------------------------------------------------
        def attack(event):
            
            if self.recharge>0:
                return
            self.recharge=0.2
            attacky=event.y-500
            attackx=event.x-500
            vectlen=sqrt(attackx**2+attacky**2)
            #print(attackx,attacky)
            if vectlen > 70:
                const=70/vectlen
            else:
                const=1
            attackx*=const
            attacky*=const
            attackx=self.pers.x+attackx
            attacky=self.pers.y+attacky
            
            #print(attackx,attacky)
            circle=self.canvas.create_oval(attackx-self.pers.attackRange,attacky-self.pers.attackRange,attackx+self.pers.attackRange,attacky+self.pers.attackRange,fill='grey')
            sleep(0.05)
            def dele():
                self.canvas.delete(circle)
            self.canvas.after(100,dele)
            
            for i in self.mcb.monsters:
                if sqrt((i.x-attackx)**2+(i.y-attacky)**2)<30:
                    i.take_damage(pers.power)
                    break
            
            
            
        self.root.bind('<Left>', onKeyLeft)
        self.root.bind('<Right>', onKeyRight)
        self.root.bind('<Up>', onKeyUp)
        self.root.bind('<Down>', onKeyDown)
        self.canvas.bind('<Button-1>', attack)
        #self.mcb = MonsterCollectiveBrain(self)

        counter = 0

        while True:
            if(self.pers.isDied):
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
                self.isPaused = True
                
            try:
                #self.root.lift(self.backpack_icon)
                #self.root.lift(self.menu_button)
                #self.root.lift(self.backpack)
                if not self.root.winfo_exists():
                    break
            except:
                break
            #self.canvas.lift(self.backpack_icon)
            if not self.isPaused:
                self.mcb.loop(self)
            else:
                pass
            if counter == 1300:
                if not self.pers.isDied and not self.isPaused:
                    self.pers.starvation()
                    self.hung_is_stop = False
                    if pers.isDied:
                        self.canvas.delete(self.skin)
                        self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                             image=self.pers.skin)
                    try:
                        self.satiety.change(self.pers.satiety)
                    except:
                        return
                else:
                    self.hung_is_stop = True
                    return
                counter = 0
            sleep(0.01)
            self.root.update()
            counter += 1
            if self.recharge!=0:
                self.recharge-=0.01
            try:
                self.canvas.lift(self.backpack_icon)
                self.canvas.lift(self.menu)
                self.canvas.lift(self.backpack)
            except:
                break
    def level(self,lvl):
            x = self.pers.tile.chunk.x
            y = self.pers.tile.chunk.y
            z = self.pers.tile.chunk.z
            
            maze = self.maze
            maze.addChunk(x, y, lvl)
            self.pers.tile=self.maze.getTile(self.pers.tile.x,self.pers.tile.y,lvl)
            for i in self.canvas.find_all():
                if(i!=self.backpack_icon and i!=self.menu_button and i!= self.armor_icon):
                    self.canvas.delete(i)
            self.satiety.change(self.satiety.point)
            self.addNeighbours(maze.get(x , y, lvl))
            self.renderNeighbours(maze.get(x , y, lvl))
            self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
            #self.mcb.addPortal(self.pers.tile.neighbours[0],self,lvl)
            #monsters.append(Monster('portal',self.pers.tile.neighbours[0],self))
         
            #self.mcb.monsters[-1].target=self.pers.tile
            #self.canvas.lift(self.backpack_icon)
            
            self.canvas.lift(self.backpack_icon)
            self.canvas.lift(self.menu_button)
            self.canvas.lift(self.armor_icon)
            
            #self.canvas.lift(self.backpack)
    def addNeighbours(self, chunk):
        x = chunk.x
        y = chunk.y
        z = chunk.z
        maze = self.maze
        maze.addChunk(x + 1, y, z)
        maze.addChunk(x, y + 1, z)
        maze.addChunk(x - 1, y, z)
        maze.addChunk(x - 1, y, z)
        maze.addChunk(x, y - 1, z)
        maze.addChunk(x + 1, y - 1, z)
        maze.addChunk(x - 1, y + 1, z)
        maze.addChunk(x - 1, y - 1, z)
        maze.addChunk(x + 1, y + 1, z)

    def renderNeighbours(self, chunk):
        x = chunk.x
        y = chunk.y
        z = chunk.z
        print(chunk.x,chunk.y,chunk.cleared)
        self.ren.renderChunk(self.maze.get(x + 1, y, z))
        self.ren.renderChunk(self.maze.get(x, y + 1, z))
        self.ren.renderChunk(self.maze.get(x + 1, y + 1, z))
        self.ren.renderChunk(self.maze.get(x - 1, y, z))
        self.ren.renderChunk(self.maze.get(x, y - 1, z))
        self.ren.renderChunk(self.maze.get(x + 1, y - 1, z))
        self.ren.renderChunk(self.maze.get(x - 1, y + 1, z))
        self.ren.renderChunk(self.maze.get(x - 1, y, z))
        self.ren.renderChunk(self.maze.get(x - 1, y - 1, z))
        self.ren.renderChunk(chunk)
        if(chunk.portaled=='mayBe'):
            if(random()<0.5):
                random1=randint(2,chunk.size-2)
                random2=randint(2,chunk.size-2)
                tile = chunk.tiles[random1][random2]
                print('portal',random1,random2)
                self.mcb.monsters.append(Monster('portal',tile,self,chunk.z))
                self.mcb.monsters[-1].target=tile
            chunk.portaled='Already'

    def scroll_start(self, event):
        # print("from",event.x,event.y)
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        # if(event.x>
        # print("to",event.x,event.y)
        self.canvas.scan_dragto(event.x, event.y, gain=1)

#---------------------------------------------------------------------------
class GameController:
    def __init__(self):
        self.gui = GUI()
        self.time = 0
        # self.maze=Maze(options)
        # self.hero=Pers('pers1')
        # self.monsters={
        #    'normal':[],
        #    'minotaurs':[]
        #
        # }
        # self.renderer=Renderer()
        # self.villages=[]

    def loop(self):
        self.time += 0.05


#gui = GUI("pers1")

# -------------gameCycle----------------
stop = False

# gc = GameController()
