from Labyrynth import Maze
from Renderer import Renderer
from tkinter import *
from pers import Pers
from PIL import Image, ImageTk
from time import *
#from testPers import *

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

    def __init__(self, name, visib):
        self.size = 150
        self.x = 50000
        self.y = 50000
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=800)
        self.ren = Renderer(self)
        self.time = 0
        self.name = name
        self.visib = visib

        self.visibility = []
        self.canvas.configure(scrollregion=(0, 0, 100000, 100000))
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

        options = {
            'intensity': 0.1,
            'lifespan': 8,
            'loopchance': 0.5,
            'cavechance': 0.5,
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

        self.canvas.create_rectangle(0, 0, 20, 20, outline="black", fill='black')
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t == 0:
                        self.ren.renderChunk(self.maze.chunks[i][j][t])
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(-50000, -50000, gain=1)
        persTile = self.maze.get(0, 0, 0).tiles[3][3]
        self.pers = Pers(self.name, persTile.realx+50, persTile.realy+50, persTile)
        self.skin = self.canvas.create_image(self.pers.x, self.pers.y, image=self.pers.skin)
        pers = self.pers
        speed = pers.speed
        pers.chunk = self.maze.get(0, 0, 0)
        self.right_steps_counter = 0
        if not visib:
            self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
        def onKeyLeft(event):

            tile = pers.tile
            move = True
            if (tile.realx > pers.x - speed):

                if (tile.connections[1]):

                    pers.tile = tile.connections[1]
                    if not visib:
                        self.ren.renderVisibility(self.pers.tile, self.visibility, self.maze)
                else:
                    move = False
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
                pers.x -= speed
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
                else:
                    move = False
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
                pers.x += speed

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
                else:
                    move = False
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
                pers.y += speed
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
                else:
                    move = False
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
                pers.y -= speed
            if (pers.chunk != tile.chunk):
                pers.chunk = tile.chunk

                self.addNeighbours(tile.chunk)
                self.renderNeighbours(tile.chunk)

        self.root.bind('<Left>', onKeyLeft)
        self.root.bind('<Right>', onKeyRight)
        self.root.bind('<Up>', onKeyUp)
        self.root.bind('<Down>', onKeyDown)
        self.root.mainloop()

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

    def scroll_start(self, event):
        # print("from",event.x,event.y)
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        # if(event.x>
        # print("to",event.x,event.y)
        self.canvas.scan_dragto(event.x, event.y, gain=1)


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
