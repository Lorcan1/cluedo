from tkinter import *
from PIL import ImageTk,Image
import player
import gameplay,gamesetup,board

height = 700
width = 700
squareSize = height // 25
# root= Tk()

class Gui:
    def __init__(self):
        # # self.root = Tk()
        # self.root.mainloop()
        self.createBoard()
    def createBoard(self):
        board.b.board.pack(anchor = 'nw')
        img = ImageTk.PhotoImage(Image.open("board.jpg"))
        board.b.board.create_image(20,20,anchor=NW,image=img)
   #     (h1,h2,w1,w2) = player.p.placePlayersOnBoard()
        player.p.placePlayersOnBoard()
   #     board.b.board.create_rectangle(w1, h1, w2, h2, fill=p.colour)
        # i want gameplay to happen here 
        gameplay.gp.startPosition(player.p.allPlayersDict)
        gameplay.gp.rollDice(gamesetup.gs.playersDict)
        print(gameplay.gp.board)
        #self.root.mainloop()
        root.mainloop()

    # def placePlayersOnBoard(self):
    #     for p in player.p.allPlayersDict.values():
    #         print(p.x ,p.y)
    #         h1,h2 = 44 + 22.92*(p.x),44 + 22.92*(p.x +1)
    #         w1,w2 = 63 + 22.91*(p.y),63 + 22.91*(p.y +1)
    #         self.board.create_rectangle(w1, h1, w2, h2, fill=p.colour)
        #self.board.create_rectangle(63, 204.44, 613, 227.36, fill='black')
        # self.board.create_rectangle(240, 594.08, 250, 617, fill='black')
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