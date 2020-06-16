from Labyrynth import Maze
#import pers
from Renderer import Renderer
from tkinter import*
from time import*
from testPers import*
options={
    'intensity':0.1,
    'lifespan':8,
    'loopchance':0.5,
    'cavechance':0.5,
    'chunk_size':18,
    'block_chance':0.9,
    'double_entrance':0.2
}
class GUI:
    
    def __init__(self):
        self.size=75
        self.x=5000
        self.y=5000
        root=Tk()
        self.canvas = Canvas(root, width=800, height=800, background="bisque")
        ren=Renderer(self)
        
       
        
        
        self.canvas.configure(scrollregion=(0,0,10000,10000))
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)


        options={
            'intensity':0.1,
            'lifespan':8,
            'loopchance':0.5,
            'cavechance':0.5,
            'chunk_size':18,
            'block_chance':0.9,
            'double_entrance':0.2
        }
        self.maze=Maze(options)
        self.maze.addChunk(0,0,0)
        self.maze.addChunk(0,-1,0)
        self.maze.addChunk(1,-1,0)
        self.maze.addChunk(-1,0,0)
        self.maze.addChunk(-1,1,0)
        self.maze.addChunk(1,1,0)
        self.maze.addChunk(1,0,0)
        self.maze.addChunk(0,1,0)
        self.maze.addChunk(-1,-1,0)
        
        self.canvas.create_rectangle(0,0,20,20, outline="black", fill='black')
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t==0: 
                        ren.renderChunk(self.maze.chunks[i][j][t])
        self.canvas.scan_mark(0,0)
        self.canvas.scan_dragto(-5000,-5000,gain=1)
        persTile=self.maze.get(0,0,0).tiles[5][5]
        self.pers=TestPers(persTile.realx,persTile.realy,persTile)
        rect=self.canvas.create_rectangle(self.pers.x,self.pers.y,self.pers.x+10,self.pers.y+10,fill='red')

        pers=self.pers
        speed=pers.speed
        def onKeyLeft(event):
        
            tile=pers.tile
            move=True
            if(tile.realx>pers.x-speed):
                
                if(tile.connections[1]):
                    pers.tile=tile.connections[1]
                else:
                    move=False
            if move:
                self.canvas.scan_mark(0,0)
                self.canvas.scan_dragto(int(speed/10),0) 
                self.canvas.move(rect,-speed,0)
                pers.x-=speed
        def onKeyRight(event):
            move=True
            tile =pers.tile
            if(tile.realx+self.size-pers.size<pers.x+speed):
                
                if(tile.connections[2]):
                    pers.tile=tile.connections[2]
                else:
                    move=False
            if move:
                self.canvas.scan_mark(0,0)
                self.canvas.scan_dragto(int(-speed/10),0) 
                self.canvas.move(rect,speed,0)
                pers.x+=speed
        def onKeyDown(event):
            move=True
            tile =pers.tile
            if(tile.realy+self.size-pers.size<pers.y+speed):
                
                if(tile.connections[3]):
                    pers.tile=tile.connections[3]
                else:
                    move=False
            if move:
                self.canvas.scan_mark(0,0)
                self.canvas.scan_dragto(0,int(-speed/10)) 
                self.canvas.move(rect,0,speed)
                pers.y+=speed
        def onKeyUp(event):
            move=True
            tile =pers.tile
            if(tile.realy>pers.y-speed):
                
                if(tile.connections[0]):
                    pers.tile=tile.connections[0]
                else:
                    move=False
            if move:
                self.canvas.scan_mark(0,0)
                self.canvas.scan_dragto(0,int(speed/10)) 
                self.canvas.move(rect,0,-speed)
                pers.y-=speed
        root.bind('<Left>',onKeyLeft)
        root.bind('<Right>',onKeyRight)
        root.bind('<Up>',onKeyUp)
        root.bind('<Down>',onKeyDown)
        root.mainloop()
    def scroll_start(self, event):
        #print("from",event.x,event.y)
        self.canvas.scan_mark(event.x, event.y)
    def scroll_move(self, event):
        #if(event.x>
        #print("to",event.x,event.y)
        self.canvas.scan_dragto(event.x, event.y, gain=1)
class GameController:
    def __init__(self):
        self.gui=GUI()
        self.time=0
        self.maze=Maze(options)
        self.hero=Pers('pers1')
        self.monsters={
            'normal':[],
            'minotaurs':[]

        }
        self.renderer=Renderer()
        self.villages=[]
        
    def loop(self):
        time+=0.05
        
GUI()

#-------------gameCycle----------------
#stop=False
#gc = GameController()
#def run():
#  if(not stop):
#      gc.loop()
#     run()
#      sleep(0.05)
