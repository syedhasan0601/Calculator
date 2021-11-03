from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

win = Tk()

win.wm_title('Calculator2')

#functions
def button_click(number):
    #line.delete(0,END)          #will clear the text field
    current = line.get()
    line.delete(0,END)
    line.insert(0,str(current)+str(number))

def button_clear():
    line.delete(0,END)

def button_add():
    first_number = line.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    line.delete(0,END)

def button_minus():
    first_number = line.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    line.delete(0,END)

def button_multiply():
    first_number = line.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    line.delete(0,END)

def button_divide():
    first_number = line.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    line.delete(0,END)

def button_equal():
    second_number  = line.get()
    line.delete(0,END)
    
    if math == "addition":
        line.insert(0,f_num + int(second_number))
    elif math == "subtraction":
        line.insert(0,f_num - int(second_number))
    elif math == "multiplication":
        line.insert(0,f_num * int(second_number))
    else:
        line.insert(0,f_num / int(second_number))



#entry
line = Entry(win,width=35,borderwidth=5)
line.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#buttons
b1 = Button(win,text='7',pady=10,width=10,command=lambda: button_click(7))
b1.grid(row=1,column=0)

b2 = Button(win,text='8',pady=10,width=10,command=lambda: button_click(8))
b2.grid(row=1,column=1)

b3 = Button(win,text='9',pady=10,width=10,command=lambda: button_click(9))
b3.grid(row=1,column=2)

b4 = Button(win,text='4',pady=10,width=10,command=lambda: button_click(4))
b4.grid(row=2,column=0)

b5 = Button(win,text='5',pady=10,width=10,command=lambda: button_click(5))
b5.grid(row=2,column=1)

b6 = Button(win,text='6',pady=10,width=10,command=lambda: button_click(6))
b6.grid(row=2,column=2)

b7 = Button(win,text='1',pady=10,width=10,command=lambda: button_click(1))
b7.grid(row=3,column=0)

b8 = Button(win,text='2',pady=10,width=10,command=lambda: button_click(2))
b8.grid(row=3,column=1)

b9 = Button(win,text='3',pady=10,width=10,command=lambda: button_click(3))
b9.grid(row=3,column=2)

b10 = Button(win,text='0',pady=10,width=10,command=lambda: button_click(0))
b10.grid(row=4,column=0)

b11 = Button(win,text='+',pady=10,width=10,command=button_add)
b11.grid(row=4,column=1)

b12 = Button(win,text='-',pady=10,width=10,command=button_minus)
b12.grid(row=4,column=2)

b13 = Button(win,text='*',pady=10,width=10,command=button_multiply)
b13.grid(row=5,column=0)

b14 = Button(win,text='/',pady=10,width=10,command=button_divide)
b14.grid(row=5,column=1)

b15 = Button(win,text='=',pady=10,width=10,command=button_equal)
b15.grid(row=5,column=2)

b16 = Button(win,text='Exit',pady=10,width=10,command=win.destroy)
b16.grid(row=6,column=0,columnspan=1)

b17 = Button(win,text='Clear',pady=10,width=22,command=button_clear)
b17.grid(row=6,column=1,columnspan=2)











win.mainloop()