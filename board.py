from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
height = 700
width = 700
# root= Tk()
counter = 20
widgetsList = []
class Canvas:
    def __init__(self):
	    self.root = Tk()
	    self.board =  Canvas(self.root,width=width,height=height) 
	    self.widget = None

    def createWelcomeMessage(self):
        welcomeMessage = Label(self.root, text='Welcome!')
        welcomeMessage.place(x=660, y=20)
        widgetsList.append(welcomeMessage)

    def updateWidget(self,text):
        global counter,widgetsList
        if counter > 620:
        	self.clearWidgets(widgetsList)
        counter = counter +20
        label = Label(self.root, text=text)
        label.place(x=660, y=counter)
        widgetsList.append(label)


    def clearWidgets(self,widgetsList):
        for widget in widgetsList:
            widget.destroy()
        global counter
        counter = 0






b = Board()