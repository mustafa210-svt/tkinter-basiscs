import tkinter 

#drawing screen and geomtry
screen = tkinter.Tk()
screen.geometry("800x500")
screen.title("Ping pong")

#canvas
c = tkinter.Canvas(screen, bg = "black")
c.pack(fill="both", expand=True)
c.create_line(400,0,400,500,width= 1,fill = "white")
c.create_oval(350,200,450,300,width= 1,outline= "white")

class Ball:
    def __init__(self):
        
       self.ball = c.create_oval(380,230,400,250, width= 1, fill= "yellow")
       self.change_x = 5
       self.change_y =  -5

    def drop():
        pass


b_object = Ball()

class  Paddle:
    def __init__(self,x1,y1,x2,y2):
        self.paddles = c.create_rectangle(x1,y1,x2,y2,fill= "Red")
        self.change_y = 0


p1_object = Paddle(x1= 20, y1 = 200,x2= 30, y2= 310)
p2_object = Paddle(x1 = 750, y1= 200, x2= 740, y2= 310)
        








screen.mainloop()

