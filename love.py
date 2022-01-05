# LOVE-CALCULATOR
import tkinter
from tkinter import *
import random
root = Tk()
root.geometry('450x350')
root.title("LoVE CalCuLATor")

def find():
    s = '456789'
    digit = 2
    result.config(text= "".join(random.sample(s,digit)))

head = Label(root , text = 'LOVE CALCULTOR' , font = ("goudy stout" , 20 ))
head.pack()

body = Label(root , text = 'Enter Your and Your lovers name')
body.pack()

bodyi = Label(root , text = 'Enter Your name')
bodyi.pack()

num_enter = Entry(root , font = ("arial ", 15 , "bold"),border = 5 , bg = "white" , fg = 'green')
num_enter.pack()

bodye = Label(root , text = 'Enter Your lovers name')
bodye.pack()

num_enter2 = Entry(root , font = ("arial ", 15 , "bold"),border = 5 , bg = "white" , fg = 'green')
num_enter2.pack()

btn = Button(root , text = 'CALCULATE' , font = "Broadway" , width = 10 , height = 1 , command = find )
btn.pack(pady = 4)

result = Label(root , text = 'LOVE PRECENTAGE' , bg = 'cyan',fg ='blue', font = ("Broadway",22,"bold"))
result.pack(pady = 5)

btn2 = Button(root , text = 'Quit ! love calculator :(' , width = 25, height = 2 , command = root.destroy)
btn2.pack(pady = 15 , anchor = 'se')

tkinter.mainloop()

