from functools import partial
from tkinter.ttk import *
from gameController import *
from time import *


class Start_window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Game")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        width = width // 2
        height = height // 2
        width = width - 250
        height = height - 250
        self.window.geometry('500x500+{}+{}'.format(width, height))
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, height=500, width=500)
        self.canvas.pack()
        self.visibility_cvar1 = BooleanVar()
        self.visibility_cvar1.set(0)

        img = Image.open('img/start_window_last.png')
        img = ImageTk.PhotoImage(img)
        img2 = Image.open('img/start.png')
        img2 = ImageTk.PhotoImage(img2)

        self.bg = self.canvas.create_image(0, 0, image=img, anchor=NW)
        self.start = self.canvas.create_image(75, 370/2, image=img2, anchor=NW)
        self.motion()
        self.canvas.tag_bind(self.start, '<Button-1>', self.main_window)
        self.window.mainloop()

    def motion(self):
        self.canvas.move(self.start, 0, -1)
        if self.canvas.coords(self.start)[1] > 370/2-30:
            self.window.after(15, self.motion)

    def main_window(self, event):
        if self.bg:
            self.canvas.delete(self.bg)
        if self.start:
            self.canvas.delete(self.start)
        self.menu_icon = Image.open("img/menu_button.png")
        self.menu = self.menu_icon.resize((50, 50), Image.ANTIALIAS)
        self.menu = ImageTk.PhotoImage(self.menu)
        self.menu_canv = self.canvas.create_image(0, 0, image=self.menu, anchor=NW)
        self.canvas.tag_bind(self.menu_canv, '<Button-1>', self.pers_choice)
        self.selected_pers = Image.open("img/Pers1.png")
        self.selected_pers = self.selected_pers.resize((350, 350), Image.ANTIALIAS)
        self.selected_pers = ImageTk.PhotoImage(self.selected_pers)
        self.selected_pers_name = "pers1"
        self.canvas.create_image(250, 150, image=self.selected_pers)
        self.play = Image.open("img/play.png")
        self.play = ImageTk.PhotoImage(self.play)
        self.play_button = self.canvas.create_image(240, 350, image=self.play)
        self.canvas.tag_bind(self.play_button, "<Button-1>", self.start_f)
        self.gears_icon = Image.open("img/shesterna.png")
        self.gears = self.gears_icon.resize((50, 50), Image.ANTIALIAS)
        self.gears = ImageTk.PhotoImage(self.gears)
        self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
        self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)

    def settings(self, event):
        self.canvas.delete(self.gears_button)
        self.gears_button_close = self.canvas.create_image(475, 25, image=self.gears)
        self.settings_frame = Label(self.canvas, width=64)
        self.settings_frame.place(x=0, y=0)
<<<<<<< HEAD
        self.frame = Frame(self.settings_frame, width=450, height=500)
        
        self.frame.grid(column=0, row=0)
=======
        self.frame = Frame(self.settings_frame, width=450, height=500, bg="lightblue")
        self.frame.grid(column=1, row=0)
