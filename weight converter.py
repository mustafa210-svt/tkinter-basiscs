import tkinter 

#drawing screen
screen = tkinter.Tk()

#screen size and title
screen.geometry("400x100")
screen.title("Weight converter")

def calculate():
    kg = int(entry.get())
    gr = kg * 1000
    po = kg * 2.20462
    ou = kg * 35.274
    grams.config(text = gr)
    pounds.config(text = po)
    ounce.config(text = ou)



#widgets 
convert = tkinter.Button(screen, text = "Convert", command= calculate )

entry = tkinter.Entry(screen)

l1 = tkinter.Label(screen, text = "Enter the weight in kg")
l2 = tkinter.Label(screen, text = "gram")
l3 = tkinter.Label(screen, text = "pounds")
l4 = tkinter.Label(screen, text = "ounce")

grams = tkinter.Label(screen, width= 20)
pounds = tkinter.Label(screen, width= 20)
ounce =  tkinter.Label(screen, width= 20)
 

#grid
l1.grid(row= 1, column= 1)
l2.grid(row= 2, column= 1)
grams.grid(row= 3, column= 1)

entry.grid(row= 1, column= 2)
l3.grid(row= 2, column= 2)
pounds.grid(row= 3, column= 2 )

convert.grid(row= 1, column= 3)
l4.grid(row= 2, column= 3)
ounce.grid(row= 3,column= 3)
screen.mainloop()