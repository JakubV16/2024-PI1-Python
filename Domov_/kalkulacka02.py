from tkinter import *

root = Tk()


textbox=Entry(width=20, borderwidth=5)
textbox.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
def button_click():
    


button1=Button(root,text = "1", padx=30, pady=20, command=button_click )
button1.grid(row=1, column=0)

button2=Button(root,text = "2", padx=30, pady=20, command=button_click)
button2.grid(row=1, column=1)

button3=Button(root,text = "3", padx=30, pady=20, command=button_click )
button3.grid(row=1, column=2)

button4=Button(root,text = "4", padx=30, pady=20, command=button_click)
button4.grid(row=2, column=0)

button5=Button(root,text = "5", padx=30, pady=20, command=button_click)
button5.grid(row=2, column=1)

button6=Button(root,text = "6", padx=30, pady=20, command=button_click)
button6.grid(row=2, column=2)

button7=Button(root,text = "7", padx=30, pady=20, command=button_click)
button7.grid(row=3, column=0)

button8=Button(root,text = "8", padx=30, pady=20, command=button_click)
button8.grid(row=3, column=1)

button9=Button(root,text = "9", padx=30, pady=20, command=button_click)
button9.grid(row=3, column=2)

button0=Button(root,text = "0", padx=30, pady=20, command=button_click)
button0.grid(row=4, column=0)

buttonm=Button(root,text="-", padx=30, pady=20, command=button_click)
buttonm.grid(row=4, column=1)

buttonp=Button(root,text="+", padx=30, pady=20, command=button_click)
buttonp.grid(row=4, column=2)

buttonk=Button(root,text="÷",padx=30, pady=20, command=button_click)
buttonk.grid(row=5, column=0)

buttonk=Button(root,text="x",padx=30, pady=20, command=button_click)
buttonk.grid(row=5, column=1)

buttonC=Button(root,text="C", padx=30, pady=20, command=button_click)
buttonC.grid(row=5, column=2)

buttonx2=Button(root,text="x²", padx=30, pady=20, command=button_click)
buttonx2.grid(row=1, column=3)

buttonback=Button(root,text="<--", padx=30, pady=20, command=button_click)
buttonback.grid(row=2, column=3)

buttonr=Button(root,text="=", padx=30, pady=20, command=button_click)
buttonr.grid(row=3, column=3)










root.mainloop()