>>>>>>> 6207c04c1b971997ad33a2daf88a34def0db2c99
        self.checkbutton_visibility = Checkbutton(self.frame, text="visibility", variable=self.visibility_cvar1, onvalue=1, offvalue=0)
        self.checkbutton_visibility.grid(column=1, row=0)
        self.intensivity = Label(self.frame, text="intensivity")
        self.intensivity.grid(column=0, row=1)
        self.intensivity_ent = Entry(self.frame)
        self.intensivity_ent.grid(column=1, row=1)
        self.lifespan = Label(self.frame, text="lifespan")
        self.lifespan.grid(column=0, row=2)
        self.lifespan_ent = Entry(self.frame)
        self.lifespan_ent.grid(column=1, row=2)
        self.loopchance = Label(self.frame, text="loopchance")
        self.loopchance.grid(column=0, row=3)
        self.loopchance_ent = Entry(self.frame)
        self.loopchance_ent.grid(column=1, row=3)
        self.cavechance = Label(self.frame, text="cavechance")
        self.cavechance.grid(column=0, row=4)
        self.cavechance_ent = Entry(self.frame)
        self.cavechance_ent.grid(column=1, row=4)
        self.chunk_size = Label(self.frame, text="chunk_size")
        self.chunk_size.grid(column=0, row=5)
        self.chunk_size_ent = Entry(self.frame)
        self.chunk_size_ent.grid(column=1, row=5)
        self.block_chance = Label(self.frame, text="block_chance")
        self.block_chance.grid(column=0, row=6)
        self.block_chance_ent = Entry(self.frame)
        self.block_chance_ent.grid(column=1, row=6)
        self.double_entrance = Label(self.frame, text="double_entrance")
        self.double_entrance.grid(column=0, row=6)
        self.double_entrance_ent = Entry(self.frame)
        self.double_entrance_ent.grid(column=1, row=6)
        self.button = Button(self.frame, text="Ok")
        self.button.grid(column=1, row=7)
        self.canvas.tag_bind(self.gears_button_close, "<Button-1>", self.close_settings)

    def close_settings(self, event):
        if self.gears_button_close:
            self.canvas.delete(self.gears_button_close)
            self.gears_button = self.canvas.create_image(475, 25, image=self.gears)
            self.canvas.tag_bind(self.gears_button, "<Button-1>", self.settings)
        if self.settings_frame:
            self.settings_frame.destroy()

    def pers_choice(self, event):
        self.canvas.delete(self.menu)
        self.menu_icon = self.menu_icon.rotate(90)
        self.menu_rotated = self.menu_icon.resize((50, 50), Image.ANTIALIAS)
        self.menu_rotated = ImageTk.PhotoImage(self.menu_rotated)
        self.menu = self.canvas.create_image(0, 0, image=self.menu_rotated, anchor=NW)
        self.pers_choice_label = Label(self.canvas, width=64)
        self.pers_choice_label.place(x=50, y=0)
        self.frame_pers1 = Frame(self.pers_choice_label, width=225, height=250)
        self.frame_pers1.grid(column=0, row=0)

        self.frame_pers2 = Frame(self.pers_choice_label, width=225, height=250)
        self.frame_pers2.grid(column=1, row=0)

        self.frame_pers3 = Frame(self.pers_choice_label, width=225, height=250)
        self.frame_pers3.grid(column=0, row=1)

        self.frame_pers4 = Frame(self.pers_choice_label, width=225, height=250)
        self.frame_pers4.grid(column=1, row=1)

        self.pers1_canv = Canvas(self.frame_pers1, width=222, height=247, bg="red")
        self.pers1_canv.pack()

        self.pers2_canv = Canvas(self.frame_pers2, width=222, height=247, bg="blue")
        self.pers2_canv.pack()

        self.pers3_canv = Canvas(self.frame_pers3, width=222, height=247, bg="yellow")
        self.pers3_canv.pack()

        self.pers4_canv = Canvas(self.frame_pers4, width=222, height=247, bg="green")
        self.pers4_canv.pack()
        self.selected_pers = None

        pers1_icon = Image.open("img/Pers1.png")
        self.pers1_canv.icon = pers1_icon
        pers1_icon = pers1_icon.resize((222, 222), Image.ANTIALIAS)
        pers1_icon = ImageTk.PhotoImage(pers1_icon)
        self.pers1 = self.pers1_canv.create_image(0, 15, image=pers1_icon, anchor=NW)
        self.pers1_canv.image = pers1_icon
        self.pers1_canv.bind("<Button-1>", partial(self.click_color_config, self.pers1_canv, "darkred"))
        self.pers1_canv.tag_bind(self.pers1, "<Button-3>", self.properties_pers1)
        self.pers1_canv.name = "pers1"

        pers2_icon = Image.open("img/Pers4.png")
        self.pers2_canv.icon = pers2_icon
        pers2_icon = pers2_icon.resize((222, 222), Image.ANTIALIAS)
        pers2_icon = ImageTk.PhotoImage(pers2_icon)
        self.pers2 = self.pers2_canv.create_image(0, 15, image=pers2_icon, anchor=NW)
        self.pers2_canv.image = pers2_icon
        self.pers2_canv.bind("<Button-1>", partial(self.click_color_config, self.pers2_canv, "lightblue"))
        self.pers2_canv.tag_bind(self.pers2, "<Button-3>", self.properties_pers2)
        self.pers2_canv.name = "pers2"

        pers3_icon = Image.open("img/Pers5.png")
        self.pers3_canv.icon = pers3_icon
        pers3_icon = pers3_icon.resize((222, 222), Image.ANTIALIAS)
        pers3_icon = ImageTk.PhotoImage(pers3_icon)
        self.pers3 = self.pers3_canv.create_image(0, 15, image=pers3_icon, anchor=NW)
        self.pers3_canv.image = pers3_icon
        self.pers3_canv.bind("<Button-1>", partial(self.click_color_config, self.pers3_canv, "orange"))
        self.pers3_canv.tag_bind(self.pers3, "<Button-3>", self.properties_pers3)
        self.pers3_canv.name = "pers3"

        pers4_icon = Image.open("img/Pers8.png")
        self.pers4_canv.icon = pers4_icon
        pers4_icon = pers4_icon.resize((222, 222), Image.ANTIALIAS)
        pers4_icon = ImageTk.PhotoImage(pers4_icon)
        self.pers4 = self.pers4_canv.create_image(0, 15, image=pers4_icon, anchor=NW)
        self.pers4_canv.image = pers4_icon
        self.pers4_canv.bind('<Button-1>', partial(self.click_color_config, self.pers4_canv, "lightgreen"))
        self.canvas.tag_bind(self.menu, '<Button-1>', self.close_choice_pers)
        self.pers4_canv.tag_bind(self.pers4, "<Button-3>", self.properties_pers4)
        self.pers4_canv.name = "pers4"

    def click_color_config(self, widget, color, event):
        self.pers1_canv.config(bg="red")
        self.pers2_canv.config(bg="blue")
        self.pers3_canv.config(bg="yellow")
        self.pers4_canv.config(bg="green")
        widget.config(bg=color)
        self.selected_pers = widget.icon
        self.selected_pers_name = widget.name

    def close_choice_pers(self, event):
        if self.menu:
            self.canvas.delete(self.menu)
        if self.pers_choice_label:
            self.pers_choice_label.destroy()
        self.menu_icon = Image.open("img/menu_button.png")
        self.menu = self.menu_icon.resize((50, 50), Image.ANTIALIAS)
        self.menu = ImageTk.PhotoImage(self.menu)
        self.menu_canv = self.canvas.create_image(0, 0, image=self.menu, anchor=NW)
        self.canvas.tag_bind(self.menu_canv, '<Button-1>', self.pers_choice)
        if not self.selected_pers:
            self.selected_pers = self.pers1_canv.icon
            self.selected_pers_name = self.pers1_canv.name
        self.selected_pers = self.selected_pers.resize((350, 350), Image.ANTIALIAS)
        self.selected_pers = ImageTk.PhotoImage(self.selected_pers)
        self.canvas.create_image(250, 150, image=self.selected_pers)
        self.play = Image.open("img/play.png")
        self.play = ImageTk.PhotoImage(self.play)
        self.play_button = self.canvas.create_image(240, 350, image=self.play)
        self.canvas.tag_bind(self.play_button, "<Button-1>", self.start_f)

    def properties_pers1(self, event):
        self.pers1_canv.delete(self.pers1)
        self.pers1_canv.config(bg="red")
        self.rect1 = self.pers1_canv.create_rectangle(10, 10, 214, 239, fill="yellow")
        self.power1 = self.pers1_canv.create_text(60, 40, text="power:", font="Verdana 14")
        self.power_value1 = self.pers1_canv.create_text(150, 40, text="16", font="Verdana 15 bold")
        self.speed1 = self.pers1_canv.create_text(60, 80, text="speed:", font="Verdana 14")
        self.speed_value1 = self.pers1_canv.create_text(150, 80, text="20", font="Verdana 15 bold")
        self.health1 = self.pers1_canv.create_text(60, 120, text="health", font="Verdana 14")
        self.health_value1 = self.pers1_canv.create_text(150, 120, text="100", font="Verdana 15 bold")
        self.pers1_canv.tag_bind(self.rect1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.power1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.power_value1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.speed1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.speed_value1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.health1, '<Button-3>', self.back_pers1)
        self.pers1_canv.tag_bind(self.health_value1, '<Button-3>', self.back_pers1)

    def properties_pers2(self, event):
        self.pers2_canv.delete(self.pers2)
        self.pers2_canv.config(bg="red")
        self.rect2 = self.pers2_canv.create_rectangle(10, 10, 214, 239, fill="yellow")
        self.power2 = self.pers2_canv.create_text(60, 40, text="power:", font="Verdana 14")
        self.power_value2 = self.pers2_canv.create_text(150, 40, text="20", font="Verdana 15 bold")
        self.speed2 = self.pers2_canv.create_text(60, 80, text="speed:", font="Verdana 14")
        self.speed_value2 = self.pers2_canv.create_text(150, 80, text="20", font="Verdana 15 bold")
        self.health2 = self.pers2_canv.create_text(60, 120, text="health", font="Verdana 14")
        self.health_value2 = self.pers2_canv.create_text(150, 120, text="80", font="Verdana 15 bold")
        self.pers2_canv.tag_bind(self.rect2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.power2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.power_value2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.speed2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.speed_value2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.health2, '<Button-3>', self.back_pers2)
        self.pers2_canv.tag_bind(self.health_value2, '<Button-3>', self.back_pers2)

    def properties_pers3(self, event):
        self.pers3_canv.delete(self.pers3)
        self.pers3_canv.config(bg="red")
        self.rect3 = self.pers3_canv.create_rectangle(10, 10, 214, 239, fill="yellow")
        self.power3 = self.pers3_canv.create_text(60, 40, text="power:", font="Verdana 14")
        self.power_value3 = self.pers3_canv.create_text(150, 40, text="12", font="Verdana 15 bold")
        self.speed3 = self.pers3_canv.create_text(60, 80, text="speed:", font="Verdana 14")
        self.speed_value3 = self.pers3_canv.create_text(150, 80, text="25", font="Verdana 15 bold")
        self.health3 = self.pers3_canv.create_text(60, 120, text="health", font="Verdana 14")
        self.health_value3 = self.pers3_canv.create_text(150, 120, text="110", font="Verdana 15 bold")
        self.pers3_canv.tag_bind(self.rect3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.power3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.power_value3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.speed3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.speed_value3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.health3, '<Button-3>', self.back_pers3)
        self.pers3_canv.tag_bind(self.health_value3, '<Button-3>', self.back_pers3)

    def properties_pers4(self, event):
        self.pers4_canv.delete(self.pers4)
        self.pers4_canv.config(bg="red")
        self.rect4 = self.pers4_canv.create_rectangle(10, 10, 214, 239, fill="yellow")
        self.power4 = self.pers4_canv.create_text(60, 40, text="power:", font="Verdana 14")
        self.power_value4 = self.pers4_canv.create_text(150, 40, text="20", font="Verdana 15 bold")
        self.speed4 = self.pers4_canv.create_text(60, 80, text="speed:", font="Verdana 14")
        self.speed_value4 = self.pers4_canv.create_text(150, 80, text="10", font="Verdana 15 bold")
        self.health4 = self.pers4_canv.create_text(60, 120, text="health", font="Verdana 14")
        self.health_value4 = self.pers4_canv.create_text(150, 120, text="120", font="Verdana 15 bold")
        self.pers4_canv.tag_bind(self.rect4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.power4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.power_value4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.speed4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.speed_value4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.health4, '<Button-3>', self.back_pers4)
        self.pers4_canv.tag_bind(self.health_value4, '<Button-3>', self.back_pers4)

    def back_pers1(self, event):
        self.pers1_canv.delete(self.rect1)
        self.pers1_canv.config(bg="red")
        self.pers1_canv.delete(self.power1)
        self.pers1_canv.delete(self.power_value1)
        self.pers1_canv.delete(self.speed1)
        self.pers1_canv.delete(self.speed_value1)
        self.pers1_canv.delete(self.health1)
        self.pers1_canv.delete(self.health_value1)
        pers1_icon = Image.open("img/Pers1.png")
        self.pers1_canv.icon = pers1_icon
        pers1_icon = pers1_icon.resize((222, 222), Image.ANTIALIAS)
        pers1_icon = ImageTk.PhotoImage(pers1_icon)
        self.pers1 = self.pers1_canv.create_image(0, 15, image=pers1_icon, anchor=NW)
        self.pers1_canv.image = pers1_icon
        self.pers1_canv.bind("<Button-1>", partial(self.click_color_config, self.pers1_canv, "darkred"))
        self.pers1_canv.tag_bind(self.pers1, "<Button-3>", self.properties_pers1)

    def back_pers2(self, event):
        self.pers2_canv.delete(self.rect2)
        self.pers2_canv.config(bg="blue")
        self.pers2_canv.delete(self.power2)
        self.pers2_canv.delete(self.power_value2)
        self.pers2_canv.delete(self.speed2)
        self.pers2_canv.delete(self.speed_value2)
        self.pers2_canv.delete(self.health2)
        self.pers2_canv.delete(self.health_value2)
        pers2_icon = Image.open("img/Pers4.png")
        self.pers2_canv.icon = pers2_icon
        pers2_icon = pers2_icon.resize((222, 222), Image.ANTIALIAS)
        pers2_icon = ImageTk.PhotoImage(pers2_icon)
        self.pers2 = self.pers2_canv.create_image(0, 15, image=pers2_icon, anchor=NW)
        self.pers2_canv.image = pers2_icon
        self.pers2_canv.bind("<Button-1>", partial(self.click_color_config, self.pers2_canv, "lightblue"))
        self.pers2_canv.tag_bind(self.pers2, "<Button-3>", self.properties_pers2)

    def back_pers3(self, event):
        self.pers3_canv.delete(self.rect3)
        self.pers3_canv.config(bg="yellow")
        self.pers3_canv.delete(self.power3)
        self.pers3_canv.delete(self.power_value3)
        self.pers3_canv.delete(self.speed3)
        self.pers3_canv.delete(self.speed_value3)
        self.pers3_canv.delete(self.health3)
        self.pers3_canv.delete(self.health_value3)
        pers3_icon = Image.open("img/Pers5.png")
        self.pers3_canv.icon = pers3_icon
        pers3_icon = pers3_icon.resize((222, 222), Image.ANTIALIAS)
        pers3_icon = ImageTk.PhotoImage(pers3_icon)
        self.pers3 = self.pers3_canv.create_image(0, 15, image=pers3_icon, anchor=NW)
        self.pers3_canv.image = pers3_icon
        self.pers3_canv.bind("<Button-1>", partial(self.click_color_config, self.pers3_canv, "orange"))
        self.pers3_canv.tag_bind(self.pers3, "<Button-3>", self.properties_pers3)

    def back_pers4(self, event):
        self.pers4_canv.delete(self.rect4)
        self.pers4_canv.config(bg="green")
        self.pers4_canv.delete(self.power4)
        self.pers4_canv.delete(self.power_value4)
        self.pers4_canv.delete(self.speed4)
        self.pers4_canv.delete(self.speed_value4)
        self.pers4_canv.delete(self.health4)
        self.pers4_canv.delete(self.health_value4)
        pers4_icon = Image.open("img/Pers8.png")
        self.pers4_canv.icon = pers4_icon
        pers4_icon = pers4_icon.resize((222, 222), Image.ANTIALIAS)
        pers4_icon = ImageTk.PhotoImage(pers4_icon)
        self.pers4 = self.pers4_canv.create_image(0, 15, image=pers4_icon, anchor=NW)
        self.pers4_canv.image = pers4_icon
        self.pers4_canv.bind("<Button-1>", partial(self.click_color_config, self.pers4_canv, "lightgreen"))
        self.pers4_canv.tag_bind(self.pers4, "<Button-3>", self.properties_pers4)

    def start_f(self, event):
        self.window.destroy()
        self.visibility_cvar1 = self.visibility_cvar1.get()
        gui = GUI(self.selected_pers_name, self.visibility_cvar1, int(self.intensivity_ent), int(self.lifespan_ent),
                  int(self.loopchance_ent), int(self.cavechance_ent), int(self.chunk_size_ent), int(self.block_chance_ent),
                  int(self.double_entrance_ent))
Start_window()
