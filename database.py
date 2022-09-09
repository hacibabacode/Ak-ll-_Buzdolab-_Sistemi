from tkinter import *
import sqlite3 
import tkinter as tk


ws = tk.Tk()
ws.geometry("400x400")
ws.title('Database')
#Database

#Crete a database or connect to one
conn = sqlite3.connect('database.db')

#Create curcor
print("Bağlantı gerçekleştirildi.")

cursor = conn.cursor()

print("Cursor oluşturu")
#Create table
def tabloolustur():
 cursor.execute("CREATE TABLE PRODUCTS(name TEXT, number INT, type TEXT)")

def degerekle():
 cursor.execute("INSERT INTO PRODUCTS VALUES('2, Salatalık, 1 Kg, Sebze')")              

def submit():
  '''
   conn = sqlite3.connect('list.db')

   c = conn.cursor()

   #Insert Into Table
   c.execute("INSERT INTO PRODUCTS VALUES(:p_name, :p_type, :p_number",
   
   {
       
       'p_name' : p_name.get(),
       'p_type' : p_type.get(),
       'p_number' : p_number.get() 
    })

   conn.commit()
   
   conn.close()
#Clear The Text Boxes


p_name.delete(0, END)
p_type.delete(0, END)
p_number.delete(0, END)


'''
#Create Text Boxes


p_name = Entry(ws,width=30)
p_name.grid(row=0, column=1, padx=20,pady=20)

p_type = Entry(ws,width=30)
p_type.grid(row=1, column=1)

p_number = Entry(ws,width=30)
p_number.grid(row=2, column=1)

#Create Text Box Labels

p_name_label = Label(ws, text="Name giriniz")
p_name_label.grid(row=0, column=0)

p_type_label = Label(ws, text="Türünü giriniz")
p_type_label.grid(row=1, column=0)

p_number_label = Label(ws, text="Sayısını giriniz")
p_number_label.grid(row=2, column=0)

#Create Submit Button
submitbutton = Button(ws, text="Add Record To Database", command=submit)
submitbutton.grid(row=3, column=0, columnspan=2, pady=20, padx=20, ipadx=100)



#Commit Changes

conn.commit()
#Close Connection
conn.close()

ws.mainloop()