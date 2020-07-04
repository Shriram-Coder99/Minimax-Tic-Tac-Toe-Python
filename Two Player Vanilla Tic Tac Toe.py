from tkinter import *
import tkinter.messagebox
#from PIL import ImageTk, Image

X_player = True
moves = 0


def click_btn(button):#,X_IMG,O_IMG):    
    global X_player,moves
    if button["text"] == "" and X_player:
        button["text"] = "X"
        #button["image"] = X_IMG        
        X_player = False
        moves += 1
        check_winner()
    elif button["text"] == "" and not X_player:
        button["text"] = "O"
        #button["image"] = O_IMG        
        X_player = True
        moves += 1
        check_winner()
    elif button["text"] != "":
        tkinter.messagebox.showinfo(window,"Already Filled!")
        
def check_winner():
    global moves
    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X" or
    btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X" or
    btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X" or
    btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X" or
    btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X" or
    btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X" or
    btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X" or
    btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X"):        
        tkinter.messagebox.showinfo(window,"X Wins!")
        resetState()
        
    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
    btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or
    btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or
    btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O" or
    btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O" or
    btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O" or
    btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or
    btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O"):        
        tkinter.messagebox.showinfo(window,"O Wins!")
        resetState()
        
    elif moves >= 9:        
        tkinter.messagebox.showinfo(window,"Tie!")
        resetState()
        
def resetState():
    global moves, X_player
    moves = 0
    X_player = True
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""
    #return moves

window = Tk()
window.title("Tic Tac Toe")
window.geometry('600x530')
window.resizable(height = 0,width = 0)
X_IMG = PhotoImage(file = "blueX.png")
O_IMG = PhotoImage(file = "redCircle.png")
btn1 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn1))#,X_IMG,O_IMG))
btn1.grid(row = 0,column = 0)
btn2 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn2))#,X_IMG,O_IMG))
btn2.grid(row = 0,column = 1)
btn3 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn3))#,X_IMG,O_IMG))
btn3.grid(row = 0,column = 2)
btn4 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn4))#,X_IMG,O_IMG))
btn4.grid(row = 1,column = 0)
btn5 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn5))#,X_IMG,O_IMG))
btn5.grid(row = 1,column = 1)
btn6 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn6))#,X_IMG,O_IMG))
btn6.grid(row = 1,column = 2)
btn7 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn7))#,X_IMG,O_IMG))
btn7.grid(row = 2,column = 0)
btn8 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn8))#,X_IMG,O_IMG))
btn8.grid(row = 2,column = 1)
btn9 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn9))#,X_IMG,O_IMG))
btn9.grid(row = 2,column = 2)

window.mainloop()






