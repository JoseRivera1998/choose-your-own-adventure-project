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
    messagebox.showinfo("Title", "Your name is Jose. ""One day you are going on a jog, you jog so far into the deep forest then you got lost and you need to find a way home. You forgot your phone, it is getting late. So you just walk around hoping to find shelter to wait it out until morning.")
    messagebox.showinfo("Start", "You're walking down the road when you stumble upon 8 magical portals one leads to heaven, one to hell, one stay on earth, one to your own fantasy world, one to the sea, one to the desert, one to the world of League of Legends, and last but not least one to GTA V.")                    
    choice = simpledialog.askinteger("Choose which path",
                                     "You have 8 choices, choose 1 if you want to go to heaven to fight god. Choose 2 if you want to go to hell to fight the devil. Choose 3 if you want to stay on Earth.\n"
                                     "Choose 4 if you want to go to a fantasy world. Choose 5 if you want to go to the sea. Choose 6 if you want to go to the desert. Choose 7 if you want to go to Summoner's Rift\n"
                                     " League of Legends World. Choose 8 if you want to go to GTA V world. Enter in 1, 2, 3, 4, 5, 6, 7, or 8.\n\n")
    if choice == 1:
         choice1()
    elif choice == 2:
         choice2()
    elif choice == 3:
         choice3()
    elif choice == 4:
         choice4()
    elif choice == 5:
         choice5()
    elif choice == 6:
         choice6()
    elif choice == 7:
         choice7()
    elif choice == 8:
         choice8()
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

##################### KHAI FUNCTION #########################
def choice5():
    choice = simpledialog.askinteger("Choose carefully",
                                     "You're now transported to an island where you are stranded with some coconut trees and fishing tools. You have 2 choices, either you become a pirate and get rich or you can choose not to become a pirate and live the rest of your life on that island fishing and drinking coconuts. You must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You're King of the Sea!",
                            "You hace chosen to become a pirate, you venture out onto the sea and rob everyone you could find and become the richest pirate around. Live a life full of adventures!")
    elif (choice == 2):
        messagebox.showinfo("Darn. Sucks to be you",
                            "You've decided not to become a pirate and live the rest of your life fishing and drinking coconuts on a lonely island until you die. R.I.P.")
    else:
        choice5()

##################### JOSE FUNCTION #########################
def choice6():
    choice = simpledialog.askineger("Choose carefully",
                                    "You get to decide if you want to go to the desert that leads you to your house or you decide to stay where you are and die.You must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You decide to go to the desert!",
                            "You have chosen to take the path that leads to the desert, once you got through the desrt you were able to get to your house safely!")
    elif(choice == 2):
        messagebox.showinfo("You decide not to go through the desert because you believed you would get no where so you ended up staying and you died")
    else:
        choice6()
##################### KHAI FUNCTION #########################
def choice7():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You have chosen to go to the League of Legends world! Do you want to be a summoner? A summoner is someone who battle other summoners for the pride and glory of winning.\n You can choose to go pro or not. Enter in 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You're the world champion!",
                            " You have chosen to go pro. You now go into the battlefield of league of legends and begin your training to become the best in the world to win 1 million dollars!")
    elif (choice == 2):
        messagebox.showinfo("Loser!",
                            "You have chosen not to go pro and now you spend the rest of your life in this world and play this game until you die of boredom.")
    else:
        choice7()     
##################### JOSE FUNCTION #########################
def choice8():
    choice = simpledialog.askinteger("Choose carefully",
                                    "one of the eight paths leasd to a world called GTA V. You can either choose to go become friends with Franklin or not to be freinds with Franklin. You must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("You decided to become freinds with Franklin!",
                            "once you became friends with Franklin you both decided to go kill everybody and commit crimes in Los Santos and you live happily ever after.")
    elif(choice == 2):
        messagebox.showinfo("You decided to not becamoe friends with Franklin",
                            "once you decided not to become friends with Frankilin you kill him and become the lead protagonist in GTA V.")
    else:
        choice8()
        
###################### MAIN #################################
intro()

root.destroy()
