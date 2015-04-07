# choose.py
# by Jose and Khai
# Description: starter code for your
# own adventure project

#import statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "Your name is Jose. ""One day you are going on a jog, but then you got lost and you need to find a way home. You forgot your phone and you're too dumb to call for help. So you just walk around. ")
    messagebox.showinfo("Start", "You're walking down the road when you stumble upon 2 paths, one leads to heaven and the other leads to hell.")                    
    choice = simpledialog.askinteger("Choose which path",
                                     "You have 2 choices, choose 1 if you want to go to heaven to fight god. Choose 2 if you want to go to hell to fight the devil. Enter in 1 or 2.")
    if choice == 1:
         choice1()
    elif choice == 2:
         choice2()
    else:
         intro()


###################### JOSE FUNCTION ########################


###################### KHAI FUNCTION ########################



###################### MAIN #################################
intro()

root.destroy()
