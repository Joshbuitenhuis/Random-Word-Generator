#import's random for random values and tkinter for gui
import random
from tkinter import *
#sets up gui window
root = Tk()
root.title("Random Word Generator")
root.geometry("200x500")

#sets a = 1 so console can loop
a = 1
def consoleran():   
    while a == 1:
        print("A random word is : ", end="")
        #choose random word to print
        print (random.choice(ranword))
        print("Click Enter To Print Another Random Word")
        # wait's for user input until it choose anther word
        input()
def guiapp ():

    #defines gui elements
    ranwordtext = Label(root, teext=random.choice(ranword),padx=50,pady=50,)
    startbutton = Button(root, txt="Generate Random Word", height = 10, width =30,command=ranwordgen)
    #renders gui elements
    startbutton.grid(row=0, column=0)
    ranwordtext.grid(row=1, column=0)
   
#defines word list
ranword = ['trash bin', 'hamer', 'window', 'mouse', 'brick','bin','happy','boy','super','ugly','man','woman','five','four','three','two','one','six','why','how','boo','goo','fun','glue','pen','key','beg','I','mabey','so','no','yes','woo','yay','ok','go','nevermind','well','that','odd','you','google','state','mate','great','oh','bad','good','mad','sad']

#ask's user if they want to use console mode or gui mode
print("Type Console to use the console interface and type gui to use the gui interface")
#compares user input to see if it matches gui or Console
b = input()
if b == "Console":
    
    consoleran()
if b == "gui":
    print("launching gui now")
    guiapp()

    







