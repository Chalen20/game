from tkinter import *
class MiniMap:
    def __init__(self,gui):
        self.gui = gui
    def toggle(self):
        print(111)
        self.frame = Frame(self.gui.root, width=270, height=270, bg="green")
        self.frame.place(x=0, y=0)
        self.canvas = Canvas(self.frame, width=180, height=180, bg="#ccccaa")
        self.canvas.configure(scrollregion=(0, 0, 100000, 100000))
        self.canvas.pack()
        self.canvas.scan_mark(0, 0)
        self.canvas.scan_dragto(-15, -15, gain=1)
        #self.canvas.place(x=0, y=0)
        #print(111)
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

        def scroll_start(self, event):
            print(event.x,event.y)
            self.canvas.scan_mark(event.x, event.y)

        def scroll_move(self, event):
            self.canvas.scan_dragto(event.x, event.y)
        
        
