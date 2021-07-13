from tkinter import *
from PIL import ImageTk,Image
import player
import gameplay,gamesetup,canvas
import time

height = 700
width = 700
squareSize = height // 25
boardImg = ImageTk.PhotoImage(Image.open("board.jpg"))

class Gui:
    def __init__(self):
        self.createBoard()
    def createBoard(self):
        canvas.c.canvas.pack(anchor = 'nw')
        logoImg = Image.open("cluedo.png")
        resize_image = logoImg.resize((500,500))
        logoImg = ImageTk.PhotoImage(resize_image)  
        canvas.c.canvas.create_image(width/2, height/2, image=logoImg) 
        canvas.c.root.after(2000, self.changeImg)
        #self.createWidget()
        canvas.c.root.after(2000, canvas.c.createWelcomeMessage)
        gameplay.gp.startPosition(player.p.allPlayersDict)
       # gameplay.gp.centreWeaponInRoom()
        gameplay.gp.rollDice(gamesetup.gs.playersDict)
        print(gameplay.gp.board)
        canvas.c.root.mainloop()


    def changeImg(self):
        canvas.c.canvas.delete("all")
        canvas.c.canvas.create_image(20,20, anchor=NW, image=boardImg)
        player.p.placePlayersOnBoard()

    # def createWidget(self):
    # 	Label(canvas.c.root, text="Hello WORLD").place(x=660, y=20)

gui = Gui()
# gui.createBoard()

#need to display counters on the board
#get the location of every player
#manually input start squares - similar to player location
#for player starting in top right, measure margin in from top and side,
#then add 0 squares and square
#GET LENGTH OF YELLOW AND DIVIDE BY NUMBER OF SQUARES

#Measuremets
#25 squares width
#top margin = 44
#bottom margin = 250
#height of token = (617 - 44)/25 = 22.92
#width of token = (613 - 63)/24 = 22.91