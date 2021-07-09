from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
h = 700
w = 700
# root= Tk()
counter = 20
widgetsList = []
class GuiCanvas:
    def __init__(self):
	    self.root = Tk()
	    self.canvas =  Canvas(self.root,width=w,height=h) 
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

c = GuiCanvas()