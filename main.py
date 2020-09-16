
import random

from tkinter import *

root = Tk()
root.title("Random Genarater")

def ranword ():
    # using choice() to generate a random word from a
    # given list.
    print(random.choice(["trash bin", "hamer", "window", "mouse", "brick"]))
    ranwordtext = Label(root, text=random.choice(["trash bin", "hamer", "window", "mouse", "brick"]))
    ranwordtext.grid(row=1, column=0)
#defines button
startbutton = Button(root, text="Genarate Random Word", height = 10, width =30,command=ranword)
startbutton.grid(row=0, column=0)
