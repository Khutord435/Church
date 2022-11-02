from re import T
from tkinter import *
import os

root = Tk()

def buttonClocked():
   # text = myInput.insert(0, "r'")
   # text2 = myInput.insert(END, "'")
    text = myInput.get()
    new_text = text.replace("'\'", "/")
    #myLabel1 = Label(root, text= text )
    for file in os.listdir(new_text):
        if file.endswith(".pptx"):
            full_path = os.path.join(new_text, file)
            myList.insert(0, full_path)
           # myLabel1.append(full_path)
            myList.grid(row=4, column=0)
    print(value)

myLabel = Label(root, text="Enter song:   ")
mybutton = Button(root, text="Search", command=buttonClocked)
myInput = Entry(root, width = 40)
myInput.grid(row=0, column=1)
myLabel.grid(row=0, column=0)
myList = Listbox(root, width=70)
mybutton.grid(row=0, column=2)
value = myInput.get()


root.mainloop()