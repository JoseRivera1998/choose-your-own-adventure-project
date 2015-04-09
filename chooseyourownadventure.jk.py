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
    messagebox.showinfo("Start", "You're walking down the road when you stumble upon 4 paths, one leads to heaven, one to hell, one stay on earth, the other one is a fantasy world.")                    
    choice = simpledialog.askinteger("Choose which path",
                                     "You have 4 choices, choose 1 if you want to go to heaven to fight god. Choose 2 if you want to go to hell to fight the devil. Choose 3 if you want to stay on Earth. Choose 4 if you want to go to a fantasy world. Enter in 1, 2, 3 or 4.")
    if choice == 1:
         choice1()
    elif choice == 2:
         choice2()
    elif choice == 3:
         choice3()
    elif choice == 4:
         choice4()
    else:
         intro()


###################### JOSE FUNCTION ########################
def choice1():
    choice =  simpledialog.askinteger("Choose carefully",
                                      "You get to decide if you wnat to fight God or not. You must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You win!",
                            "You beat God and became the leader of all Heaven.")
    elif (choice == 2):
        messagebox.showinfo("You decided not to fight God!!",
                              "Now that you have decided not to fight with God you became BFF's and God made you into an Angel.")
    else:
      choice1()                                
                                
###################### KHAI FUNCTION ########################
def choice2():
    choice = simpledialog.askinteger("Choose carefully",
                                     "You get to decide if you want to fight the Devil. Now you must choose 1 or 2 again. Enter in 1 or 2.")
    if (choice == 1):
        messagebox.showinfo("You win!",
                            "You become leader of all Hell!")
    elif (choice == 2):
        messagebox.showinfo("You have decided not to fight Devil!",
                            "You have chosen not to fight Devil, you become his BFF for eternity and plan to someday team up with him to fight God.")
    else:
        choice2()

###################### KHAI FUNCTION ########################
def choice3():
    choice = simpledialog.askinteger("Choose carefully",
                                     "You get to decide if you want to create an army or not. You must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You win!",
                            "You have chosen to create an army, your army win every single battle and now you rule the world!")
    elif (choice == 2):
        messagebox.showinfo("You live a normal life.",
                            "You have chosen not to create an army, there is now world peace and you live happily ever after.")
    else:
        choice3()

##################### JOSE FUNCTION #########################
def choice4():
    choice = simpledialog.askinteger("Choose carefully",
                                     "You get to decide if you want to be the leader of the fantasy world or not. You must choose 1 or 2 once again.")
    if (choice == 1):
        messagebox.showinfo("Do whatever you want!",
                            "You have chosen to be the leader of the fantasy world, now you can fight both God and the Devil to become the ultimate ruler of everything!")
    elif (choice == 2):
        messagebox.showinfo("Now you enjoy the rest of your life",
                            "You decide to not to become the leader of the fantasy world, but you decide to stay in the fantsy world either way and you live happily ever after in your fantasy house or do whatever you want in your fantsy world.")

    else:
        choice4()

        
###################### MAIN #################################
intro()

root.destroy()
