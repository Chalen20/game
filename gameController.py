from Labyrynth import Maze
#import pers
from Renderer import Renderer
from tkinter import*
from time import*
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
        self.size=10
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
        self.maze.addChunk(0,1,0)
        self.maze.addChunk(1,1,0)
        self.maze.addChunk(1,0,0)
        self.maze.addChunk(1,2,0)
        self.maze.addChunk(2,1,0)
        self.maze.addChunk(1,2,0)
        self.maze.addChunk(2,2,0)
        self.maze.addChunk(0,2,0)
        self.maze.addChunk(2,0,0)
        self.canvas.create_rectangle(0,0,20,20, outline="black", fill='black')
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t==0: 
                        ren.renderChunk(self.maze.chunks[i][j][t])
        self.canvas.scan_mark(0,0)
        #self.canvas.scan_dragto(-5000,-5000,gain=1)
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
