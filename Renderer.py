class Renderer:
    def __init__(self, gui):
        self.size = gui.size
        self.gui = gui
        self.x = self.gui.x
        self.y = self.gui.y
        self.canvas = self.gui.canvas
        self.chunk=''
    def renderChunk(self, chunk):
        self.chunk=chunk
        if(chunk.rendered):
            for i in chunk.drawings:
               self.canvas.delete(i) 
        if(not chunk):
            return
        chunk.rendered=True
        for i in chunk.tiles:
           for j in i:
               self.renderTile(j, chunk.x, chunk.y, chunk)
    def renderTile(self,tile,cx,cy,chunk):
        #print(tile.x,tile.y,cx,cy)
        size = self.size
        x = self.x+size*(tile.x+cx*chunk.size)
        y = self.y+size*(tile.y+cy*chunk.size)
        tile.realx=x
        tile.realy=y
        if not tile.connections[0]:
            self.addWall(x, y, x+size, y+1)
        if not tile.connections[1]:
            self.addWall(x, y, x+1, y+size)
        if not tile.connections[2]:
            self.addWall(x+size, y+1, x+size, y+size)
        if not tile.connections[3]:

            self.addWall(x+1, y+size, x+size, y+size)
    def addWall(self, x1, y1, x2, y2):
        self.chunk.drawings.append(self.canvas.create_rectangle(x1, y1, x2, y2))
    def renderVisibility(self,tile,vis,tiles):
        #print(tile)
        t= tile
        for i in vis:
            self.canvas.delete(i)
        while(tile.connections[0]):
            tile=tile.connections[0]
            tile.visible=True
        tile=t
        while(tile.connections[1]):
            tile=tile.connections[1]
            tile.visible=True
        tile=t
        while(tile.connections[2]):
            tile=tile.connections[2]
            tile.visible=True
        tile=t
        while(tile.connections[3]):
            tile=tile.connections[3]
            tile.visible=True
        #print(t.mazey)
        tile=t
        tile.visible=True
        #a=tiles.getTile(0,0,0)
        #vis.append(self.canvas.create_rectangle(a.realx+100,a.realy+100,a.realx+100+self.size,a.realy+100+self.size,fill='black'))
        #print(a.realx,a.realy)
        for i in range(tile.mazex-8,tile.mazex+8):
            for j in range(tile.mazey-8,tile.mazey+8):
                a=tiles.getTile(i,j,0)
                if(a):
                    #print(a)
                    if(not a.visible):
                        vis.append(self.canvas.create_rectangle(a.realx,a.realy,a.realx+self.size,a.realy+self.size,fill='black'))
                    a.visible=False    
                        
                    
            
            
        








        
