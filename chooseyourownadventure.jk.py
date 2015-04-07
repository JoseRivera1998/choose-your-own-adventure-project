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
def choice2():
    choice = simpledialog.askinteger("Choose carefully",
                                     "You get to decide if you want to fight the Devil. Now you must choose 1 or 2 again, 1 is to fight the Devil and 2 is to not fight the Devil. Enter in 1 or 2.")
    if (choice == 1):
        messagebox.showinfo("You win!",
                            "You become leader of all Hell!    THE END")
    elif (choice == 2):
        messagebox.showinfo("You have decided not to fight Devil!",
                            "You have chosen not to fight Devil, you become his BFF for eternity and plan to someday team up with him to fight God.   THE END")
    else:
        choice2()


###################### MAIN #################################
intro()

root.destroy()
