from PIL import ImageTk, Image
from random import randint
class Minotavr:
    def __init__(self, x, y, speed, attack):
        skin = Image.open("img/Minotavr.png")
        skin = skin.resize((100, 100), Image.ANTIALIAS)
        died_skin = skin.rotate(90)
        transpose_skin = skin.transpose(Image.FLIP_LEFT_RIGHT)
        transpose_died_skin = transpose_skin.rotate(90)
        skin = ImageTk.PhotoImage(skin)
        died_skin = ImageTk.PhotoImage(died_skin)
        transpose_skin = ImageTk.PhotoImage(transpose_skin)
        transpose_died_skin = ImageTk.PhotoImage(transpose_died_skin)

        back_skin = Image.open('img/Minotavr_bottom_view.png')
        back_skin = back_skin((100, 100), Image.ANTIALIAS)
        died_back_skin = back_skin.rotate(90)
        transpose_back_skin = back_skin.transpose(Image.FLIP_LEFT_RIGHT)
        transpose_died_back_skin = transpose_back_skin.rotate(90)
        back_skin = ImageTk.PhotoImage(back_skin)
        died_back_skin = ImageTk.PhotoImage(died_back_skin)
        transpose_back_skin = ImageTk.PhotoImage(transpose_back_skin)
        transpose_died_back_skin = ImageTk.PhotoImage(transpose_died_back_skin)

        self.skin = skin
        self.transpose_skin = transpose_skin
        self.speed = speed
        self.health = 1000
        self.died_skin = died_skin
        self.died_back_skin = died_back_skin
        self.transpose_died_skin = transpose_died_skin
        self.transpose_died_back_skin = transpose_died_back_skin
        self.faced_north = True
        self.faced_east = False
        self.bot_skin = back_skin
        self.transpose_bot_skin = transpose_back_skin
        self.coords = {}
        self.coords.x = 0
        self.coords.y = 0
        self.attack = attack
        self.x = x
        self.y = y
        self.isDied = False

    def attack(self):
        attack_value = randint(0.9 * self.attack, 1.1 * self.attack)
        return attack_value

    def die(self):
        self.health = 0
        self.skin = self.died_skin
        self.isDied = True

    def take_damage(self, damage):
        if self.health < damage:
            self.die()
            return
        else:
            self.health -= damage