SOUTH=0
WEST=2
EAST=1
NORTH=3
from tkinter import *
from random import*
from time import sleep
#
#options={
#            'intensity':0.1,
#            'lifespan':8,
#            'loopchance':0.5,
#            'cavechance':0.5,
##            Chunck options:
#            'chunk_size':18,
#            'block_chance':0.9,
#            'double_entrance':0.2
#        }
#
#------------------------------------------------------------

#------------------------------------------------------------
#Maze:
#   Chunk(every chunk has the same tile numeration but ech chunk has it`s own x y z):
#       Tile(has main property - connections which tiles it is connectd to)
#
#
class Maze:
    def __init__(self,opt):
        options={
            'intensity': opt['intensity'],
            'lifespan':opt['lifespan'],
            'loopchance':opt['loopchance'],
            'cavechance':opt['cavechance']            
        }
        self.chunkOptions={
            'chunk_size':opt['chunk_size'],
            'block_chance':opt['block_chance'],
            'double_entrance':opt['double_entrance'],
            
        }
        self.rooms=[]
        self.chunks = {}
        self.cb=CollectiveBrain(options)
        self.chunks[0]={}
        self.chunks[0][0]={}
        self.chunks[0][0][0]={}
        self.unoMap={}
        self.unoMap[0]={}
        self.unoMap[0][0]={}
        self.unoMap[0][0][0]={}
        
        
    def addChunk(self,x,y,z):
        if(self.get(x,y,z)):
            return
        #print(x,y,z)
        c=Chunk(self.chunkOptions,x,y,z,self)
        southN=self.get(x,y-1,z)
        northN=self.get(x,y+1,z)
        westN=self.get(x+1,y,z)
        eastN=self.get(x-1,y,z)
        self.cb.setChunk(c)
        room = self.cb.createChunk(c.tiles[0][0])     
        if southN:
            c.connect(southN,SOUTH)
        if westN:
            c.connect(westN,WEST)
        if eastN:
            c.connect(eastN,EAST)
        if northN:
            c.connect(northN,NORTH)
        self.rooms.append(room)
        self.add(x,y,z,c)
    def getTiles(self,x,y,deltax,deltay):
        pass
        
     
        
    def add(self,x,y,z,item):
        if not x in self.chunks:
            self.chunks[x]={}
        if not y in self.chunks[x]:
            self.chunks[x][y]={}
        self.chunks[x][y][z]=item  

    def get(self,x,y,z):
        if not x in self.chunks:
            return False
        if not y in self.chunks[x]:
            return False
        if not z in self.chunks[x][y]:
            return False
        return self.chunks[x][y][z]

    def addTile(self,x,y,z,item):
        if not x in self.unoMap:
            self.unoMap[x]={}
        if not y in self.unoMap[x]:
            self.unoMap[x][y]={}
        self.unoMap[x][y][z]=item  

    def getTile(self,x,y,z):
        if not x in self.unoMap:
            return False
        if not y in self.unoMap[x]:
            return False
        if not z in self.unoMap[x][y]:
            return False
        return self.unoMap[x][y][z]
class Chunk:
    def __init__(self,options,x,y,z,maze):
        self.drawings=[]
        self.rendered=False
        self.x=x
        self.y=y
        self.z=z
        self.size=options['chunk_size']
        self.block_chance=options['block_chance']
        self.e_chance=options['double_entrance']
        self.tiles=[]
        self.chunkExits=[None,None,None,None]
        self.neighbours=[]
        for i in range(options['chunk_size']):
            self.tiles.append([])
            for j in range(options['chunk_size']):
                tile=Tile(i,j,x,y,self)
                self.tiles[i].append(tile);
                x1=self.x*(self.size)+i
                y2=self.y*(self.size)+j
                z3=self.z
                if(x1==0 and y2==0 and z3==0):
                    print(x1,y2,z3)
                maze.addTile(x1,y2,z3,tile)
                if(i>0):
                    self.tiles[i][j].addNeighbour(EAST,self.tiles[i-1][j])
                if(j>0):
                    self.tiles[i][j].addNeighbour(SOUTH,self.tiles[i][j-1])
    
    #def generateExits(self,southExit,eastExit,westExit,northExit):
    #        self.self.chunkExits=[southExit,eastExit,westExit,northExit]
    def connect(self,chunk,direction):
        
        exits=0
        def genEx(x,y,exits):
            blocked=False
            for i in self.chunkExits:
                if(i):
                    blocked=True
                    break
            if(blocked and random()>self.block_chance):
                blocked=False
            #print(blocked,self.block_chance)
            for t in range(self.size):
                cx=x
                cy=y
                if(y is False):
                    cy=t
                    oy=t
                else:
                    oy=chunk.size-1-cy
                if(x is False):
                    cx=t
                    ox=t
                else:
                    ox=chunk.size-1-cx
                    
                i=self.tiles[cx][cy]
                i.addNeighbour(direction,chunk.tiles[ox][oy])
                rand = random()
                if not blocked and exits<3 and (random()<t/(chunk.size-1) or rand<self.e_chance):
                    exits+=1         
                    i.connect(chunk.tiles[ox][oy])
                    self.chunkExits[direction]=i
       
        if direction==EAST:
            genEx(0,False,exits)
        if direction==SOUTH:
            genEx(False,0,exits)
        if direction==NORTH:
            genEx(False,chunk.size-1,exits)
        if direction==WEST:
            genEx(chunk.size-1,False,exits)
        
            
        
