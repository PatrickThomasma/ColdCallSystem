"""
This will be the main GUI for students

Author: Patrick Thomasma, David Han
Last Modified: 01/14/2022

If on Linux Ubuntu use sudo apt-get install python3-tk for tkinter Module
"""
from tkinter import *
#pip install pynput in terminal; necessary for arrow input check
from pynput.keyboard import *

# Test this list, then test sample file, then test through backened pull
studentList = ["Patrick Thomasma", "David Han", "Kassandra Motaro", "Briana Vago", "Geli Zhang"]
# exRandomList = ["AA", "AB", "AC", "AD"]

listIndex = 0

#Runs the window
root = Tk()
root.geometry("900x100+300+850")
root.minsize(900, 100)
root.maxsize(900, 100)

# def toggleStudent(n):
#     toggle = Label(root, text=studentList[n])
#     toggle.pack()

def leftKey(event): #update list Index and color slots so its consistent with each key press
    global listIndex
    global slots
    if listIndex == 0:
        return
    slots[listIndex].config({"background": "Blue"})
    slots[listIndex].config({"foreground": "White"})
    listIndex -= 1
    slots[listIndex].config({"background": "White"})
    slots[listIndex].config({"foreground": "Black"})

def rightKey(event): #update list index until it hits the end of the list, keep coloring of buttons consistent with other key presses
    global listIndex
    global slots
    if listIndex == 3:
        return
    slots[listIndex].config({"background": "Blue"})
    slots[listIndex].config({"foreground": "White"})
    listIndex += 1
    slots[listIndex].config({"background": "White"})
    slots[listIndex].config({"foreground": "Black"})

 
myLabel1 = Label(root, text= "Cold Call" , font=("Arial", 20))
myLabel1.grid(row = 0, column = 1, padx = 5, pady = 5)

##myLabel2 = Label(root, text=studentList[1], font=("Arial", 20))
##myLabel2.grid(row=0, column=1)

##myLabel3 = Label(root, text=studentList[2], font=("Arial", 20))
##myLabel3.grid(row=0, column=2)

##myLabel4 = Label(root, text=studentList[3], font=("Arial", 20))
##myLabel4.grid(row=0, column=3)

slot0 = Label(root, text = studentList[0], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
slot0.grid(row = 1, column = 1, padx = 5, pady = 5)

slot1 = Label(root, text = studentList[1], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
slot1.grid(row = 1, column = 2, padx = 5, pady = 5)

slot2 = Label(root, text = studentList[2], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
slot2.grid(row = 1, column = 3, padx = 5, pady = 5)

slot3 = Label(root, text = studentList[3], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
slot3.grid(row = 1, column = 4, padx = 5, pady = 5)

slots = [slot0,slot1,slot2,slot3]

slot0.config({"background": "White"})
slot0.config({"foreground": "Black"})

# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "DA")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

# myLabel.pack()

# if key == Key.backspace:
#     exit()


root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)

root.mainloop()


"""
References:
https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV (Ttinker tutorial)
https://docs.python.org/3/library/tkinter.html
https://www.geeksforgeeks.org/python-tkinter-tutorial/
https://gitpress.io/u/1155/tkinter-example-arrow_keys
"""
