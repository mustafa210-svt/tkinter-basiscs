import tkinter 
import tkinter.messagebox
import random

#screen
screen = tkinter.Tk() 
screen.geometry ("350x350")
screen.title("Jumbled word game")
#list
words = ["Happy", "Python", "Pause", "Space", "Share", "Artist" , "Plant", "Winter", "Umbrella", "Butterfly"]




#Lables
l1 = tkinter.Label(screen, text= "Jumbled word game" )
l2 = tkinter.Label(screen )
l3 = tkinter.Label(screen, text= "Score :" )

#entry
e1 = tkinter.Entry(screen)

#buttons
b1 = tkinter.Button(screen, text= "Check Answer" )
b2 = tkinter.Button(screen, text= "Reset")

#pack
l1.pack()
l2.pack()

e1.pack()

b1.pack()
b2.pack()

l3.pack()

def jumble():
    word = random.choice(words)
    rc = list(word)
    random.shuffle(rc)
    jumbleword = ''.join(rc)
    l2.config(text= jumbleword)


def check_answer():
    global word
    entry = e1.get()
    if entry == word:
        tkinter.messagebox.showinfo("Correct !", "You guessed the jumbled word correctly !")

    else:
        tkinter.messagebox.showinfo("Incorrect !", "You didnt guess the jumbled word, please try again !")




jumble()

screen.mainloop()