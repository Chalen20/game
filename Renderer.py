from PIL import Image, ImageTk
class Renderer:
    def __init__(self, gui):
        self.size = gui.size
        self.gui = gui
        self.x = self.gui.x
        self.y = self.gui.y
        self.canvas = self.gui.canvas
        self.mini = self.gui.minimap.canvas
        self.chunk = ''
        tile_bg = Image.open("img/patern3.png")
        self.tile_bg = ImageTk.PhotoImage(tile_bg.resize((self.size, self.size), Image.ANTIALIAS))

    def renderChunk(self, chunk):
        self.chunk = chunk
        if chunk.rendered:
            for i in chunk.drawings:
                if (i != self.gui.backpack_icon and i != self.gui.menu_button and i != self.gui.armor_icon and
                        i != self.gui.health.form and i != self.gui.health.rect and i != self.gui.satiety.form and
                        i != self.gui.satiety.rect):
                    self.canvas.delete(i)
        if not chunk:
            return
        chunk.rendered = True
        for i in chunk.tiles:
           for j in i:
               self.renderTile(j, chunk.x, chunk.y, chunk)

    def renderTile(self, tile, cx, cy, chunk):
        size = self.size
        x = self.x+size*(tile.x+cx*chunk.size)
        y = self.y+size*(tile.y+cy*chunk.size)
        tile.realx = x
        tile.realy = y
        
        if not tile.connections[0]:
            self.addWall(x, y, x+size, y+5)
        if not tile.connections[1]:
            self.addWall(x, y, x+5, y+size)
        if not tile.connections[2]:
            self.addWall(x+size, y, x+size-5, y+size)
        if not tile.connections[3]:
            self.addWall(x, y+size, x+size, y+size-5)
        self.chunk.drawings.append(self.canvas.create_image(x+self.size/2, y+self.size/2, image=self.tile_bg))
        self.canvas.lower(self.chunk.drawings[-1])

    def addWall(self, x1, y1, x2, y2):
        self.chunk.drawings.append(self.canvas.create_rectangle(x1, y1, x2, y2, fill='red'))
        self.canvas.lower(self.chunk.drawings[-1])
        self.chunk.drawings.append(self.mini.create_line(int(x1/10), int(y1/10), int(x2/10), int(y2/10),
                                                         width=2, fill='black'))
        self.canvas.lower(self.chunk.drawings[-1])
        
    def renderVisibility(self, tile, vis, tiles):
        t = tile
        c = t.chunk.z
        self.gui.visible = [[], []]
        self.gui.visible.append(t)
        for i in vis:
            self.canvas.delete(i)
        for i in range(0, 4):
            while tile.connections[i]:
                tile=tile.connections[i]
                tile.visible=True
                self.gui.visible[0].append(tile)
            if not tile == t:
                 self.gui.visible[1].append(tile)
            tile = t
        self.gui.visible[0].append(tile)
        tile.visible = True
        if tile.room:
            for i in tile.room.tiles:
                i.visible = True
                self.gui.visible[0].append(i)
        for i in range(tile.mazex-4, tile.mazex+4):
            for j in range(tile.mazey-4, tile.mazey+4):
                a = tiles.getTile(i, j, c)
                if a:
                    if not a.visible:
                        vis.append(self.canvas.create_rectangle(a.realx, a.realy, a.realx+self.size, a.realy+self.size,
                                                                fill='black'))
                    a.visible = False
