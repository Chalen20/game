import Labyrynth
import pers
import Renderer
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
        pass
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
        

#-------------gameCycle----------------
stop=False
gc = GameController()
def run():
  if(not stop):
      gc.loop()
      run()
      sleep(0.05)
