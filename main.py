
import random
from tkinter import *


root = Tk()
root.title("Random Genarater")
root.geometry("200x500")



def ranwordgen ():
    # using choice() to generate a random word from a
    # given list.
    ranword = random.choice(['trash bin', 'hamer', 'window', 'mouse', 'brick','bin','happy','boy','super','ugly','man','woman','five','four','three','two'])
    ranwordtext = Label(root, text=ranword,padx=50,pady=50,)
    ranwordtext.grid(row=1, column=0)

#defines button
startbutton = Button(root, text="Genarate Random Word", height = 10, width =30,command=ranwordgen)
startbutton.grid(row=0, column=0)
