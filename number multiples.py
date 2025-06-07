import tkinter 
import tkinter.ttk

#drawing screen
screen = tkinter.Tk()

#screen geometry & title 
screen.geometry("400x600")
screen.title("number multiples")


#variables/lists
numbers = []


def calculation():
    num = int(cb.get())
    ran = int(o.get())
    i = 1
    result = str()
    while i <= ran:
        m = num * i
        result = result + str(num) + " * " + str(i) + " = " + str(m) + "\n"
        i = i + 1
        l3.config(text = result )




for i in range(1, 51, 1):
    numbers.append(i)










#widgets

cb = tkinter.ttk.Combobox(screen)
cb["values"] = numbers

o = tkinter.IntVar()
rb1 = tkinter.Radiobutton(screen, text= 10, variable= o, value= 10)
rb2 = tkinter.Radiobutton(screen,text= 20, variable= o, value= 20)
rb3 = tkinter.Radiobutton(screen, text= 30, variable= o, value= 30)

l1 = tkinter.Label(screen, text= "Multiplication table")
l2 = tkinter.Label(screen, text= "Number and Range")
l3 = tkinter.Label(screen)

b1 = tkinter.Button(screen, text= "Generate table", command= calculation)

#grid

l1.grid(column= 2, row= 1)
l2.grid(column= 1, row= 2)
l3.grid(column= 2, row= 6)

cb.grid(column= 2, row= 2)

rb1.grid(column= 3, row= 2)
rb2.grid(column= 3, row= 3)
rb3.grid(column= 3, row= 4)

b1.grid(column= 2, row= 5)

screen.mainloop()