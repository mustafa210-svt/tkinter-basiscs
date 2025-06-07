import tkinter
import time
import tkinter.messagebox
#drawing screen 
screen =tkinter.Tk()
#screen size and title
screen.geometry("200x200")
screen.title("Timer")

h1 = tkinter.StringVar()
m1 = tkinter.StringVar()
s1 = tkinter.StringVar()


def t():

    s = int(seconds.get())
    m = int(mins.get())
    h = int(hours.get())

    ts = h * 3600 + m * 60 + s
    while ts > 0:
        ts = ts - 1
        time.sleep(1)
        h = ts//3600
        m = ts%3600//60
        s = ts%3600%60
        h1.set(str(h))
        m1.set(str(m))
        s1.set(str(s))
        screen.update()
        print(ts)

    if ts == 0:
        tkinter.messagebox.showinfo("Notice", "Times up!")
        b1.config(state= "disabled")



h1.set(str(0))
m1.set(str(0))
s1.set(str(0))

#Label
b1 = tkinter.Button(screen, text= "Set time countdown", command= t)

#Entries
seconds = tkinter.Entry(screen, width= 4, textvariable= s1)
mins = tkinter.Entry(screen,width= 4, textvariable= m1)
hours = tkinter.Entry(screen,width= 4, textvariable= h1)

#grid
hours.grid(row= 1, column= 1,padx= 10)
mins.grid(row= 1, column= 2,padx= 10)
seconds.grid(row=1, column= 3,padx= 10)

b1.grid(row= 2, column= 1, columnspan=3, pady= 50 )

screen.mainloop()