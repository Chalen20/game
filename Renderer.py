from PIL import Image, ImageTk
class Renderer:
    def __init__(self, gui):
        self.size = gui.size
        self.gui = gui
        self.x = self.gui.x
        self.y = self.gui.y
        self.canvas = self.gui.canvas
        self.chunk=''
        tile_bg = Image.open("img/patern.png")
        self.tile_bg=ImageTk.PhotoImage(tile_bg.resize((self.size, self.size), Image.ANTIALIAS))
    def renderChunk(self, chunk):
        self.chunk=chunk
        #tile_bg = Image.open("img/patern.png")
        #self.tile_bg=ImageTk.PhotoImage(tile_bg.resize((97, 97), Image.ANTIALIAS))
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
        
        #self.skin = self.canvas.create_image(x,y)
        size = self.size
        x = self.x+size*(tile.x+cx*chunk.size)
        y = self.y+size*(tile.y+cy*chunk.size)
        tile.realx=x
        tile.realy=y
        
        if not tile.connections[0]:
            self.addWall(x, y, x+size, y+5)
        if not tile.connections[1]:
            self.addWall(x, y, x+5, y+size)
        if not tile.connections[2]:
            self.addWall(x+size, y, x+size-5, y+size)
        if not tile.connections[3]:
            self.addWall(x, y+size, x+size, y+size-5)
        self.chunk.drawings.append(self.canvas.create_image(x-50,y-50,image=self.tile_bg))
        self.canvas.lower(self.chunk.drawings[-1])
    def addWall(self, x1, y1, x2, y2):
        self.chunk.drawings.append(self.canvas.create_rectangle(x1, y1, x2, y2,fill='red'))
        self.canvas.lower(self.chunk.drawings[-1])
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
        if(tile.room):
            for i in tile.room.tiles:
                i.visible=True
        #vis.append(self.canvas.create_rectangle(a.realx+100,a.realy+100,a.realx+100+self.size,a.realy+100+self.size,fill='black'))
        #print(a.realx,a.realy)
        for i in range(tile.mazex-4,tile.mazex+4):
            for j in range(tile.mazey-4,tile.mazey+4):
                a=tiles.getTile(i,j,0)
                if(a):
                    #print(a)
                    if(not a.visible):
                        vis.append(self.canvas.create_rectangle(a.realx,a.realy,a.realx+self.size,a.realy+self.size,fill='black'))
                    a.visible=False    
                        
                    
            
            
        








        
