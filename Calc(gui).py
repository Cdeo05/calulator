from tkinter import *


root = Tk()
root.title("Calculator")
textin= StringVar()
operator=""


def clickbut(x):
    global operator
    operator=operator+str(x)
    textin.set(operator)
    
def clr():
    global operator
    operator=""
    textin.set('')
    
    
def equal():
    global operator
    result=eval(operator)
    textin.set(result)
    operator=str(result)

    
    

entry = Entry(root,textvar=textin)
button_9 = Button(root, text="9", width=4, height=2, bg="cyan",command= lambda:clickbut(9))
button_8 = Button(root, text="8", width=4, height=2, bg="cyan",command= lambda:clickbut(8))
button_7 = Button(root, text="7", width=4, height=2, bg="cyan",command= lambda:clickbut(7))
button_6 = Button(root, text="6", width=4, height=2,bg="cyan",command= lambda:clickbut(6))
button_5 = Button(root, text="5", width=4, height=2, bg="cyan",command= lambda:clickbut(5))
button_4 = Button(root, text="4", width=4, height=2, bg="cyan",command= lambda:clickbut(4))
button_3 = Button(root, text="3", width=4, height=2, bg="cyan",command= lambda:clickbut(3))
button_2 = Button(root, text="2", width=4, height=2, bg="cyan",command= lambda:clickbut(2))
button_1 = Button(root, text="1", width=4, height=2, bg="cyan", command= lambda:clickbut(1))
button_ac =Button(root, text="AC", width=9,height=2, bg="cyan",command= lambda:clr())
button_0 = Button(root, text="0", width=4, height=2, bg="cyan",command= lambda:clickbut(0))
button_add = Button(root, text="+", width=4, height= 2, bg="cyan",command= lambda:clickbut("+"))
button_sub = Button(root, text="-", width=4, height= 2, bg="cyan", command= lambda:clickbut("-"))
button_x = Button(root, text="x", width=4, height= 2, bg="cyan", command= lambda:clickbut("*"))
button_div = Button(root, text="/", width=4, height= 2, bg="cyan", command= lambda:clickbut("/"))
button_equal=Button(root, text="=",width=15, height=2, bg ="cyan",command= equal)
button_dot=Button(root, text=".", width=4, height=2, bg="cyan", command= lambda:clickbut("."))


button_9.grid( row=1)
button_8.grid( row=1 ,column=1)
button_7.grid( row=1 ,column=2)
button_6.grid( row=2 ,column=0)
button_5.grid( row=2 ,column=1)
button_4.grid( row=2 ,column=2)
button_3.grid( row=3 ,column=0)
button_2.grid( row=3 ,column=1)
button_1.grid( row=3 ,column=2)
button_ac.grid( row=4 ,columnspan=2)
button_0.grid( row=4, column=2)
button_x.grid( row=1, column=3)
button_div.grid( row=2, column=3)
button_sub.grid( row=3, column=3)
button_add.grid( row=4, column=3)
entry.grid(row=0,columnspan=6)
button_equal.grid(row=5,columnspan=3)
button_dot.grid(row=5,column=3)


root.mainloop()