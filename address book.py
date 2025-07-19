import tkinter
import tkinter.filedialog
import tkinter.messagebox 

#screen
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Address book")

add_book = {}

#functions

def add_button():
    name = e1.get()
    adr = e2.get()
    numb = e3.get()
    email = e4.get()
    dob = e5.get()

    add_book[name] = [adr,numb,email,dob]
    update()
    e1.delete(0,tkinter.END)
    e2.delete(0,tkinter.END)
    e3.delete(0,tkinter.END)
    e4.delete(0,tkinter.END)
    e5.delete(0,tkinter.END)



def update():
    lb.delete(0,tkinter.END)

    for key in add_book.keys():
        lb.insert(tkinter.END, key)
        


def delete_button():
    global add_book
    index = lb.curselection()
    name = lb.get(index)
    del add_book[name]
    update()
    
def edit_button():
    global add_book
    index = lb.curselection()
    name = lb.get(index)
    values = add_book[name]
    e1.insert(tkinter.END, name)
    e2.insert(tkinter.END, values[0])
    e3.insert(tkinter.END, values[1])
    e4.insert(tkinter.END, values[2])
    e5.insert(tkinter.END, values[3])

def save_button():
    taskfile = tkinter.filedialog.asksaveasfile()
    if taskfile is not None:
        print(add_book,file= taskfile)

def open_button():
    global add_book
    taskfile = tkinter.filedialog.askopenfile()
    lb.delete(0,tkinter.END)
    if taskfile is not None:
        data = taskfile.read()
        add_book = eval(data)
        update()

def viewinfo(event):
    index = lb.curselection() 
    name =lb.get(index)
    records = add_book.get(name)
    tkinter.messagebox.showinfo(name, "address ="+ records[0] + "\n Contact number=" + records[1] +"\n Email=" + records[2] + "\n Dob=" + records[3])
    















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
open = tkinter.Button(screen, text= "Open", width= 10, command= open_button)
edit = tkinter.Button(screen, text= "Edit", width = 10, command= edit_button)
delete = tkinter.Button(screen, text= "Delete", width= 10, command= delete_button)
save = tkinter.Button(screen, text= "Save", width= 30, command= save_button)
add = tkinter.Button(screen, text= "Update/Add", width= 10, command= add_button)

#list box
lb = tkinter.Listbox(screen, width=40, height= 20)
lb.bind("<<ListboxSelect>>", viewinfo)


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