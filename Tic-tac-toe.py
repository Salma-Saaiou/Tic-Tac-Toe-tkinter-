from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('tic-tac-toe')

root.iconbitmap('tic tac toe.ico')

root.resizable(False,False)

# X starts so true
clicked = True
count = 0



# disable all the buttons:
def disabled_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# checking the winner

def checkifwon():
    global winner
    # if there is already been a winner, winner will be changed to true and then the game will stop
    winner = False


    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
          b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
          b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
          b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or
          b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
          b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
          b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
          b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        winner = True
        messagebox.showinfo("WINNER X", "YOU JUST WON!!!!")
        disabled_buttons()



    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
          b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
          b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
          b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" or
          b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
          b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
          b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
          b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        winner = True
        messagebox.showinfo("WINNER O", "YOU JUST WON!!!!!")
        disabled_buttons()


# tie

    elif count == 9 and winner == False:
        messagebox.showinfo('Ops!!!','IT IS A TIE.')



# Button clicked function

def b_click(b):
    global clicked, count

    if b['text'] == ' ' and clicked is True:
        b['text'] = "X"
        clicked = False
        count += 1
        checkifwon()



    elif b['text'] == ' ' and clicked is False:
        b['text'] = "O"
        clicked = True
        count += 1
        checkifwon()




# Start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked , count
    clicked = True
    count = 0

    # building buttons

    b1 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b1))
    b2 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b2))
    b3 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b3))

    b4 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b4))
    b5 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b5))
    b6 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b6))

    b7 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b7))
    b8 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b8))
    b9 = Button(root, text=' ', font=('Arial', 25), height=3, width=6, bg='#efefef', command=lambda: b_click(b9))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)



# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)


# Create options menu
options_menu = Menu(my_menu, tearoff = False)

my_menu.add_cascade(label= 'Options', menu=options_menu)
options_menu.add_command(label='Reset game', command= reset)


reset()


root.mainloop()