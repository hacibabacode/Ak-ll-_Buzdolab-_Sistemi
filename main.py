import tkinter as tk
from tkinter import *
from tkinter import messagebox


ws = tk.Tk()

canvas = tk.Canvas(ws, height=450, width=750)
canvas.pack()

def access_page():
    ws.withdraw()
    import accPage



def ButtonFunc():
    messagebox.showinfo( "Hello and Welcome !", 
    "This application is a smart refrigerator system.In this application is an application that displays and determines the products in the refrigerator, their expiration date and the products that are in the refrigerator.")


loginButton = tk.Button(ws, text="Access", command=access_page)
loginButton.place(x=300, y=225)
InformationButton =tk.Button(ws, text ="Information", command = ButtonFunc)
InformationButton.place(x=365, y=125)

exitButton = tk.Button(text = "ÇIKIŞ", command=ws.quit)
exitButton.place(x=500, y=225)

ws.mainloop()