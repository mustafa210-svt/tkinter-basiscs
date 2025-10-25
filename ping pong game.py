import tkinter 
import time

#drawing screen and geomtry
screen = tkinter.Tk()
screen.geometry("800x500")
screen.title("Ping pong")

#canvas
c = tkinter.Canvas(screen, bg = "black")
c.pack(fill="both", expand=True)
c.create_line(400,0,400,500,width= 1,fill = "white")
c.create_oval(350,200,450,300,width= 1,outline= "white")

class Ball():
    def __init__(self,c):
       self.canvas = c 
       self.ball = c.create_oval(380,230,400,250, width= 1, fill= "yellow")
       self.change_x = 5
       self.change_y =  -5

    def hit_paddle(self,paddle1,paddle2):
        p1 = self.canvas.coords(paddle1.paddles)
        p2 = self.canvas.coords(paddle2.paddles)
        ba = self.canvas.coords(b_object)

        if p1[1] < ba[3] and p1[3] > ba[1]:
            if p1[2] > ba[0] and p1[0] < ba[0]:
                self.change_x = 5
        
        

        if p2[1] < ba[3] and p1[3] > ba[1]:
            if p2[2] > ba[2] and p2[0] < ba[2]:
                self.change_x = -5

        
                   

    def move_ball(self):
        self.canvas.move(self.ball, self.change_x, self.change_y)
        self.position = self.canvas.coords(self.ball)

        if self.position[2] >= 800 :
            self.change_x = -5

        if self.position[0] <= 0:
            self.change_x =  5

        if self.position[1]  <= 0:
            self.change_y = 5 


        if self.position[3] >= 500:
            self.change_y = -5

   
        

#object for ball
b_object = Ball(c =c)


class  Paddle():
    def __init__(self,x1,y1,x2,y2,c1):
        self.canvas = c1
        self.paddles = self.canvas.create_rectangle(x1,y1,x2,y2,fill= "Red")
        self.change_y = 0
    



    def move_padddle(self):
        self.canvas.move(self.paddles,0,self.change_y)
        self.position = self.canvas.coords(self.paddles)
        self.change_y = 0



    def paddle_up(self,event):
        self.change_y  = -7
        


    def paddle_down(self,event):
        self.change_y = 7
    
#objects for paddle
p1_object = Paddle(x1= 20, y1 = 200,x2= 30, y2= 310, c1 = c)
p2_object = Paddle(x1 = 750, y1= 200, x2= 740, y2= 310, c1 =c )

#moving left paddle
c.bind_all("<w>", p1_object.paddle_up)
c.bind_all("<s>", p1_object.paddle_down)

#moving right paddle
c.bind_all("<KeyPress-Up>", p2_object.paddle_up)
c.bind_all("<KeyPress-Down>", p2_object.paddle_down)
x = 0


def w():
    p1_object.move_padddle()
    p2_object.move_padddle()
    b_object.move_ball()
    screen.update_idletasks()
    screen.update()
    screen.after(10,w)

    

w()


screen.mainloop()






