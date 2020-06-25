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
class MiniMap:
    def __init__(self,gui):
        self.gui = gui
    def toggle(self):
        self.frame = Frame(self.gui.root, width=150, height=150, bg="green")
        self.frame.place(x=650, y=650)
        self.canvas = Canvas(self.frame, width=150, height=150, bg="#ccccaa")
        self.canvas.configure(scrollregion=(0, 0, 100000, 100000))
        self.canvas.place(x=0, y=0)
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(-5000, -5000, gain=1)
        self.pers = self.canvas.create_rectangle(5048,5048,5057,5057, fill ='red')
    def turnoff(self):
        self.frame.destroy()
    def drag(self,x,y):
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(x, y, gain=15)
        self.canvas.move(self.pers,-x*15,-y*15)
    def lifter(self):
        self.frame.lift()
    def lowerer(self):
        self.frame.lower()
    
class GUI:


    def __init__(self, name, visib, on):
        self.size = 150
        self.x = 50000
        self.y = 50000
        self.root = Tk()
        self.root.grab_set()
        self.root.focus_force()
        self.canvas = Canvas(self.root, width=800, height=800)
        #self.canvas.focus_set()
        self.minimap = MiniMap(self)
        self.minimap.toggle()
        self.minimap.lowerer()
        self.ren = Renderer(self)
        self.time = 0
        self.name = name
        self.on = on
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

        self.allMonsters = allMonsters()

        self.canvas.create_rectangle(0, 0, 20, 20, outline="black", fill='black')
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t == 0:
                        self.ren.renderChunk(self.maze.chunks[i][j][t])
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(100000, 100000, gain=1)
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(-50000, -50000, gain=1)
        persTile = self.maze.get(0, 0, 0).tiles[3][3]
        self.pers = Pers(self.name, persTile.realx+50, persTile.realy+50, persTile, self)
        self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.skin)
        pers = self.pers
        speed = pers.speed
        self.speed = speed
        pers.chunk = self.maze.get(0, 0, 0)
        self.right_steps_counter = 0
        if not visib:
            self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
        self.health = Health(self.canvas, pers.health, persTile.realx + 250, persTile.realy - 420, persTile, "red",
                             200, 200, self.pers.health)
        self.satiety = Health(self.canvas, pers.satiety, persTile.realx + 270, persTile.realy - 380, persTile,
                              'yellow', 150, 100, pers.satiety)
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
        self.allItems_ = self.allItems.getAll()
        item = self.allItems.get()

        self.ammunition = []
        self.items.append(self.allItems_["potion2"])
        self.items.append(self.allItems_["mail7"])
        self.equipment = {"weapon": [], "helmet": [], "mail": [], "hands": [], "boots": [], "shield": []}
        self.armor_window = Ammunition(self.root, self, self.allItems_)
        self.backback = Backpack(self.root, self.pers, self.satiety, self, self.allItems_)
        self.backpack = Image.open("img/back_pack.png")
        self.backpack = self.backpack.resize((75, 75), Image.ANTIALIAS)
        self.backpack = ImageTk.PhotoImage(self.backpack)
        self.backpack_icon = self.canvas.create_image(pers.x - 460, pers.y, image=self.backpack)
        self.recharge = 0
        self.canvas.tag_bind(self.backpack_icon, "<Button-1>", self.backpack_func)
        self.canvas.tag_bind(self.armor_icon, "<Button-1>", self.armor_func)
        self.canvas.tag_bind(self.menu_button, "<Button-1>", self.menu_label)
        self.mcb = MonsterCollectiveBrain(self)
        self.root.bind('<Left>', self.onKeyLeft)
        self.root.bind('<Right>', self.onKeyRight)
        self.root.bind('<Up>', self.onKeyUp)
        self.root.bind('<Down>', self.onKeyDown)
        self.canvas.bind('<Button-1>', self.attack)
        # self.mcb = MonsterCollectiveBrain(self)

        counter = 0

        while True:
            if (self.pers.isDied):
                self.canvas.delete(self.skin)
                self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
                self.isPaused = True

            try:
                # self.root.lift(self.backpack_icon)
                # self.root.lift(self.menu_button)
                # self.root.lift(self.backpack)
                if not self.root.winfo_exists():
                    break
            except:
                break
            # self.canvas.lift(self.backpack_icon)
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
                        print("satiety error")
                else:
                    self.hung_is_stop = True
                counter = 0
            sleep(0.01)
            self.root.update()
            counter += 1
            if self.recharge != 0:
                self.recharge -= 0.01
            try:
                self.canvas.lift(self.backpack_icon)
                self.canvas.lift(self.menu)
                self.canvas.lift(self.backpack)
            except:
                break

        #self.backback = Backpack(self.root, self.canvas, self.pers, self.satiety, pers.x-400, pers.y-400,self)
    def backpack_func(self, event):
        if self.armor_window.is_Open:
            self.close_armor(event)
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')
        self.isPaused = True
        self.close_menu(event)
        self.canvas.tag_unbind(self.backpack_icon, "<Button-1>")

        self.backback = Backpack(self.root, self.pers, self.satiety, self, self.allItems_)

        self.backback.start()
        self.canvas.tag_bind(self.backpack_icon, "<Button-1>", self.close_backpack)

    def close_backpack(self, event):
        self.play_func(event)
            
        self.backback.remove()
        self.canvas.tag_unbind(self.backpack_icon, "<Button-1>")
        self.canvas.tag_bind(self.backpack_icon, "<Button-1>", self.backpack_func)
        self.isPaused = False

    def armor_func(self, event):
        if self.backback.is_Open:
            self.close_backpack(event)
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')
        self.isPaused = True
        self.close_menu(event)
        self.armor_window = Ammunition(self.root, self, self.allItems_)
        self.armor_window.start()
        self.canvas.lift(self.armor_window)
        self.canvas.tag_unbind(self.armor_icon, "<Button-1>")
        self.canvas.tag_bind(self.armor_icon, "<Button-1>", self.close_armor)

    def close_armor(self, event):
        self.play_func(event)
        self.armor_window.remove()
        self.canvas.tag_unbind(self.armor_icon, "<Button-1>")
        self.canvas.tag_bind(self.armor_icon, "<Button-1>", self.armor_func)
        self.isPaused = False

        #self.canvas.tag_bind(self.menu_button,"<Button-1>",

    def pause_func(self, event):
        self.paused = Image.open("img/paused.png")
        self.paused = ImageTk.PhotoImage(self.paused)
        self.paused_icon = self.canvas.create_image(self.pers.x-70, self.pers.y-100, image=self.paused)
        self.canvas.lift(self.paused_icon)
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')
        self.isPaused = True
        self.close_menu(event)
        self.canvas.tag_bind(self.paused_icon, "<Button-1>", self.play_func)

    def play_func(self, event):
        self.close_menu(event)
        self.isPaused = False
        self.canvas.delete(self.paused_icon)
        self.root.bind('<Left>', self.onKeyLeft)
        self.root.bind('<Right>', self.onKeyRight)
        self.root.bind('<Up>', self.onKeyUp)
        self.root.bind('<Down>', self.onKeyDown)
        self.isPaused = False

    def exit_func(self, event):
        self.root.destroy()

    def back_func(self, event):
        #print(self)
        self.root.destroy()
        self.on()
        #del self

    def menu_label(self, event):
        self.pause = Image.open("img/pause.png")
        self.pause = self.pause.resize((100, 40), Image.ANTIALIAS)
        self.pause = ImageTk.PhotoImage(self.pause)
        self.pause_icon = self.canvas.create_image(self.pers.x-340, self.pers.y-430, image=self.pause)

        self.play = Image.open("img/play2.png")
        self.play = self.play.resize((100, 40), Image.ANTIALIAS)
        self.play = ImageTk.PhotoImage(self.play)
        self.play_icon = self.canvas.create_image(self.pers.x - 340, self.pers.y - 470, image=self.play)

        self.back = Image.open("img/back.png")
        self.back = self.back.resize((100, 40), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(self.back)
        self.back_icon = self.canvas.create_image(self.pers.x - 340, self.pers.y - 390, image=self.back)

        self.exit = Image.open("img/exit.png")
        self.exit = self.exit.resize((100, 40), Image.ANTIALIAS)
        self.exit = ImageTk.PhotoImage(self.exit)
        self.exit_icon = self.canvas.create_image(self.pers.x - 340, self.pers.y - 350, image=self.exit)

        self.canvas.lift(self.pause_icon)
        self.canvas.lift(self.play_icon)
        self.canvas.lift(self.back_icon)
        self.canvas.lift(self.exit_icon)
        self.canvas.tag_unbind(self.menu_button, "<Button-1>")
        self.canvas.tag_bind(self.menu_button, "<Button-1>", self.close_menu)

        self.canvas.tag_bind(self.pause_icon, "<Button-1>", self.pause_func)
        self.canvas.tag_bind(self.play_icon, "<Button-1>", self.play_func)
        self.canvas.tag_bind(self.exit_icon, "<Button-1>", self.exit_func)
        #self.canvas.tag_bind(self.exit_icon, "<Button-1>", exit_func)
        self.canvas.tag_bind(self.back_icon, "<Button-1>", self.back_func)

    def close_menu(self, event):
        self.canvas.delete(self.pause_icon)
        self.canvas.delete(self.play_icon)
        self.canvas.delete(self.back_icon)
        self.canvas.delete(self.exit_icon)
        self.canvas.tag_bind(self.menu_button, "<Button-1>", self.menu_label)

        # self.canvas.tag_bind(self.menu_button, "<Button-1>", menu_label)
        
#----------------------------------------------------------------------------------
    def onKeyLeft(self, event):
        tile = self.pers.tile
        move = True
        if (tile.realx > self.pers.x - self.speed):

            if (tile.connections[1]):

                self.pers.tile = tile.connections[1]
                if not self.visib:
                    self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                    self.canvas.lift(self.health.rect)
                    self.canvas.lift(self.health.form)
                    self.canvas.lift(self.satiety.rect)
                    self.canvas.lift(self.satiety.form)
                    self.canvas.lift(self.menu_button)
                    self.canvas.lift(self.armor_icon)
                    self.canvas.lift(self.backpack_icon)
                    self.minimap.drag(1, 0)
            else:
                move = False
        if self.pers.isDied:
            move = False
            self.canvas.delete(self.skin)
            self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
        if move:
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(self.speed, 0, gain=1)
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
            self.canvas.move(self.skin, -self.speed, 0)
            self.canvas.move(self.health.form, -self.speed, 0)
            self.canvas.move(self.health.rect, -self.speed, 0)
            self.canvas.move(self.satiety.form, -self.speed, 0)
            self.canvas.move(self.satiety.rect, -self.speed, 0)
            self.canvas.move(self.menu_button, -self.speed, 0)
            self.canvas.move(self.armor_icon, -self.speed, 0)
            self.canvas.move(self.backpack_icon, -self.speed, 0)
            self.pers.x -= self.speed
            self.health.x -= self.speed
            self.satiety.x -= self.speed
            self.pers.now_skin = self.pers.bot_skin
            self.canvas.delete(self.pause_icon)
            self.canvas.delete(self.play_icon)
            self.canvas.delete(self.back_icon)
            self.canvas.delete(self.exit_icon)
        if (self.pers.chunk != tile.chunk):
            self.pers.chunk = tile.chunk
            self.addNeighbours(tile.chunk)
            self.renderNeighbours(tile.chunk)

    def onKeyRight(self, event):
        move = True
        tile = self.pers.tile
        if (tile.realx + self.size - self.pers.size < self.pers.x + self.speed):

            if (tile.connections[2]):
                self.pers.tile = tile.connections[2]
                if not self.visib:
                    self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                    self.canvas.lift(self.health.rect)
                    self.canvas.lift(self.health.form)
                    self.canvas.lift(self.satiety.rect)
                    self.canvas.lift(self.satiety.form)
                    self.canvas.lift(self.menu_button)
                    self.canvas.lift(self.armor_icon)
                    self.canvas.lift(self.backpack_icon)
                    self.minimap.drag(-1, 0)
            else:
                move = False
        if self.pers.isDied:
            move = False
            self.canvas.delete(self.skin)
            self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
        if move:
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(-self.speed, 0, gain=1)
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
            self.canvas.move(self.skin, self.speed, 0)
            self.canvas.move(self.health.form, self.speed, 0)
            self.canvas.move(self.health.rect, self.speed, 0)
            self.canvas.move(self.satiety.form, self.speed, 0)
            self.canvas.move(self.satiety.rect, self.speed, 0)
            self.canvas.move(self.menu_button, self.speed, 0)
            self.canvas.move(self.armor_icon, self.speed, 0)
            self.canvas.move(self.backpack_icon, self.speed, 0)
            self.pers.x += self.speed
            self.health.x += self.speed
            self.satiety.x += self.speed
            self.pers.now_skin = self.pers.skin
            self.canvas.delete(self.pause_icon)
            self.canvas.delete(self.play_icon)
            self.canvas.delete(self.back_icon)
            self.canvas.delete(self.exit_icon)
        if (self.pers.chunk != tile.chunk):
            self.pers.chunk = tile.chunk

            self.addNeighbours(tile.chunk)
            self.renderNeighbours(tile.chunk)

    def onKeyDown(self, event):
        move = True
        tile = self.pers.tile
        if (tile.realy + self.size - self.pers.size < self.pers.y + self.speed):

            if (tile.connections[3]):
                self.pers.tile = tile.connections[3]
                if not self.visib:
                    self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                    self.canvas.lift(self.health.rect)
                    self.canvas.lift(self.health.form)
                    self.canvas.lift(self.satiety.rect)
                    self.canvas.lift(self.satiety.form)
                    self.canvas.lift(self.menu_button)
                    self.canvas.lift(self.armor_icon)
                    self.canvas.lift(self.backpack_icon)
                    self.minimap.drag(0, -1)
            else:
                move = False
        if self.pers.isDied:
            move = False
            self.canvas.delete(self.skin)
            self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.skin)
        if move:
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(0, -self.speed,gain=1)
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
            self.canvas.move(self.skin, 0, self.speed)
            self.canvas.move(self.health.form, 0, self.speed)
            self.canvas.move(self.health.rect, 0, self.speed)
            self.canvas.move(self.satiety.form, 0, self.speed)
            self.canvas.move(self.satiety.rect, 0, self.speed)
            self.canvas.move(self.menu_button, 0, self.speed)
            self.canvas.move(self.armor_icon, 0, self.speed)
            self.canvas.move(self.backpack_icon, 0, self.speed)
            self.pers.y += self.speed
            self.health.y += self.speed
            self.satiety.y += self.speed
            self.pers.now_skin = self.pers.transpose_skin
            self.canvas.delete(self.pause_icon)
            self.canvas.delete(self.play_icon)
            self.canvas.delete(self.back_icon)
            self.canvas.delete(self.exit_icon)
        if (self.pers.chunk != tile.chunk):
            self.pers.chunk = tile.chunk

            self.addNeighbours(tile.chunk)
            self.renderNeighbours(tile.chunk)
        
    def onKeyUp(self, event):
        move = True
        tile = self.pers.tile
        if (tile.realy > self.pers.y - self.speed):

            if (tile.connections[0]):
                self.pers.tile = tile.connections[0]
                if not self.visib:
                    self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                    self.canvas.lift(self.health.rect)
                    self.canvas.lift(self.health.form)
                    self.canvas.lift(self.satiety.rect)
                    self.canvas.lift(self.satiety.form)
                    self.canvas.lift(self.menu_button)
                    self.canvas.lift(self.armor_icon)
                    self.canvas.lift(self.backpack_icon)
                    self.minimap.drag(0, 1)
            else:
                move = False
        if self.pers.isDied:
            move = False
            self.canvas.delete(self.skin)
            self.skin = self.canvas.create_image(self.pers.x, self.pers.y,
                                                     image=self.pers.skin)
        if move:
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(0, self.speed, gain=1)
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
            self.canvas.move(self.skin, 0, -self.speed)
            self.canvas.move(self.health.form, 0, -self.speed)
            self.canvas.move(self.health.rect, 0, -self.speed)
            self.canvas.move(self.satiety.form, 0, -self.speed)
            self.canvas.move(self.satiety.rect, 0, -self.speed)
            self.canvas.move(self.menu_button, 0, -self.speed)
            self.canvas.move(self.armor_icon, 0, -self.speed)
            self.canvas.move(self.backpack_icon, 0, -self.speed)
            self.pers.y -= self.speed
            self.health.y -= self.speed
            self.satiety.y -= self.speed
            self.pers.now_skin = self.pers.bot_transpose_skin
            self.canvas.delete(self.pause_icon)
            self.canvas.delete(self.play_icon)
            self.canvas.delete(self.back_icon)
            self.canvas.delete(self.exit_icon)
        if (self.pers.chunk != tile.chunk):
            self.pers.chunk = tile.chunk

            self.addNeighbours(tile.chunk)
            self.renderNeighbours(tile.chunk)
