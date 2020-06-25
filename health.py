from PIL import Image, ImageTk

class Health:
    def __init__(self, canvas, point, x, y, tile, color, width, height, maxv):
        self.x = x - 85 * width/200
        self.y = y - 15 * height/200
        self.point = point
        self.tile = tile
        self.canvas = canvas
        self.color = color
        self.width = width
        self.maxv = maxv
        self.height = height
        if self.point > maxv:
            self.point = maxv
        self.health_line = Image.open("img/health_line.png")
        self.image = ImageTk.PhotoImage(self.health_line.resize((width, height), Image.ANTIALIAS))
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.point * 1.75 * width/200,
                                                 self.y + 20 * height/200, fill=self.color)
        self.form = self.canvas.create_image(self.x + 85 * width/200, self.y + 15 * height/200, image=self.image)
    def change(self, points):
        if points < 0:
            points = 0
        if points > self.maxv:
            points = self.maxv
        self.canvas.delete(self.rect)
        self.canvas.delete(self.form)
        self.point = points
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + points * 175/self.maxv * self.width/200,
                                                self.y + 20 * self.height/200, fill=self.color)
        #print(self.canvas.coords(self.rect))
        self.form = self.canvas.create_image(self.x + 85 * self.width/200, self.y + 15*self.height/200,
                                             image=self.image)
