import tkinter
import tkinter.messagebox

# Drawing screen
screen = tkinter.Tk()

# Screen geometry
screen.geometry("310x368")
screen.title("X & O - PvP")

def playerbutton(buttonclick):
    global turn, play
    if buttonclick in Bs and buttonclick["text"] == "" and play:
        buttonclick.config(text=turn)
        Bs.remove(buttonclick)
        winnerchecker()
        if play:  # Switch turn only if game not over
            turn = "O" if turn == "X" else "X"

def winnerchecker():
    global play
    for w in win:
        if w[0]["text"] == "X" and w[1]["text"] == "X" and w[2]["text"] == "X" and play:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player 1 (X) has won!")
            play = False
            disablebuttons()
        if w[0]["text"] == "O" and w[1]["text"] == "O" and w[2]["text"] == "O" and play:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player 2 (O) has won!")
            play = False
            disablebuttons()
    if len(Bs) == 0 and play:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        play = False
        disablebuttons()

def disablebuttons():
    for b in B:
        b.config(state="disabled")

# Widgets
b1 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b1), font=("TkDefaultFont", 30))
b2 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b2), font=("TkDefaultFont", 30))
b3 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b3), font=("TkDefaultFont", 30))
b4 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b4), font=("TkDefaultFont", 30))
b5 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b5), font=("TkDefaultFont", 30))
b6 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b6), font=("TkDefaultFont", 30))
b7 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b7), font=("TkDefaultFont", 30))
b8 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b8), font=("TkDefaultFont", 30))
b9 = tkinter.Button(screen, width=4, height=2, command=lambda: playerbutton(b9), font=("TkDefaultFont", 30))

# Grid
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)

b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)

# Lists & variables
Bs = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
win = [[b1, b2, b3], [b4, b5, b6], [b7, b8, b9],
       [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],
       [b1, b5, b9], [b3, b5, b7]]
play = True
turn = "X"  # Player 1 starts
B = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

screen.mainloop()
