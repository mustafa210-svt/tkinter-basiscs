import tkinter
import calendar

#drawing screen
screen = tkinter.Tk()

#screen coords
screen.geometry("400x300")
screen.title("Calendar")


#widgets
label = tkinter.Label(screen, text= "Enter year", bg= "orange", fg= "black")
label2 = tkinter.Label(screen, text= "Calendar", bg= "Grey", fg= "black", font = ("Arial", 60, "bold"))

entry = tkinter.Entry(screen)
def s2():

    screen2 = tkinter.Tk()
    screen.geometry("800x800")
    screen.title("Calendar")
    year = int(entry.get())
    calendartext = calendar.calendar(year)
    t1 = tkinter.Text(screen2, height= 600)
    t1.insert(tkinter.END,calendartext)
    t1.pack()
    screen2.mainloop()

button = tkinter.Button(screen, text= "Show Calendar",bg = "red", command= s2)
button2 = tkinter.Button(screen, text= "Exit",bg = "red")

#pack
label2.pack()
label.pack()
entry.pack()
button.pack()
button2.pack()


screen.mainloop()
