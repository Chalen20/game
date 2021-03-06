from random import *
from time import *
from PIL import Image, ImageTk

class Pers():
    def __init__(self, name, x, y, tile, gui):
        front_skin1 = Image.open("img/Pers1.png")
        front_skin1 = front_skin1.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin1 = front_skin1.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation1 = Image.open("img/Pers1_animation1.png")
        front_skin_animation1 = front_skin_animation1.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation1 = front_skin_animation1.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation2 = Image.open("img/Pers1_animation2.png")
        front_skin_animation2 = front_skin_animation2.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation2 = front_skin_animation2.transpose(Image.FLIP_LEFT_RIGHT)

        front_died_skin1 = front_skin1.rotate(90)
        transpose_front_died_skin1 = front_died_skin1.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin1 = Image.open("img/Pers1_bottom_view.png")
        back_skin1 = back_skin1.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin1 = back_skin1.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation1 = Image.open("img/Pers1_bottom_view_animation1.png")
        back_skin_animation1 = back_skin_animation1.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation1 = back_skin_animation1.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation2 = Image.open("img/Pers1_bottom_view_animation2.png")
        back_skin_animation2 = back_skin_animation2.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation2 = back_skin_animation2.transpose(Image.FLIP_LEFT_RIGHT)

        back_died_skin1 = back_skin1.rotate(90)
        transpose_back_died_skin1 = back_died_skin1.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin2 = Image.open("img/Pers4.png")
        front_skin2 = front_skin2.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin2 = front_skin2.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation1_2 = Image.open("img/Pers4_animation1.png")
        front_skin_animation1_2 = front_skin_animation1_2.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation1_2 = front_skin_animation1_2.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation2_2 = Image.open("img/Pers4_animation2.png")
        front_skin_animation2_2 = front_skin_animation2_2.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation2_2 = front_skin_animation2_2.transpose(Image.FLIP_LEFT_RIGHT)

        front_died_skin2 = front_skin2.rotate(90)
        transpose_front_died_skin2 = front_died_skin2.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin2 = Image.open("img/Pers4_bottom_view.png")
        back_skin2 = back_skin2.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin2 = back_skin2.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation1_2 = Image.open("img/Pers4_bottom_view_animation1.png")
        back_skin_animation1_2 = back_skin_animation1_2.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation1_2 = back_skin_animation1_2.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation2_2 = Image.open("img/Pers4_bottom_view_animation2.png")
        back_skin_animation2_2 = back_skin_animation2_2.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation2_2 = back_skin_animation2_2.transpose(Image.FLIP_LEFT_RIGHT)

        back_died_skin2 = back_skin2.rotate(90)
        transpose_back_died_skin2 = back_died_skin2.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin3 = Image.open("img/Pers5.png")
        front_skin3 = front_skin3.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin3 = front_skin3.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation1_3 = Image.open("img/Pers5_animation1.png")
        front_skin_animation1_3 = front_skin_animation1_3.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation1_3 = front_skin_animation1_3.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation2_3 = Image.open("img/Pers5_animation2.png")
        front_skin_animation2_3 = front_skin_animation2_3.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation2_3 = front_skin_animation2_3.transpose(Image.FLIP_LEFT_RIGHT)

        front_died_skin3 = front_skin3.rotate(90)
        transpose_front_died_skin3 = front_died_skin3.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin3 = Image.open("img/Pers5_bottom_view.png")
        back_skin3 = back_skin3.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin3 = back_skin3.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation1_3 = Image.open("img/Pers5_bottom_view_animation1.png")
        back_skin_animation1_3 = back_skin_animation1_3.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation1_3 = back_skin_animation1_3.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation2_3 = Image.open("img/Pers5_bottom_view_animation2.png")
        back_skin_animation2_3 = back_skin_animation2_3.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation2_3 = back_skin_animation2_3.transpose(Image.FLIP_LEFT_RIGHT)

        back_died_skin3 = back_skin3.rotate(90)
        transpose_back_died_skin3 = back_died_skin3.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin4 = Image.open("img/Pers8.png")
        front_skin4 = front_skin4.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin4 = front_skin4.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation1_4 = Image.open("img/Pers8_animation1.png")
        front_skin_animation1_4 = front_skin_animation1_4.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation1_4 = front_skin_animation1_4.transpose(Image.FLIP_LEFT_RIGHT)

        front_skin_animation2_4 = Image.open("img/Pers8_animation2.png")
        front_skin_animation2_4 = front_skin_animation2_4.resize((100, 100), Image.ANTIALIAS)
        transpose_front_skin_animation2_4 = front_skin_animation2_4.transpose(Image.FLIP_LEFT_RIGHT)

        front_died_skin4 = front_skin4.rotate(90)
        transpose_front_died_skin4 = front_died_skin4.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin4 = Image.open("img/Pers8_bottom_view.png")
        back_skin4 = back_skin4.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin4 = back_skin4.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation1_4 = Image.open("img/Pers8_bottom_view_animation1.png")
        back_skin_animation1_4 = back_skin_animation1_4.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation1_4 = back_skin_animation1_4.transpose(Image.FLIP_LEFT_RIGHT)

        back_skin_animation2_4 = Image.open("img/Pers8_bottom_view_animation2.png")
        back_skin_animation2_4 = back_skin_animation2_4.resize((100, 100), Image.ANTIALIAS)
        transpose_back_skin_animation2_4 = back_skin_animation2_4.transpose(Image.FLIP_LEFT_RIGHT)

        back_died_skin4 = back_skin4.rotate(90)
        transpose_back_died_skin4 = back_died_skin4.transpose(Image.FLIP_LEFT_RIGHT)

        allPers = {"pers1": [ImageTk.PhotoImage(front_skin1), ImageTk.PhotoImage(back_skin1), 16, 20, 100,
                             ImageTk.PhotoImage(transpose_front_skin1), ImageTk.PhotoImage(transpose_back_skin1),
                             ImageTk.PhotoImage(front_skin_animation1), ImageTk.PhotoImage(front_skin_animation2),
                             ImageTk.PhotoImage(transpose_front_skin_animation1),
                             ImageTk.PhotoImage(transpose_front_skin_animation2),
                             ImageTk.PhotoImage(back_skin_animation1), ImageTk.PhotoImage(back_skin_animation2),
                             ImageTk.PhotoImage(transpose_back_skin_animation1),
                             ImageTk.PhotoImage(transpose_back_skin_animation2),
                             ImageTk.PhotoImage(front_died_skin1), ImageTk.PhotoImage(transpose_front_died_skin1),
                             ImageTk.PhotoImage(back_died_skin1), ImageTk.PhotoImage(transpose_back_died_skin1)],
                   "pers2": [ImageTk.PhotoImage(front_skin2), ImageTk.PhotoImage(back_skin2), 20, 20, 80,
                             ImageTk.PhotoImage(transpose_front_skin2), ImageTk.PhotoImage(transpose_back_skin2),
                             ImageTk.PhotoImage(front_skin_animation1_2), ImageTk.PhotoImage(front_skin_animation2_2),
                             ImageTk.PhotoImage(transpose_front_skin_animation1_2),
                             ImageTk.PhotoImage(transpose_front_skin_animation2_2),
                             ImageTk.PhotoImage(back_skin_animation1_2), ImageTk.PhotoImage(back_skin_animation2_2),
                             ImageTk.PhotoImage(transpose_back_skin_animation1_2),
                             ImageTk.PhotoImage(transpose_back_skin_animation2_2),
                             ImageTk.PhotoImage(front_died_skin2), ImageTk.PhotoImage(transpose_front_died_skin2),
                             ImageTk.PhotoImage(back_died_skin2), ImageTk.PhotoImage(transpose_back_died_skin2)],
                   "pers3": [ImageTk.PhotoImage(front_skin3), ImageTk.PhotoImage(back_skin3), 12, 30, 110,
                             ImageTk.PhotoImage(transpose_front_skin3), ImageTk.PhotoImage(transpose_back_skin3),
                             ImageTk.PhotoImage(front_skin_animation1_3), ImageTk.PhotoImage(front_skin_animation2_3),
                             ImageTk.PhotoImage(transpose_front_skin_animation1_3),
                             ImageTk.PhotoImage(transpose_front_skin_animation2_3),
                             ImageTk.PhotoImage(back_skin_animation1_3), ImageTk.PhotoImage(back_skin_animation2_3),
                             ImageTk.PhotoImage(transpose_back_skin_animation1_3),
                             ImageTk.PhotoImage(transpose_back_skin_animation2_3),
                             ImageTk.PhotoImage(front_died_skin3), ImageTk.PhotoImage(transpose_front_died_skin3),
                             ImageTk.PhotoImage(back_died_skin3), ImageTk.PhotoImage(transpose_back_died_skin3)],
                   "pers4": [ImageTk.PhotoImage(front_skin4), ImageTk.PhotoImage(back_skin4), 20, 10, 120,
                             ImageTk.PhotoImage(transpose_front_skin4), ImageTk.PhotoImage(transpose_back_skin4),
                             ImageTk.PhotoImage(front_skin_animation1_4), ImageTk.PhotoImage(front_skin_animation2_4),
                             ImageTk.PhotoImage(transpose_front_skin_animation1_4),
                             ImageTk.PhotoImage(transpose_front_skin_animation2_4),
                             ImageTk.PhotoImage(back_skin_animation1_4), ImageTk.PhotoImage(back_skin_animation2_4),
                             ImageTk.PhotoImage(transpose_back_skin_animation1_4),
                             ImageTk.PhotoImage(transpose_back_skin_animation2_4),
                             ImageTk.PhotoImage(front_died_skin4), ImageTk.PhotoImage(transpose_front_died_skin4),
                             ImageTk.PhotoImage(back_died_skin4), ImageTk.PhotoImage(transpose_back_died_skin4)]}
        self.gui = gui
        self.x = x
        self.y = y
        self.tile = tile
        self.power = allPers[name][2]
        self.size = 5
        self.chunk = 0
        self.attackRange = 10
        self.skin = allPers[name][0]
        self.transpose_skin = allPers[name][5]
        self.bot_transpose_skin = allPers[name][6]
        self.now_skin = self.skin

        self.front_skin_animation_left_leg = allPers[name][7]
        self.front_skin_animation_right_leg = allPers[name][8]
        self.transpose_front_skin_animation_left_leg = allPers[name][9]
        self.transpose_front_skin_animation_right_leg = allPers[name][10]

        self.back_skin_animation_left_leg = allPers[name][11]
        self.back_skin_animation_right_leg = allPers[name][12]
        self.transpose_back_skin_animation_left_leg = allPers[name][13]
        self.transpose_back_skin_animation_right_leg = allPers[name][14]

        self.front_died_skin = allPers[name][15]
        self.transpose_front_died_skin = allPers[name][16]
        self.back_died_skin = allPers[name][17]
        self.transpose_back_died_skin = allPers[name][18]

        self.items = []
        self.speed = allPers[name][3]
        self.health = allPers[name][4]
        self.maxHealth = allPers[name][4]
        self.satiety = 100
        self.armor = 0
        self.speed_of_hunger_change = 5
        self.bot_skin = allPers[name][1]
        self.speed_of_hunger_change_timer = 13
        self.isDied = False

    def armor_value(self):
        value = 0
        if self.gui.equipment["shield"] != []:
            value += self.gui.equipment["shield"][4]
        if self.gui.equipment["helmet"] != []:
            value += self.gui.equipment["helmet"][4]
        if self.gui.equipment["mail"] != []:
            value += self.gui.equipment["mail"][4]
        if self.gui.equipment["hands"] != []:
            value += self.gui.equipment["hands"][4]
        if self.gui.equipment["boots"] != []:
            value += self.gui.equipment["boots"][4]
        return value

    def attack(self):
        if not self.gui.equipment["weapon"] == []:
            attack_value = randint(1, self.power)
        else:
            attack_value = randint(1, self.power + self.gui.equipment["weapon"][4])
        return attack_value

    def die(self):
        self.health = 0
        self.satiety = 0
        self.isDied = True
        if self.now_skin == self.skin:
            self.skin = self.front_died_skin
            self.transpose_skin = self.front_died_skin
            self.bot_transpose_skin = self.front_died_skin

            self.front_skin_animation_left_leg = self.front_died_skin
            self.front_skin_animation_right_leg = self.front_died_skin
            self.transpose_front_skin_animation_left_leg = self.front_died_skin
            self.transpose_front_skin_animation_right_leg = self.front_died_skin

            self.back_skin_animation_left_leg = self.front_died_skin
            self.back_skin_animation_right_leg = self.front_died_skin
            self.transpose_back_skin_animation_left_leg = self.front_died_skin
            self.transpose_back_skin_animation_right_leg = self.front_died_skin

            self.bot_skin = self.front_died_skin

        elif self.now_skin == self.transpose_skin:
            self.skin = self.transpose_front_died_skin
            self.transpose_skin = self.transpose_front_died_skin
            self.bot_transpose_skin = self.transpose_front_died_skin

            self.front_skin_animation_left_leg = self.transpose_front_died_skin
            self.front_skin_animation_right_leg = self.transpose_front_died_skin
            self.transpose_front_skin_animation_left_leg = self.transpose_front_died_skin
            self.transpose_front_skin_animation_right_leg = self.transpose_front_died_skin

            self.back_skin_animation_left_leg = self.transpose_front_died_skin
            self.back_skin_animation_right_leg = self.transpose_front_died_skin
            self.transpose_back_skin_animation_left_leg = self.transpose_front_died_skin
            self.transpose_back_skin_animation_right_leg = self.transpose_front_died_skin

            self.bot_skin = self.transpose_front_died_skin

        elif self.now_skin == self.bot_skin:
            self.skin = self.back_died_skin
            self.transpose_skin = self.back_died_skin
            self.bot_transpose_skin = self.back_died_skin

            self.front_skin_animation_left_leg = self.back_died_skin
            self.front_skin_animation_right_leg = self.back_died_skin
            self.transpose_front_skin_animation_left_leg = self.back_died_skin
            self.transpose_front_skin_animation_right_leg = self.back_died_skin

            self.back_skin_animation_left_leg = self.back_died_skin
            self.back_skin_animation_right_leg = self.back_died_skin
            self.transpose_back_skin_animation_left_leg = self.back_died_skin
            self.transpose_back_skin_animation_right_leg = self.back_died_skin

            self.bot_skin = self.back_died_skin

        else:
            self.skin = self.transpose_back_died_skin
            self.transpose_skin = self.transpose_back_died_skin
            self.bot_transpose_skin = self.transpose_back_died_skin

            self.front_skin_animation_left_leg = self.transpose_back_died_skin
            self.front_skin_animation_right_leg = self.transpose_back_died_skin
            self.transpose_front_skin_animation_left_leg = self.transpose_back_died_skin
            self.transpose_front_skin_animation_right_leg = self.transpose_back_died_skin

            self.back_skin_animation_left_leg = self.transpose_back_died_skin
            self.back_skin_animation_right_leg = self.transpose_back_died_skin
            self.transpose_back_skin_animation_left_leg = self.transpose_back_died_skin
            self.transpose_back_skin_animation_right_leg = self.transpose_back_died_skin

            self.bot_skin = self.transpose_back_died_skin

    def take_damage(self, damage):
        if self.armor_value() != 0 and self.health < damage * (275-self.armor_value())/275:
            self.die()
            return
        elif self.armor_value() == 0 and self.health < damage:
            self.die()
            return
        elif self.armor_value() != 0:
            self.health -= damage * (275-self.armor_value())/275
        else:
            self.health -= damage

    def starvation(self):
        if self.satiety < self.speed_of_hunger_change:
            self.die()
            return
        self.satiety -= self.speed_of_hunger_change
        if self.satiety > 70:
            self.speed_of_hunger_change_timer = 13
        elif self.satiety > 40:
            self.speed_of_hunger_change_timer = 26
        elif self.satiety > 10:
            self.speed_of_hunger_change_timer = 39
        else:
            self.speed_of_hunger_change_timer = 52
