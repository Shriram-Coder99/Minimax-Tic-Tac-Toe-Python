from tkinter import *
import tkinter.messagebox
import random
import math

human_turn = False
moves = 0
board = ['' for i in range(9)]

def make_human_move(num):
    global human_turn,moves,board
    if human_turn:
        if board[num] == '':
            board[num] = 'O'
            moves += 1
            set_text(board)
            human_turn = False
            check_for_win(board)
            show_winner()
            
            make_AI_move()
        else:
            tkinter.messagebox.showinfo(window,"Filled!")
        
    
    
def make_AI_move():
    global moves,human_turn,board
    best_score = -math.inf
    best_spot = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(False,board)
            board[i] = ''
            
            if score > best_score:
                best_score = score
                best_spot = i
                
    print(best_spot)      
    board[best_spot] = 'X'
    moves += 1
    set_text(board)
    human_turn = True
    check_for_win(board)
    show_winner()

def minimax(isMaximizer,board):
    #return 1
    score = check_for_win(board)
    
    if score == "X":
        return 10
    elif score == "O":
        return -10
    elif score == 'Tie':
        return 0
    
    if isMaximizer:
        best_score = -math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(False,board)
                board[i] = ''
                best_score = max(score,best_score)
        return best_score
    
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(True,board)
                board[i] = ''
                best_score = min(score,best_score)
        return best_score
    

def set_text(board):
        
    btn0["text"] = board[0] if board[0] != "" else ""
    btn1["text"] = board[1] if board[1] != "" else ""
    btn2["text"] = board[2] if board[2] != "" else ""
    btn3["text"] = board[3] if board[3] != "" else ""
    btn4["text"] = board[4] if board[4] != "" else ""
    btn5["text"] = board[5] if board[5] != "" else ""
    btn6["text"] = board[6] if board[6] != "" else ""
    btn7["text"] = board[7] if board[7] != "" else ""
    btn8["text"] = board[8] if board[8] != "" else ""
    


def check_for_win(board):    
    global moves
    if (board[0] == "X" and board[1] == "X" and board[2] == "X" or
        board[3] == "X" and board[4] == "X" and board[5] == "X" or
        board[6] == "X" and board[7] == "X" and board[8] == "X" or
        board[0] == "X" and board[3] == "X" and board[6] == "X" or
        board[1] == "X" and board[4] == "X" and board[7] == "X" or
        board[2] == "X" and board[5] == "X" and board[8] == "X" or
        board[0] == "X" and board[4] == "X" and board[8] == "X" or
        board[2] == "X" and board[4] == "X" and board[6] == "X"):
        #print(board)
        #tkinter.messagebox.showinfo(window,"X Wins!")
        #print("Also")
        #resetState()
        return "X"
    
    elif (board[0] == "O" and board[1] == "O" and board[2] == "O" or
        board[3] == "O" and board[4] == "O" and board[5] == "O" or
        board[6] == "O" and board[7] == "O" and board[8] == "O" or
        board[0] == "O" and board[3] == "O" and board[6] == "O" or
        board[1] == "O" and board[4] == "O" and board[7] == "O" or
        board[2] == "O" and board[5] == "O" and board[8] == "O" or
        board[0] == "O" and board[4] == "O" and board[8] == "O" or
        board[2] == "O" and board[4] == "O" and board[6] == "O"):
        #tkinter.messagebox.showinfo(window,"O Wins!")
        #print("Also")
        #resetState()
        return "O"
    
    elif moves == 9:
        #tkinter.messagebox.showinfo(window,"Tie!")
        #print("Also")
        #resetState()
        return "Tie"
    
def show_winner():
    global board
    winner = check_for_win(board)
    if winner == "X":
        msg = "AI Wins!"
    elif winner == "O":
        msg = "You Win!"
    elif winner == "Tie":
        msg = "Tie!"
    if winner in ["X","O","Tie"]:
        tkinter.messagebox.showinfo(window,msg)
        resetState()
        
def resetState():
    global moves, human_turn, board
    board = ['' for i in range(9)]
    moves = 0
    human_turn = True
    set_text(board)
    make_AI_move()

window = Tk()
window.title("Tic Tac Toe")
window.geometry('600x530')
window.resizable(height = 0,width = 0)
btn0 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(0))
btn0.grid(row = 0,column = 0)
btn1 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(1))
btn1.grid(row = 0,column = 1)
btn2 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(2))
btn2.grid(row = 0,column = 2)
btn3 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(3))
btn3.grid(row = 1,column = 0)
btn4 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(4))
btn4.grid(row = 1,column = 1)
btn5 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(5))
btn5.grid(row = 1,column = 2)
btn6 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(6))
btn6.grid(row = 2,column = 0)
btn7 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(7))
btn7.grid(row = 2,column = 1)
btn8 = Button(window,height = 5,width = 12,text = "",font = "Times 20 bold",bg = 'white',cursor = 'hand2',command = lambda:make_human_move(8))
btn8.grid(row = 2,column = 2)
make_AI_move()
window.mainloop()







