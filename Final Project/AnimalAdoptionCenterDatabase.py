# Program made solely by Ethan Smith

# Final Project: Animal Adoption Center Database

from tkinter import *
from tkinter import ttk
import pandas as pd

list = ["text", "hopefully", "this", "works"]
# Configuring my window for the program
window = Tk()
window.title('Adoption Database')
window.minsize(width=300, height=300)
window.resizable(width=False, height=False)
    
    
# Configuring my Labels

Label(window, text='Pet Name').grid(row=4)
Label(window, text='Pet Type').grid(row=5)
Label(window, text='Pet Breed').grid(row=6)
Label(window, text='Pet Age').grid(row=7)
Label(window, text='Pet Weight').grid(row=8)
Label(window, text='Available for Adoption?').grid(row=9)

# Configuring my Entrys
pnEntry = Entry(window)
pnEntry.config(state='readonly')
ptEntry = Entry(window)
ptEntry.config(state='readonly')
pbEntry = Entry(window)
pbEntry.config(state='readonly')
paEntry = Entry(window)
paEntry.config(state='readonly')
pwEntry = Entry(window)
pwEntry.config(state='readonly')

# Importing Values From Spreadsheet
file_location = "C:\\Users\\ethan\\OneDrive\\Desktop\\Final Project\\pets.xlsx"
pets= pd.read_excel(file_location, usecols="A")
listpetname = pets.values.tolist()
pets= pd.read_excel(file_location, usecols="B")
listpettype = pets.values.tolist()
pets= pd.read_excel(file_location, usecols="C")
listpetbreed = pets.values.tolist()
pets= pd.read_excel(file_location, usecols="D")
listpetage = pets.values.tolist()
pets= pd.read_excel(file_location, usecols="E")
listpetweight = pets.values.tolist()
pets= pd.read_excel(file_location, usecols="F")
listpetATA = pets.values.tolist()

# Callback From Button Press To Retrieve Selected Items Index and Changing Entry Values Upon Botton Press
def callback():
    
    pnEntry.config(state='normal')
    pnEntry.delete(0,END)
    ptEntry.config(state='normal')
    ptEntry.delete(0,END)
    pbEntry.config(state='normal')
    pbEntry.delete(0,END)
    paEntry.config(state='normal')
    paEntry.delete(0,END)
    pwEntry.config(state='normal')
    pwEntry.delete(0,END)
    global nameIndex
    nameIndex = combo.current()
    print(nameIndex)
    print(listpetname[nameIndex])
    pnEntry.insert(0, listpetname[nameIndex])
    ptEntry.insert(0, listpettype[nameIndex])
    pbEntry.insert(0, listpetbreed[nameIndex])
    paEntry.insert(0, listpetage[nameIndex])
    pwEntry.insert(0, listpetweight[nameIndex])
    pnEntry.config(state='readonly')
    ptEntry.config(state='readonly')
    pbEntry.config(state='readonly')
    paEntry.config(state='readonly')
    pwEntry.config(state='readonly')
    ATA = str(listpetATA[nameIndex])
    if ATA == "['Yes']":
        cb.select()
        print("Selected")
    else:
        cb.deselect()
        print("Deselected")


# Configuring my Drop Down
Label(window, text='Pick a pet from the drop down').grid(row=0,column=1)
Label(window, text='             ').grid(row=0,column=2)
but = Button(window, text='Select',command=callback)
but.grid(row=2,column=1)

# Populating my Dropdown
combo = ttk.Combobox(
    state="readonly",
    values=listpetname
)  

# Griding my Entrys
pnEntry.grid(row=4, column=1)
ptEntry.grid(row=5, column=1)
pbEntry.grid(row=6, column=1)
paEntry.grid(row=7, column=1)
pwEntry.grid(row=8, column=1)

# Griding the Dropdown Box
combo.grid(row=1, column=1)

# Configuring the Checkbox for Adoption Availability
cb = Checkbutton(window, state='disabled')
cb.grid(row=9,column=1)
# Loading my Main Window
window.mainloop()