#----------------------------------------------------------------------
    def attack(self, event):
            
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
                i.take_damage(self.pers.power)
                break
    def level(self,lvl):
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(100000, 100000, gain=1)
            self.canvas.scan_mark(0, 0)
            self.canvas.scan_dragto(-50000, -50000, gain=1)

            self.minimap.canvas.scan_mark(0, 0)
            self.minimap.canvas.scan_dragto(100000, 100000, gain=1)
            self.minimap.canvas.scan_mark(0, 0)
            self.minimap.canvas.scan_dragto(-5000, -5000, gain=1)
            #persTile = self.maze.get(0, 0, lvl).tiles[3][3]
            options = {
                'intensity': 0.1,
                'lifespan': 8,
                'loopchance': 0.5,
                'cavechance': 1,
                'chunk_size': 18,
                'block_chance': 0.9,
                'double_entrance': 0.2
            }
            self.maze=Maze(options)
            maze = self.maze
            maze.addChunk(0, 0, lvl)
            persTile = self.maze.get(0, 0, lvl).tiles[3][3]
            self.pers.tile=persTile
            
            #self.canvas.create_rectangle(self.pers.tile.realx,self.pers.tile.realy,self.pers.tile.realx+150,self.pers.tile.realy+150,fill='red)
            self.minimap.canvas.delete('all')
            
            #self.minimap.pers = self.minimap.canvas.create_rectangle(5048,5048,5057,5057, fill ='red')
            for i in self.canvas.find_all():
                if(i!=self.backpack_icon and i!=self.menu_button and i!= self.armor_icon):
                    self.canvas.delete(i)
            self.satiety.change(self.satiety.point)
            self.addNeighbours(maze.get(0 , 0, lvl))
            self.renderNeighbours(maze.get(0 , 0, lvl))
            self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
            self.mcb.addPortal(self.pers.tile.neighbours[0],self,lvl)
            self.pers.x=self.pers.tile.realx+50
            self.pers.y=self.pers.tile.realy+50
            #self.mcb.monsters.append(Monster('portal',self.pers.tile.neighbours[0],self,lvl))
         
            #self.mcb.monsters[-1].target=self.pers.tile
            #self.canvas.lift(self.backpack_icon)
            self.canvas.delete(self.backpack_icon)
            self.canvas.delete(self.menu_button)
            self.canvas.delete(self.armor_icon)
            self.canvas.delete(self.health)
            self.canvas.delete(self.satiety)
            self.health = Health(self.canvas, self.pers.health, persTile.realx + 250, persTile.realy - 420, persTile, "red",
                                 200, 200, self.pers.health)
            self.satiety = Health(self.canvas, self.pers.satiety, persTile.realx + 270, persTile.realy - 380, persTile,
                                  'yellow', 150, 100, self.pers.satiety)
            self.menu_button = self.canvas.create_image(persTile.realx - 400, persTile.realy - 420, image=self.menu)
            self.canvas.tag_bind(self.menu_button, "<Button-1>", self.menu_label)
            self.backpack_icon = self.canvas.create_image(self.pers.x - 460, self.pers.y, image=self.backpack)
            self.canvas.tag_bind(self.backpack_icon, "<Button-1>", self.backpack_func)
            self.armor_icon = self.canvas.create_image(self.pers.x - 460, self.pers.y - 200, image=self.armor)
            self.canvas.tag_bind(self.armor_icon, "<Button-1>", self.armor_func)
            self.canvas.lift(self.backpack_icon)
            self.canvas.lift(self.menu_button)
            self.canvas.lift(self.armor_icon)
            tx = self.pers.tile.realx/10
            ty = self.pers.tile.realy/10
            self.minimap.pers = self.minimap.canvas.create_rectangle(tx+3,ty+3,tx+13,ty+13, fill ='red')
            #self.canvas.create_rectangle(self.pers.tile.realx,self.pers.tile.realy,self.pers.tile.realx+150,self.pers.tile.realy+150,fill='red')
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
                self.mcb.addPortal(self.pers.tile.neighbours[0],self,chunk.z)
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
