import tkinter
import tkinter.filedialog
#drawing screen
screen = tkinter.Tk()

#screen gem.
screen.geometry("400x500")
screen.title("Memoriser")


#variables

def o():
    taskfile = tkinter.filedialog.askopenfile()
    if taskfile is not None:
        Lb1.delete(0, tkinter.END)
        store = taskfile.readlines()
        for item in store:
            Lb1.insert(tkinter.END, item)
def d():
    index = Lb1.curselection()
    Lb1.delete(index)
   

def s():
    taskfile = tkinter.filedialog.asksaveasfile()
    if taskfile is not None:
        store = Lb1.get(0,tkinter.END)
        for item in store:
            print(item.strip(),file = taskfile)
            
        Lb1.delete(0,tkinter.END)
    

def a():
    item = e1.get()
    Lb1.insert(tkinter.END, item)
    e1.delete(0,tkinter.END)





#widgets

open = tkinter.Button(screen, text= "Open", width= 16, command= o)
delete = tkinter.Button(screen,text= "Delete",width= 16,command= d )
save = tkinter.Button(screen, text= "Save", width= 16, command = s)
Add = tkinter.Button(screen,text= "Add", width= 16, command= a)

e1 = tkinter.Entry(screen, width= 30)

Lb1 = tkinter.Listbox(screen, width= 60,height= 15 )

#grid
open.grid(column= 1, row= 1)
delete.grid(column= 2, row= 1)
save.grid(column= 3, row= 1)
Add.grid(column= 3, row= 2)
e1.grid(column= 1, row= 2, columnspan=2)
Lb1.grid(column= 1,row= 3,columnspan=3)

screen.mainloop()