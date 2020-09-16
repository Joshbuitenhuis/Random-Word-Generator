
import random

from tkinter import *

root = Tk()
root.title("Random Genarater")




def ranwordgen ():
    # using choice() to generate a random word from a
    # given list.
    ranword = random.choice(["trash bin", "hamer", "window", "mouse", "brick"])
    print(random.choice(["trash bin", "hamer", "window", "mouse", "brick"]))
    ranwordtext = Label(root, text=ranword)
    ranwordtext.grid(row=1, column=0)

#defines button
startbutton = Button(root, text="Genarate Random Word", height = 10, width =30,command=ranwordgen)
startbutton.grid(row=0, column=0)
