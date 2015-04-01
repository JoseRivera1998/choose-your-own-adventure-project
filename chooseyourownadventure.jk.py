# Import and value sets
import random
import math
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

root = Tk()
w = Label(root, text="ChooseYour own Adventure")
w.pack()

##############Jose and Khai###############
def intro():
    choice = simpledialog.askinteger("Choose the path",
                                     " Jose has two roads to choose. Jose is walking down a road\n" +
                                     "when Jose came across two paths, one leads to HELL, and the other \nleads to HEAVEN.\n\n" +
                                    "Choose what to do:\n 1: Go to HEAVEN.\n 2: Go to HELL.")
    if (choice == 1):
        HEAVEN()
    elif (choice == 2):
        HELL()
    else:
        intro()
##############JOSE################
                                     
   def HEAVEN():
    choice = simpledialog.askinteger("What to do?",  "You go to HEAVEN to meet god.
                                        You get to meet god.\n" +
                                        "Since you decided to go to HEAVEN.
                                        \nThere you meet god. " +
                                        "God asks if you need anything.\n\You decide to:n 1 : To Fight God.\n 2: Do not fight God.")
       if (choice == 1):
           messagebox.showinfo
                                        
                                        
       
                                     
                                     
