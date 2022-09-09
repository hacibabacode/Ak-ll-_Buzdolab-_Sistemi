from tkinter import *
from  tkinter import ttk
import tkinter as tk


ws2  = tk.Tk()
ws2.title('Eski Liste')
canvas = tk.Canvas(ws2, height=50, width=750)
canvas.pack()

bak_frame = Frame(ws2)
bak_frame.pack()

#scrollbar
bak_scroll = Scrollbar(bak_frame)
bak_scroll.pack(side=RIGHT, fill=Y)

bak_scroll = Scrollbar(bak_frame,orient='horizontal')
bak_scroll.pack(side= BOTTOM,fill=X)

my_bak = ttk.Treeview(bak_frame,yscrollcommand=bak_scroll.set, xscrollcommand =bak_scroll.set)


my_bak.pack()

bak_scroll.config(command=my_bak.yview)
bak_scroll.config(command=my_bak.xview)

#define our column
 
my_bak['columns'] = ('Name', 'Number', 'Type')

# format our column
my_bak.column("#0", width=0,  stretch=NO)
my_bak.column("Name",anchor=CENTER, width=80)
my_bak.column("Number",anchor=CENTER,width=80)
my_bak.column("Type",anchor=CENTER,width=80)


#Create Headings 
my_bak.heading("#0",text="",anchor=CENTER)
my_bak.heading("Name",text="Name",anchor=CENTER)
my_bak.heading("Number",text="Kg",anchor=CENTER)
my_bak.heading("Type",text="Type",anchor=CENTER)


#add data 
my_bak.insert(parent='',index='end',iid=0,text='',
values=('Muz','1 Kg','Meyve'))
my_bak.insert(parent='',index='end',iid=1,text='',
values=('Salatalık','1 Kg','Sebze'))
my_bak.insert(parent='',index='end',iid=2,text='',
values=('Kola','3 Adet','İçecek'))
my_bak.insert(parent='',index='end',iid=3,text='',
values=('Soda','6 Adet','İçecek'))
my_bak.insert(parent='',index='end',iid=4,text='',
values=('Süt','2 Adet','İçecek'))
my_bak.insert(parent='',index='end',iid=5,text='',
values=('Kaşar','750 Gram','Kahvaltı'))
my_bak.insert(parent='',index='end',iid=6,text='',
values=('Peynir','600 Gram','Kahvaltı'))
my_bak.insert(parent='',index='end',iid=7,text='',
values=('Krema','1 Adet','Yemek'))
my_bak.insert(parent='',index='end',iid=8,text='',
values=('Sucuk','650 Gram','Kahvaltı'))
my_bak.insert(parent='',index='end',iid=9,text='',
values=('Zeytin','500 Gram','Kahvaltı'))
my_bak.insert(parent='',index='end',iid=10,text='',
values=('Domates','1 Kg','Sebze'))
my_bak.insert(parent='',index='end',iid=11,text='',
values=('Salça','1 Adet','Yemek'))
my_bak.insert(parent='',index='end',iid=12,text='',
values=('Tost Ekmeği','1 Adet','Kahvaltı'))
my_bak.insert(parent='',index='end',iid=13,text='',
values=('Marul','1 Adet','Sebze'))
my_bak.insert(parent='',index='end',iid=14,text='',
values=('Elma','3 Adet','Meyve'))


my_bak.pack()

frame = Frame(ws2)
frame.pack(pady=20)

#labels
playername= Label(frame,text = "Name")
playername.grid(row=0,column=0 )

playernumber = Label(frame,text="Number")
playernumber.grid(row=0,column=1)

playertype = Label(frame,text="Type")
playertype.grid(row=0,column=2)

#Entry boxes
playername_entry= Entry(frame)
playername_entry.grid(row= 1, column=0)

playernumber_entry = Entry(frame)
playernumber_entry.grid(row=1,column=1)

playertype_entry = Entry(frame)
playertype_entry.grid(row=1,column=2)

#Select Record
def select_record():
    #clear entry boxes
    playername_entry.delete(0,END)
    playernumber_entry.delete(0,END)
    playertype_entry.delete(0,END)
    
    #grab record
    selected=my_bak.focus()
    #grab record values
    values = my_bak.item(selected,'values')
    #temp_label.config(text=selected)

    #output to entry boxes
    playername_entry.insert(0,values[0])
    playernumber_entry.insert(0,values[1])
    playertype_entry.insert(0,values[2])

#save Record
def update_record():
    selected=my_bak.focus()
    #save new data 
    my_bak.item(selected,text="",values=(playername_entry.get(),playergram_entry.get(),playernumber_entry.get()))
    
   #clear entry boxes
    playername_entry.delete(0,END)
    playernumber_entry.delete(0,END)
    playertype_entry.delete(0,END)

#Back
def access_pageexp():
    ws2.withdraw()
    import runpy
    file_globals = runpy.run_path("accPage.py")

def backAction():
    ws2.withdraw()
    access_pageexp()
  
#Buttons
select_button = tk.Button(ws2,text="Select Record", command=select_record)
select_button.pack(pady =10)

edit_button = tk.Button(ws2,text="Edit ",command=update_record)
edit_button.pack(pady = 10)

nextButton = tk.Button(ws2, text="Back", command=backAction)
nextButton.place(x=145, y=425)




ws2.mainloop()