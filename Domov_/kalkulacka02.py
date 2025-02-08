from tkinter import *

root = Tk()


textbox=Entry(width=20, borderwidth=5)
textbox.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_click(number):
    curennt = textbox.get()
    textbox.delete(0, END)
    textbox.insert(0,str(curennt)+str(number))


def button_clear():
    textbox.delete(0, END)

def button_plus():
    first_number = textbox.get()
    global f_num
    global math
    math = "sucet"
    f_num= int(first_number)
    textbox.delete(0,END)

def button_rovnasa():
    second_number = textbox.get()
    textbox.delete(0,END)
    if math == "sucet":
        textbox.insert(0, f_num+ int(second_number))
    if math == "rozdiel":
        textbox.insert(0, f_num-int(second_number))    
    if math == "krat":
        textbox.insert(0, f_num* int(second_number))
    if math == "deleno":
        textbox.insert(0, f_num/ int(second_number))
def button_minus():
    first_number = textbox.get()
    global f_num
    global math
    math = "rozdiel"
    f_num = int(first_number)
    textbox.delete(0,END)

def button_krat():
    first_number = textbox.get()
    global f_num
    global math
    math = "krat"
    f_num = int(first_number)
    textbox.delete(0,END) 

def button_deleno():
    first_number = textbox.get()
    global f_num
    global math
    math = "deleno"
    f_num = int(first_number)
    textbox.delete(0,END)




button1=Button(root,text = "1", padx=10, pady=5, command=lambda:button_click(1))
button1.grid(row=1, column=0)

button2=Button(root,text = "2", padx=10, pady=5, command=lambda:button_click(2))
button2.grid(row=1, column=1)

button3=Button(root,text = "3", padx=10, pady=5, command=lambda:button_click (3))
button3.grid(row=1, column=2)

button4=Button(root,text = "4", padx=10, pady=5, command=lambda:button_click(4))
button4.grid(row=2, column=0)

button5=Button(root,text = "5", padx=10, pady=5, command=lambda:button_click(5))
button5.grid(row=2, column=1)

button6=Button(root,text = "6", padx=10, pady=5, command=lambda:button_click(6))
button6.grid(row=2, column=2)

button7=Button(root,text = "7", padx=10, pady=5, command=lambda:button_click(7))
button7.grid(row=3, column=0)

button8=Button(root,text = "8", padx=10, pady=5, command=lambda:button_click(8))
button8.grid(row=3, column=1)

button9=Button(root,text = "9", padx=10, pady=5, command=lambda:button_click(9))
button9.grid(row=3, column=2)

button0=Button(root,text = "0", padx=10, pady=5, command=lambda:button_click(0))
button0.grid(row=4, column=0)

buttonm=Button(root,text="-", padx=10, pady=5, command=button_minus)
buttonm.grid(row=4, column=1)

buttonp=Button(root,text="+", padx=10, pady=5, command=button_plus)
buttonp.grid(row=4, column=2)

buttonk=Button(root,text="÷",padx=10, pady=5, command=button_deleno)
buttonk.grid(row=5, column=0)

buttonk=Button(root,text="x",padx=10, pady=5, command=button_krat)
buttonk.grid(row=5, column=1)

buttonC=Button(root,text="C", padx=10, pady=5, command=button_clear)
buttonC.grid(row=5, column=2,)

buttonr=Button(root,text="=", padx=10, pady=75, command=button_rovnasa)
buttonr.grid(row=1, column=3, rowspan=5)










root.mainloop()
