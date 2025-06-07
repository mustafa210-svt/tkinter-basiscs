import tkinter 

#screen
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Address book")


#widgets 
#entries
e1 = tkinter.Entry(screen)
e2 = tkinter.Entry(screen)
e3 = tkinter.Entry(screen)
e4 = tkinter.Entry(screen)
e5 = tkinter.Entry(screen)


#lists
title = tkinter.Label(screen, text= "Address book")
name= tkinter.Label(screen, text= "Name")
numb = tkinter.Label(screen, text= "Contact number")
adr = tkinter.Label(screen, text= "Address")
email = tkinter.Label(screen, text= "Email")
dob = tkinter.Label(screen, text= "Date of birth")

#buttons
open = tkinter.Button(screen, text= "Open", width= 10)
edit = tkinter.Button(screen, text= "Edit", width = 10)
delete = tkinter.Button(screen, text= "Delete", width= 10)
save = tkinter.Button(screen, text= "Save", width= 30)
add = tkinter.Button(screen, text= "Update/Add", width= 10)

#list box
lb = tkinter.Listbox(screen, width=40, height= 20)


#grid
#title and listbox
title.grid(column= 1, row= 1, columnspan= 2)
lb.grid(column=1 , row= 2, rowspan= 5, columnspan= 2)

#lists
name.grid(column= 3, row=2)
adr.grid(column=3, row=3)
numb.grid(column= 3,row= 4)
email.grid(column= 3, row=5)
dob.grid(column= 3, row= 6)

#entries
e1.grid(column= 4, row= 2)
e2.grid(column= 4, row= 3)
e3.grid(column= 4,row=4)
e4.grid(column= 4, row= 5)
e5.grid(column= 4, row= 6)

#buttons
open.grid(column= 3, row= 1)
edit.grid(column=1 ,row=7)
delete.grid(column= 2, row= 7)
add.grid(column= 4, row= 7)
save.grid(column= 1,row= 8, columnspan= 4)



screen.mainloop()