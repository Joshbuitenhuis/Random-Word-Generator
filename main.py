
import random
from tkinter import *
root = Tk()
root.title("Random Genarater")
root.geometry("200x500")


a = 1
def consoleran():   
    while a == 1:
        print("A random word is : ", end="")
        print (random.choice(ranword))
        print("Click Enter To Print Another Random Word")
        input()
def ranwordgen ():
    # using choice() to generate a random word from a
    # given list.
    
    ranwordtext = Label(root, text=random.choice(ranword),padx=50,pady=50,)
    startbutton = Button(root, text="Genarate Random Word", height = 10, width =30,command=ranwordgen)
    startbutton.grid(row=0, column=0)
    ranwordtext.grid(row=1, column=0)
   

ranword = ['trash bin', 'hamer', 'window', 'mouse', 'brick','bin','happy','boy','super','ugly','man','woman','five','four','three','two','one','six','why','how','boo','goo','fun','glue','pen','key','beg','I','mabey','so','no','yes','woo','yay','ok','go','nevermind','well','that','odd']
print("Type Console to use the consolo interface and type gui to use the gui interface")
b = input()
if b == "Console":
    
    consoleran()
if b == "gui":
    print("launching gui now")
    ranwordgen()

    







