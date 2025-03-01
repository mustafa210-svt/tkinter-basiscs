import tkinter

#drawing screen
screen = tkinter.Tk()

#screen coords
screen.geometry("800x800")
screen.title("tkinter basics")

#widgets
#1. Label
label = tkinter.Label(screen, text= "Tkinter label", bg= "orange", fg= "black", width = 12, height= 2, )

#2. entry 
entry = tkinter.Entry(screen)

#3. button
def b():

    screen2=tkinter.Tk()

    screen2.geometry("400x400")
    screen2.title("Second screen")
    button = tkinter.Button(screen2, text= "secret button",bg = "red", width = 8, height= 2)
    button.grid(row=2, column= 1)
    screen2.mainloop()
    


button = tkinter.Button(screen, text= "next page",bg = "red", width = 8, height= 2, command= b )

#4. text
text = tkinter.Text(screen, bg= "yellow", width= 20, height= 10)

#geometry managers:
#1. pack function
#label.pack()
#entry.pack()
#button.pack()

#2. grid
label.grid(row= 400, column= 5)
entry.grid(row= 300, column= 3)
button.grid(row=200, column= 1)
text.grid(row= 100, column= 4)

#3. place
#label.place(x= 400,y= 300)
#entry.place(x= 200, y= 150)
#button.place(x= 10,y= 600)


screen.mainloop()