SOUTH=0
WEST=2
EAST=1
NORTH=3
from tkinter import *
from random import*
from time import sleep

#------------------------------------------------------------
#Temporary Renderer
#
class GUI:
    def __init__(self):
        window=Tk()
        canvas = Canvas(window,width=300,height=300,bg='white')
        canvas.pack()
        c=Chunk({'chunk_size':16},0,0)
        ren = Renderer(canvas)
        cb = CollectiveBrain()
        cb.setChunk(c)
        cb.createChunk(c.tiles[0][0])
        ren.renderChunk(c)
    
class Renderer:
    def __init__(self,canvas):
        self.canvas=canvas
    def renderChunk(self,chunk):
       for i in chunk.tiles:
           for j in i:
               self.renderTile(j)
    def renderTile(self,tile):
        print('tile: '+str(tile.x)+" "+str(tile.y)+'con:')
        self.betterTiles(tile.connections)
        size =10
        x= tile.x*10
        y= tile.y*10
        if not tile.connections[0]:
            self.canvas.create_line(x,y,x+10,y)
        if not tile.connections[1]:
            self.canvas.create_line(x,y,x,y+10)
        if not tile.connections[2]:
            self.canvas.create_line(x+10,y,x+10,y+10)
        if not tile.connections[3]:
            self.canvas.create_line(x,y+10,x+10,y+10)
    def renderBuilder(self,b):
         self.canvas.create_rectangle(b.x*10,b.y*10,b.x*10+10,b.y*10+10,fill='red')
    def betterTiles(self, tiles):
        for i in tiles:
            if i :
                print(str(i.x)+' '+str(i.y))
        print()
#------------------------------------------------------------
#Labyrynth:
#   Chunk(every chunk has the same tile numeration but ech chunk has it`s own x y z):
#       Tile(has main property - connections which tiles it is connectd to)
#
#
class Labyrynth:
    def __init__(self,options):
        self.chunks =[[[]]]
        
    
        

class Chunk:
    def __init__(self,options,x,y):
        self.x=x
        self.y=y
        self.size=options['chunk_size']
        self.tiles=[]
        self.chunkExits=[]
        #self.generateExits(0,0,0,0)
        for i in range(options['chunk_size']):
            self.tiles.append([])
            for j in range(options['chunk_size']):
                self.tiles[i].append(Tile(i,j,x,y));
                if(i>0):
                    self.tiles[i][j].addNeighbour(EAST,self.tiles[i-1][j])
                if(j>0):
                    self.tiles[i][j].addNeighbour(SOUTH,self.tiles[i][j-1])
    #def neighbours(self,tile):
    #    result=[None,None,None,None]
    #    #y x reversed    
    #    x=tile.x
    #    y=tile.y
    #    if(x>0):
    #        result[SOUTH]=self.tiles[x][y-1]
    #    if(y>0):
    #        result[WEST]=self.tiles[x-1][y]
    #    if(y+2<self.size):
    #        result[NORTH]=self.tiles[x][y+1]
    #    if(x+2<self.size):
    #        result[EAST]=self.tiles[x+1][y]
    #    return result
    def generateExits(self,southExit,eastExit,westExit,northExit):
            self.self.chunkExits=[southExit,eastExit,westExit,northExit]
                   
class Tile:
    def __init__(self,x,y,cx,cy):
        self.x=x
        self.y=y
        self.chunk_x=cx
        self.chunk_y=cy
        self.connections =[False,False,False,False]
        self.neighbours =[False,False,False,False]
    def addNeighbour(self,direction,tile):
        self.neighbours[direction]=tile
        tile.neighbours[3-direction]=self
    def connect(self,tile):
        #if self.connections[self.neighbours.index(tile)]==tile:
            self.connections[self.neighbours.index(tile)]=tile
            #if tile.connections[3-self.neighbours.index(tile)]==False:
            tile.connections[3-self.neighbours.index(tile)]=self
        
#---------------------------------------------------------------
#CollectiveBrain(coordinate work of all labBuilders):
#   LabBuilder
#
class CollectiveBrain:
    def __init__(self):
        self.chunk=None
        self.intensity=0.1
        self.lifespanlength = 6
        self.loopChance=0.2
    def setChunk(self,chunk):
        self.chunk = chunk
    def createChunk(self,enterPoint):
        self.team=[]
        self.pool=[]
        self.addBuilder(enterPoint)
        while len(self.pool)< self.chunk.size*self.chunk.size :
            print(len(self.pool))
            for i in self.team:
                
                result = i.findAndMove(self.pool)
                print(result)
                if result['tile']:
                    self.pool.append(result['tile'])
                if result['newBorn']:
                    self.team.append(result['newBorn'])
                if i.requestToDie() and len(self.team)>2:
                    i.die()
                    self.team.remove(i)
                    del i
            
        #print(self.pool)         
    def addBuilder(self,tile):
        self.team.append(LabBuilder(tile.x,tile.y,tile,self.lifespanlength,self.intensity,self.loopChance))
        self.pool.append(tile)
        
class LabBuilder:
    def __init__(self,x,y,tile,length,intensity,chance):
        self.x=x
        self.y=y
        self.lifespan=0
        self.maxLifespan=length
        self.intensity=intensity
        self.loopChance=chance
        self.currentTile=tile
        self.memory=[]
        #self.memory.append(tile)
        self.died=False
    def move(self,tile):
        #print(neighbours)
        #self.betterTiles(neighbours)
        self.memory.append(self.currentTile)
        self.currentTile.connect(tile)
        self.currentTile=tile
        self.x=self.currentTile.x
        self.y=self.currentTile.y
        self.lifespan+=1
        return self.currentTile
    def findAndMove(self,pool):
        result={'newBorn':False,'tile':False}
        possible = []
        for i in  self.currentTile.neighbours:
            if i and not i in pool:
                possible.append(i)
        if self.lifespan>self.maxLifespan and random()<0.05*(self.lifespan+1-self.maxLifespan):
                self.died=True
            
        if len(possible)==0:
            if(len(self.memory)==0):
               self.died=True
            self.currentTile=self.memory.pop(len(self.memory)-1)
            self.x=self.currentTile.x
            self.y=self.currentTile.y

        else:
            tile=possible[randint(0,len(possible)-1)]
            if len(possible)>1 and random()<self.intensity:
                possible.remove(tile)
                tile=possible[randint(0,len(possible)-1)]
                result['newBorn']=self.born(tile)
            #self.betterTiles(possible)
            tile=possible[randint(0,len(possible)-1)]
            #direction=self.getDirection(self.currentTile,tile)
            #print(str(self.currentTile.x)+" "+str(self.currentTile.y)+"   "+str(tile.x)+" "+str(tile.y)+'  '+str(direction))
            result['tile']=self.move(tile)
            self.betterTile(result['tile'])
            #pool.append(result['tile'])
            
        return result
    def betterTile(self,tile):
        print(str(tile.x)+' '+str(tile.y))
    def betterTiles(self, tiles):
        for i in range(len(tiles)):
            
            if tiles[i] :
                print(str(tiles[i].x)+' '+str(tiles[i].y)+"  "+str(i))
        print()
    
    def die(self):
        
        tile=self.currentTile.neighbours[randint(0,3)]
          
        if tile and random()<self.loopChance*4:   
           self.move(tile)
    def born(self,tile):
        self.currentTile.connect(tile)
        newBorn=LabBuilder(tile.x,tile.y,tile,self.maxLifespan,self.intensity,self.loopChance)
        newBorn.memory=self.memory
        return newBorn
    def requestToDie(self):
        die = self.died
        self.died=False
        return die
        
GUI()