class Tile:
    def __init__(self,x,y,cx,cy,chunk):
        self.room=False
        self.visible=False
        self.chunk=chunk
        self.x=x
        self.y=y
        self.chunk_x=cx
        self.chunk_y=cy
        self.mazex=cx*(self.chunk.size)+x
        self.mazey=cy*(self.chunk.size)+y
        self.connections =[False,False,False,False]
        self.neighbours =[False,False,False,False]
    def addNeighbour(self,direction,tile):
        self.neighbours[direction]=tile
        tile.neighbours[3-direction]=self
    def connect(self,tile):
            self.connections[self.neighbours.index(tile)]=tile
            tile.connections[3-self.neighbours.index(tile)]=self
class Room:
    def __init__(self,x,y,deltax,deltay,chunk):
        self.tiles=[]
        self.x=x
        self.y=y
        self.deltax=deltax
        self.deltay=deltay
        self.chunk=chunk
        self.isFree=True
        
#---------------------------------------------------------------
#CollectiveBrain(coordinate work of all labBuilders):
#   LabBuilder
#
class CollectiveBrain:
    def __init__(self,options):
        self.chunk=None
        self.intensity=options['intensity']
        self.lifespanlength = options['lifespan']
        self.loopChance= options['loopchance']
        self.caveChance=options['cavechance']
    def setChunk(self,chunk):
        self.chunk = chunk
    def createChunk(self,enterPoint):
        self.team=[]
        self.pool=[]
        self.addBuilder(enterPoint)
        while len(self.pool)< self.chunk.size*self.chunk.size :
            
            for i in self.team:
                
                result = i.findAndMove(self.pool)
               
                if result['tile']:
                    self.pool.append(result['tile'])
                if result['newBorn']:
                    self.team.append(result['newBorn'])
                if i.requestToDie() and len(self.team)>2:
                    i.die()
                    self.team.remove(i)
                    del i
        if(random()<self.caveChance):
            return self.addRoom()
    def addRoom(self):
        x=round(self.chunk.size/2-3)+randint(0,3)
        y=round(self.chunk.size/2-3)+randint(0,3)
        sizex=3+randint(0,3)
        sizey=3+randint(0,3)
        room = Room(x,y,sizex,sizey,self.chunk)
        for i in range(sizex):
            for j in range(sizey):
                nt=self.chunk.tiles[x+i][y+j]
                nt.room=room
                room.tiles.append(nt)
                #nt=self.chunk.tiles[x+i][y+j]
                nt.connect(self.chunk.tiles[x+i-1][y+j])
                nt.connect(self.chunk.tiles[x+i][y+j-1])
                
        return room
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
       
        self.died=False
    def move(self,tile):
        
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
            
            tile=possible[randint(0,len(possible)-1)]
           
            
            result['tile']=self.move(tile)

            
           
            
        return result
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
#------------------------------------------------------------
#Temporary Renderer
#
class GUI:
    def __init__(self):
        window=Tk()
        canvas = Canvas(window,width=640,height=640,bg='white')
        canvas.pack()
        ren = Renderer(canvas)
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
         
        for i in self.maze.chunks:
            for j in self.maze.chunks[i]:
                for t in self.maze.chunks[i][j]:
                    if t==0:
                        
                        ren.renderChunk(self.maze.chunks[i][j][t])
class Renderer:
    def __init__(self,canvas):
        self.canvas=canvas
    def renderChunk(self,chunk):
       for i in chunk.tiles:
           for j in i:
               self.renderTile(j,chunk.x,chunk.y)
    def renderTile(self,tile,cx,cy):
        
        size =10
        x = tile.x*10+180*cx
        y = tile.y*10+180*cy
        if not tile.connections[0]:
            self.canvas.create_line(x,y,x+10,y)
        if not tile.connections[1]:
            self.canvas.create_line(x,y,x,y+10)
        if not tile.connections[2]:
            self.canvas.create_line(x+10,y,x+10,y+10)
        if not tile.connections[3]:
            self.canvas.create_line(x,y+10,x+10,y+10)
GUI()
  

