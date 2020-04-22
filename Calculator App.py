
import tkinter as tk


root= tk.Tk()
root.title("Calculator App")

expression= ""

entry= tk.Entry(root, width= 70, borderwidth= 5, bg= "grey")
entry.grid(row= 0, column= 0, columnspan= 5, padx= 10, pady= 10)


# Functions
def button_click(number):                                                       # to select a character/ operation onto the screen
    global expression
    current= entry.get()                                                        # to get the text from the entry widget to variable 'current'
    entry.delete(0, "end")
    entry.insert(0, str(current) + str(number))                                 # inserts the characters in the entry widget as string
    expression= entry.get()                                                     # copies the characters from entry widget to the variable 'expression'
    return

def button_clear():                                                             # function to clear the last entered character/ operator
    current= entry.get()
    entry.delete(0, "end")
    entry.insert(0, str(current)[ : -1])
    return

def button_allclear():                                                          # function to remove the entire characters from the entry widget
    entry.delete(0, "end")
    return

def button_eval():                                                              # function to evaluate the expression and gives the result
    global expression
    entry.delete(0, "end")
    final= str(eval(expression))
    expression= ""
    entry.insert(0, final)
    return





# define buttons
button_1= tk.Button(root, text='1', padx= 40, pady= 20, command= lambda: button_click(1))
button_2= tk.Button(root, text='2', padx= 40, pady= 20, command= lambda: button_click(2))
button_3= tk.Button(root, text='3', padx= 40, pady= 20, command= lambda: button_click(3))

button_4= tk.Button(root, text='4', padx= 40, pady= 20, command= lambda: button_click(4))
button_5= tk.Button(root, text='5', padx= 40, pady= 20, command= lambda: button_click(5))
button_6= tk.Button(root, text='6', padx= 40, pady= 20, command= lambda: button_click(6))

button_7= tk.Button(root, text='7', padx= 40, pady= 20, command= lambda: button_click(7))
button_8= tk.Button(root, text='8', padx= 40, pady= 20, command= lambda: button_click(8))
button_9= tk.Button(root, text='9', padx= 40, pady= 20, command= lambda: button_click(9))

button_0= tk.Button(root, text='0', padx= 40, pady= 20, command= lambda: button_click(0))

# Additional buttons
button_dot= tk.Button(root, text= ".", padx= 41, pady= 20, command= lambda: button_click('.'))
#button_braces= tk.Button(root, text= "( )", padx= 38, pady= 20, command= lambda: button_click(0))

button_plus= tk.Button(root, text= "+", padx= 39, pady= 20, command=lambda: button_click("+"))
button_minus= tk.Button(root, text= "-", padx= 40, pady= 20, command=lambda: button_click("-"))
button_mul= tk.Button(root, text= "*", padx= 40, pady= 20, command=lambda: button_click("*"))
button_div= tk.Button(root, text= "/", padx= 40, pady= 20, command=lambda: button_click("/"))

button_rem= tk.Button(root, text= "%", padx= 40, pady= 20, command=lambda: button_click("%"))
button_clr= tk.Button(root, text= "Clr", padx= 39, pady= 20, command= button_clear)
button_AC= tk.Button(root, text= "AC", padx= 39, pady= 20, command= button_allclear)
button_equal= tk.Button(root, text= "=", padx= 90, pady= 20, command= button_eval)


# Placing buttons on the screen
button_1.grid(row= 3, column= 0)
button_2.grid(row= 3, column= 1)
button_3.grid(row= 3, column= 2)

button_4.grid(row= 2, column= 0)
button_5.grid(row= 2, column= 1)
button_6.grid(row= 2, column= 2)

button_7.grid(row= 1, column= 0)
button_8.grid(row= 1, column= 1)
button_9.grid(row= 1, column= 2)

button_0.grid(row= 4, column= 1)

button_dot.grid(row= 4, column= 0)
#button_braces.grid(row= 4, column= 2)

button_div.grid(row= 1, column= 3)
button_mul.grid(row= 2, column= 3)
button_plus.grid(row= 3, column= 3)
button_minus.grid(row= 4, column= 2)

button_rem.grid(row= 1, column= 4)
button_clr.grid(row= 2, column= 4)
button_AC.grid(row= 3, column= 4)
button_equal.grid(row= 4, column= 3, columnspan= 2)


root.mainloop()