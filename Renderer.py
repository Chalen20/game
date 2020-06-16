class Renderer:
    def __init__(self,gui):
        self.size=gui.size
        self.gui=gui
        self.x=self.gui.x
        self.y=self.gui.y
        self.canvas=self.gui.canvas
    def renderChunk(self,chunk):
       for i in chunk.tiles:
           for j in i:
               self.renderTile(j,chunk.x,chunk.y,chunk)
    def renderTile(self,tile,cx,cy,chunk):
        
        size = self.size
        x= self.x+size*(tile.x+cx*chunk.size)
        y= self.y+size*(tile.y+cy*chunk.size)
        if not tile.connections[0]:
            self.addWall(x,y,x+size,y+1)
        if not tile.connections[1]:
            self.addWall(x,y,x+1,y+size)
        if not tile.connections[2]:
            self.addWall(x+size,y+1,x+size,y+size)
        if not tile.connections[3]:
            self.addWall(x+1,y+size,x+size,y+size)
    def addWall(self,x1,y1,x2,y2):
        self.canvas.create_rectangle(x1,y1,x2,y2)
        
        
    
