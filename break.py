import time
from tkinter import *

run_the_program = 1

def clickedOK():
    btn1.destroy()
    lbl.configure(text ="5 minutes break started")
    root.after(5000*60, root.destroy)

def quit():
    global run_the_program
    run_the_program = 0
    root.destroy()

def break_duration():
    pass

def int_duration():
    pass

def display_clock():
    pass

def open_settings():
    settings = Toplevel()
    settings.attributes('-topmost', True)
    settings.geometry("200x100")
    settings.title("Settings")
    btn1 = Button(settings, text = "Break Duration" , fg = "blue", command=break_duration)  
    btn1.grid()
    btn2 = Button(settings, text = "Interval Duration" , fg = "blue", command=int_duration)  
    btn2.grid(column=0, row=1)
    btn3 = Button(settings, text = "Display Clock" , fg = "blue", command=display_clock)  
    btn3.grid(column=0, row=2)

time.sleep(30*60)

while run_the_program:

    root = Tk() 
    root.attributes('-topmost', True) 
    root.title("Take a Break")  
    root.geometry('250x75')

    lbl = Label(root, text = "Take a 5 minutes break, Janu") 
    lbl.grid()

    btn1 = Button(root, text = "OK" , fg = "blue", command=clickedOK)  
    btn1.grid(column=1, row=0)
    btn2 = Button(root, text = "Quit the Program", fg = "blue", command=quit) 
    btn2.grid(column=0,row=1)
    btn3 = Button(root, text = "Settings", fg = "blue", command=open_settings) 
    btn3.grid(column=1, row=1)
    root.mainloop()

    if(run_the_program):
        time.sleep(30*60)