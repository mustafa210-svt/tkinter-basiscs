import tkinter 
import tkinter.messagebox
import random

#screen
screen = tkinter.Tk() 
screen.geometry ("350x350")
screen.title("Jumbled word game")
#list and variables
words = ["happy", "python", "pause", "space", "share", "artist" , "plant", "winter", "umbrella", "butterfly"]
copylist = words.copy()
word = "" 
jumbleword = ""
score = 0




def jumble():
    global word, jumbleword
    
    word = random.choice(words)
    rc = list(word) #rc = random choice
    random.shuffle(rc)
    jumbleword = ''.join(rc)
    l2.config(text= jumbleword)
    words.remove(word)


def check_answer():
    global word, jumbleword, score
    entry = e1.get()
    
  
    if entry == word:
        tkinter.messagebox.showinfo("Correct !", "You guessed the jumbled word correctly !")
        score = score + 1 
        l3.config(text= "Score :" + str(score))

    else:
        tkinter.messagebox.showinfo("Incorrect !", "You didnt guess the jumbled word, please try again !")
     
    if len(words) == 0:
        tkinter.messagebox.showinfo("Thats it !", "Thats all the words for now")
        screen.destroy()

    else:
        jumble()
        e1.delete(0, tkinter.END)
    





  



def reset():
    global score
    score = 0
    l3.config(text= "Score :" + str(score))
    words = copylist.copy()
    
    

#Lables
l1 = tkinter.Label(screen, text= "Jumbled word game" )
l2 = tkinter.Label(screen )
l3 = tkinter.Label(screen, text= "Score : 0" )

#entry
e1 = tkinter.Entry(screen)

#buttons
b1 = tkinter.Button(screen, text= "Check Answer", command= check_answer )
b2 = tkinter.Button(screen, text= "Reset", command= reset)

#pack
l1.pack(pady= 10)
l2.pack(pady= 10)


e1.pack(pady= 10)

b1.pack(pady= 10)
b2.pack(pady= 10)

l3.pack(pady= 10)





jumble()


screen.mainloop()