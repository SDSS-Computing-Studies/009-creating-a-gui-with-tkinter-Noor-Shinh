import tkinter as tk 
from tkinter import *
from tkinter import ttk
window=tk.Tk()
window.title=("Task 4")
window.geometry("255x125")
dogphoto = PhotoImage(file="dog.png")
label1=tk.Label(window,image=dogphoto)
label2=tk.Label(window,text="Pochacco!")
label3=tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brough you Keropi and Kero Kero",background="#aaffff")
label1.place(x=60,y=0)
label2.place(x=125,y=35)
label3.place(x=0,y=90)

window.mainloop()

