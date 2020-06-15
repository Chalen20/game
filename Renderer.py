class Renderer:
    def __init__(self,gui):
        self.tileWidth=gui.size
        self.gui=gui
        self.x=self.gui.x
        self.y=self.gui.y
    def drawChunk(self,canvas,chunk):
        
    def drawTile(self,tile,size):
        x= self.x+self.tileWidth*(tile.x+size*cx
        y= tile.y*10+180*cy
        if not tile.connections[0]:
            self.canvas.create_line(x,y,x+10,y)
        if not tile.connections[1]:
            self.canvas.create_line(x,y,x,y+10)
        if not tile.connections[2]:
            self.canvas.create_line(x+10,y,x+10,y+10)
        if not tile.connections[3]:
            self.canvas.create_line(x,y+10,x+10,y+10)
    
    def drawWalls(x1,y1,x2,y2):
        
        
        
    
