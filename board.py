from tkinter import *
from PIL import ImageTk,Image
height = 700
width = 700
# root= Tk()
class Board:
	def __init__(self):
		self.root = Tk()
		self.board =  Canvas(self.root,width=width,height=height) 

b = Board()