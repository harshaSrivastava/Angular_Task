# # from datetime import datetime

# # # datetime object containing current date and time
# # now = datetime.now()
 
# # # print("now =", now)

# # # # dd/mm/YY H:M:S
# # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# # print("date and time =", dt_string)	
# from datetime import date

# today = date.today()
# print("Today's date:", today)
# # importing whole module
# from tkinter import *
# from tkinter.ttk import *

# # importing strftime function to
# # retrieve system's time
# from time import strftime

# # creating tkinter window
# root = Tk()
# root.title('Clock')

# # This function is used to
# # display time on the label
# def time():
# 	string = strftime('%H:%M:%S %p')
# 	lbl.config(text = string)
# 	lbl.after(1000, time)

# # Styling the label widget so that clock
# # will look more attractive
# lbl = Label(root, font = ('calibri', 40, 'bold'),
# 			background = 'purple',
# 			foreground = 'white')

# # Placing clock at the centre
# # of the tkinter window
# lbl.pack(anchor = 'center')
# time()

# mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


def quit(*args):
    root.destroy()

def clock_time():

    time= datetime.datetime.now()
    time= (time.strftime("Date: %Y -%m -%d \nTime: %H:%M:%S"))
    txt.set(time)

    root.after(1000,clock_time)

root =Tk()
# root.attributes("-fullscreen", False)
root.configure(bg= "black")
root.bind("x",quit)
root.geometry("1200x400")
root.title("Digital Clock Gui By Vaibhav")
root.after(1000,clock_time)

fnt = font.Font(family = "helvetica",size=80, weight ="bold")
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt, font = fnt, foreground= "white",background= "black")
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)

root.mainloop()