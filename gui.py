from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

class Gui:
    def createBoard(self):
        root = Tk()
        board = Canvas(root,width=700,height=700)
        board.pack()
        img = ImageTk.PhotoImage(Image.open("board.jpg"))
        board.create_image(20,20,anchor=NW,image=img)
        root.mainloop()


gui = Gui()
gui.createBoard()



