import tkinter
from tkinter import colorchooser

#drawing screen
screen = tkinter.Tk()

#screen geomtry  and title
screen.geometry("600x500")
screen.title("tk")

# default variables
pen_color = "black"
tool = "pen"
brush_size = 5
last_x, last_y = None, None

#functions
def use_pen():
    global tool
    tool = "pen"

def use_brush():
    global tool
    tool = "brush"

def use_eraser():
    global tool
    tool = "eraser"

def choose_color():
    global pen_color
    color = colorchooser.askcolor()[1]
    if color:
        pen_color = color

def paint(event):
    global last_x, last_y
    x, y = event.x, event.y
    size = brush_size
    color = pen_color

    if tool == "eraser":
        color = "white"

    if last_x and last_y:
        if tool == "brush":
            canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=color)
        else:
            canvas.create_line(last_x, last_y, x, y, fill=color, width=size, capstyle=tkinter.ROUND, smooth=True)

    last_x, last_y = x, y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None

def update_size(event):
    global brush_size
    brush_size = size_slider.get()

#toolbar frame
toolbar = tkinter.Frame(screen)
toolbar.pack(side="top", fill="x")

#widgets
pen_button = tkinter.Button(toolbar, text="pen", command=use_pen)
brush_button = tkinter.Button(toolbar, text="brush", command=use_brush)
color_button = tkinter.Button(toolbar, text="color", command=choose_color)
eraser_button = tkinter.Button(toolbar, text="eraser", command=use_eraser)
size_slider = tkinter.Scale(toolbar, from_=1, to=20, orient="horizontal")
size_slider.set(5)

#pack
pen_button.pack(side="left", padx=5, pady=5)
brush_button.pack(side="left", padx=5, pady=5)
color_button.pack(side="left", padx=5, pady=5)
eraser_button.pack(side="left", padx=5, pady=5)
size_slider.pack(side="left", padx=5, pady=5)

#canvas
canvas = tkinter.Canvas(screen, bg="white")
canvas.pack(fill="both", expand=True)

#bindings
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)
size_slider.bind("<Motion>", update_size)

screen.mainloop()
