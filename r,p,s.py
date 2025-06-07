import tkinter
import random 
#drawing screen
screen = tkinter.Tk()

#coords and title
screen.geometry("500x400")
screen.title("Rock, paper, scissors")



#widgets
b1 = tkinter.Button(screen, text = "Rock", command= lambda: plc("rock"))
b2 = tkinter.Button(screen, text = "Paper",command= lambda: plc("paper"))
b3 = tkinter.Button(screen, text = "Scissors",command= lambda: plc("scissors"))

l1 = tkinter.Label(screen, text = "Rock Paper Scissors")
l2 = tkinter.Label(screen, text = "")
l3 = tkinter.Label(screen, text = "Your options =")
l4 = tkinter.Label(screen, text = "Score =" )
l5 = tkinter.Label(screen, text = "You selected =")
l6 = tkinter.Label(screen, text = "Computer selected: =")
l7 = tkinter.Label(screen,text = "Player Score:")
l8 = tkinter.Label(screen, text = "Computer score:")

#variables and lists
options = ["rock", "paper", "scissors"]
pscore = 0
cscore = 0

def plc(player_choice):
    computer = random.choice(options)
    global pscore, cscore
    if computer == player_choice:
        l2.config(text= "Draw")
        l2.config(fg = "orange")
        l6.config(text= "Computer selected:" + computer)
        l5.config(text= "Player selected:" + player_choice)
    if computer == "rock" and player_choice == "scissors" or computer == "paper" and player_choice == "rock" or computer == "scissors" and player_choice == "paper":
        l2.config(text= "Computer won!")
        l2.config(fg = "red")
        l6.config(text= "Computer selected:" + computer)
        l5.config(text= "Player selected:" + player_choice)
        cscore = cscore + 1
        l8.config(text= "Computer score =" + str(cscore))

    if player_choice == "rock" and computer == "scissors" or player_choice == "paper" and computer == "rock" or player_choice == "scissors" and computer == "paper":
         l2.config(text= "Player won!")
         l2.config(fg = "green")
         l6.config(text= "Computer selected" + computer)
         l5.config(text= "Player selected:" + player_choice)
         pscore = pscore + 1 
         l7.config(text= "Player score =" + str(pscore))


#grid
b1.grid(row =4, column=2)
b2.grid(row =4, column=3)
b3.grid(row =4, column=4)

l1.grid(row= 1, column=1, columnspan=4)
l2.grid(row= 2, column=1, columnspan=4)
l3.grid(row= 3, column=1)
l4.grid(row= 5, column=1)
l5.grid(row= 6, column=2)
l6.grid(row= 7, column=2)
l7.grid(row= 6, column=3)
l8.grid(row= 7, column=3)


screen.mainloop()