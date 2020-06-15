class Renderer:
    def __init__(self,gui):
        self.tileWidth=gui.size
        self.gui=gui
        self.x=self.gui.x
        self.y=self.gui.y
        self.canvas=self.gui.canvas
    def renderChunk(self,chunk):
       for i in chunk.tiles:
           for j in i:
               self.renderTile(j,chunk.x,chunk.y)
    def renderTile(self,tile,cx,cy):
        
        size =10
        x= tile.x*50+900*cx
        y= tile.y*50+900*cy
        if not tile.connections[0]:
            self.canvas.create_rectangle(x,y,x+50,y+1)
        if not tile.connections[1]:
            self.canvas.create_rectangle(x,y,x+1,y+50)
        if not tile.connections[2]:
            self.canvas.create_rectangle(x+50,y+1,x+50,y+50)
        if not tile.connections[3]:
            self.canvas.create_rectangle(x+1,y+50,x+50,y+50)
        
        
    
