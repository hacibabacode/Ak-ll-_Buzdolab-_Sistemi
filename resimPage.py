from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image

ws7= tk.Tk()
ws7.geometry("700x700")
ws7.title('Refrigerator Object Detection')
canvas = tk.Canvas(ws7, height=20, width=20)
canvas.pack()

my_img2 = ImageTk.PhotoImage(Image.open("images/Refrigerator.jpg"))
my_label = Label(image=my_img2)
my_label.pack()

button1_quit = tk.Button(ws7, text="Exit Program", command=ws7.quit)
button1_quit.place(x=300, y=600)

 
ws7.mainloop()
