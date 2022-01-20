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
studentList = ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL"]
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

def keyCommands(key):
    if (key == Key.left) & (listIndex > 0):
        # toggle indicator to left
        listIndex -= 1

    if (key == Key.right) & (listIndex < 0):
        # toggle indicator to left
        listIndex -= 1

myLabel1 = Label(root, text=studentList[0], font=("Arial", 20))
myLabel1.grid(row=0, column=0)

myLabel2 = Label(root, text=studentList[1], font=("Arial", 20))
myLabel2.grid(row=0, column=1)

myLabel3 = Label(root, text=studentList[2], font=("Arial", 20))
myLabel3.grid(row=0, column=2)

myLabel4 = Label(root, text=studentList[3], font=("Arial", 20))
myLabel4.grid(row=0, column=3)


# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "DA")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

# myLabel.pack()

# if key == Key.backspace:
#     exit()

root.mainloop()


"""
References:
https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV (Ttinker tutorial)
https://docs.python.org/3/library/tkinter.html
https://www.geeksforgeeks.org/python-tkinter-tutorial/
"""
