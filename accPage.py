
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

ws3 = tk.Tk()
ws3.geometry("750x750")
canvas = Canvas(ws3, height=450, width=750)
canvas.pack()

def yeni_List():
    ws3.withdraw()
    import yenilist
def eski_List():
    ws3.withdraw()
    import eskilist

def dead_Line():
    ws3.withdraw()
    import deadline

def buzdolabi_Page():
    ws3.withdraw()
    import buzdolabi_Page


yeniButton = tk.Button(ws3, text="Yeni Liste", command=yeni_List)
yeniButton.place(x=300, y=225)
eskiButton = tk.Button(ws3, text="Eski Liste", command=eski_List)
eskiButton.place(x=420, y=225)
expirationDateButton = tk.Button(ws3, text="Expiration Date", command=dead_Line)
expirationDateButton.place(x=350, y=275)
buzdolabiButton = tk.Button(ws3, text="Refrigerator", command=buzdolabi_Page)
buzdolabiButton.place(x=360, y=320)


ws3.mainloop()