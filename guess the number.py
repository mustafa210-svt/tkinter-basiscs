import tkinter
import random 
import tkinter.messagebox

#drawing screen
screen = tkinter.Tk()
#geomtry and title
screen.geometry("400x300")
screen.title("Guess the number game")

def namebutton():
    name = e1.get()
    tkinter.messagebox.showinfo("guess a number", "Hi, "+ name + " Guess a number from 1 to 15")

g = random.randint(1,15)
def guess():
    global g
    number = int(e2.get())
    if number == g:
        tkinter.messagebox.showinfo("Result", "You guessed right!, it was " + str(g))
    if number < g:
        tkinter.messagebox.showinfo("Result", "your number is smaller than mine, try again")
    if number > g:
        tkinter.messagebox.showinfo("Result", "your number is higher than mine, try again")












#widgets

l1 = tkinter.Label(screen, text = "welcome to our game!",padx= 100, pady= 20 )
l2 = tkinter.Label(screen, text = "what's your name?",pady =10)
l3 = tkinter.Label(screen, text = "Take a guess:", pady=10)

b1 = tkinter.Button(screen, text = "Ok",command= namebutton)
b2 = tkinter.Button(screen, text = "Confirm", command= guess)

e1 = tkinter.Entry(screen)
e2 = tkinter.Entry(screen)

#grid

l1.grid(column=1, row= 1, columnspan= 2 )
l2.grid(column=1, row= 2)
l3.grid(column=1, row= 4)

b1.grid(column= 2, row= 3)
b2.grid(column= 2, row= 5)

e1.grid(column =1, row= 3)
e2.grid(column= 1, row= 5)


screen.mainloop()