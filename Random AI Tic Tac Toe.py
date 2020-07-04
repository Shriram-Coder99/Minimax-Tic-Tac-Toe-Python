from tkinter import *
import tkinter.messagebox
import random

human_player = True
moves = 0
empty_spots = [i for i in range(1,10)]

def click_btn(button):   
    global human_player,moves
    
    if button["text"] == "" and human_player:
        button["text"] = "X"       
        human_player = False
        moves += 1
        remove_empty_spot(button)
        check_winner()
        
    elif button["text"] != "":
        tkinter.messagebox.showinfo(window,"Already Filled!")
    AITurn()
    
def AITurn():
    global empty_spots, human_player, moves
    if not human_player:
        n = random.choice(empty_spots)
        set_button_text(n)
        moves += 1
        check_winner()
        human_player = True

def remove_empty_spot(button):
    global empty_spots
    
    if button == btn1:
        empty_spots.remove(1)
    elif button == btn2:
        empty_spots.remove(2)
    elif button == btn3:
        empty_spots.remove(3)
    elif button == btn4:
        empty_spots.remove(4)
    elif button == btn5:
        empty_spots.remove(5)
    elif button == btn6:
        empty_spots.remove(6)
    elif button == btn7:
        empty_spots.remove(7)
    elif button == btn8:
        empty_spots.remove(8)
    elif button == btn9:
        empty_spots.remove(9)
    

def set_button_text(random_num):
    global empty_spots
    empty_spots.remove(random_num)
    if random_num == 1:
        btn1["text"] = "O"
    elif random_num == 2:
        btn2["text"] = "O"
    elif random_num == 3:
        btn3["text"] = "O"
    elif random_num == 4:
        btn4["text"] = "O"
    elif random_num == 5:
        btn5["text"] = "O"
    elif random_num == 6:
        btn6["text"] = "O"
    elif random_num == 7:
        btn7["text"] = "O"
    elif random_num == 8:
        btn8["text"] = "O"
    elif random_num == 9:
        btn9["text"] = "O"


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
        tkinter.messagebox.showinfo(window,"Human Wins!")
        resetState()
        return 'X'
        
    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
    btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or
    btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or
    btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O" or
    btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O" or
    btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O" or
    btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or
    btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O"):        
        tkinter.messagebox.showinfo(window,"AI Wins!")
        resetState()
        return 'O'
        
    elif moves >= 9:        
        tkinter.messagebox.showinfo(window,"Tie!")
        resetState()
        return 'Tie'
        
def resetState():
    global moves, human_player, empty_spots
    empty_spots = [i for i in range(1,10)]
    moves = 0
    human_player = True
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""

window = Tk()
window.title("Tic Tac Toe")
window.geometry('600x530')
window.resizable(height = 0,width = 0)
X_IMG = PhotoImage(file = "blueX.png")
O_IMG = PhotoImage(file = "redCircle.png")
btn1 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn1))
btn1.grid(row = 0,column = 0)
btn2 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn2))
btn2.grid(row = 0,column = 1)
btn3 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn3))
btn3.grid(row = 0,column = 2)
btn4 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn4))
btn4.grid(row = 1,column = 0)
btn5 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn5))
btn5.grid(row = 1,column = 1)
btn6 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn6))
btn6.grid(row = 1,column = 2)
btn7 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn7))
btn7.grid(row = 2,column = 0)
btn8 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn8))
btn8.grid(row = 2,column = 1)
btn9 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:click_btn(btn9))
btn9.grid(row = 2,column = 2)

window.mainloop()






