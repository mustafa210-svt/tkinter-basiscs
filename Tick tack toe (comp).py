import tkinter
import random

# Drawing screen
screen = tkinter.Tk()

# Screen geomtry
screen.geometry("345x348")
screen.title("X & O")


def playerbutton(buttonclick):
    if buttonclick in Bs:
        buttonclick.config(text= "X")
        Bs.remove(buttonclick)
        compbutton()

    

def compbutton():
    cb = random.choice(Bs)
    cb.config(text= "O")
    Bs.remove(cb)










# Widgets
b1 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b1))
b2 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b2))
b3 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b3))
b4 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b4))
b5 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b5))
b6 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b6))
b7 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b7))
b8 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b8))
b9 = tkinter.Button(screen, width= 15, height= 7, command= lambda: playerbutton(b9))

# Grid
b1.grid(row= 1, column= 1)
b2.grid(row= 1, column= 2) 
b3.grid(row= 1, column= 3)

b4.grid(row= 2, column= 1)
b5.grid(row= 2, column= 2)
b6.grid(row= 2, column= 3)

b7.grid(row= 3, column= 1)
b8.grid(row= 3, column= 2)
b9.grid(row= 3, column= 3)


#lists
Bs = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
screen.mainloop()