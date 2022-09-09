
import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image


ws6= tk.Tk()
ws6.geometry("700x700")
ws6.title('Refrigerator')

canvas = Canvas(ws6, height=20, width=20)
canvas.pack()


my_img = ImageTk.PhotoImage(Image.open("images/buzdolabi.jpg"))
label = Label(image=my_img)
label.pack()


def resim_Page():
    ws6.withdraw()
    import resimPage
   

nextbutton = tk.Button(ws6, text="Camera Product", command=resim_Page)
nextbutton.place(x=300, y=600)

ws6.mainloop()
