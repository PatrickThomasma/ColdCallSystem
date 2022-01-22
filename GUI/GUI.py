"""
This will be the main GUI for students

Author: Patrick Thomasma, David Han
Last Modified: 01/14/2022

If on Linux Ubuntu use sudo apt-get install python3-tk for tkinter Module
"""
from tkinter import *
import os
from backend.objects import *
from backend.roster import *

# Test this list, then test sample file, then test through backened pull

# exRandomList = ["AA", "AB", "AC", "AD"]
#listIndex will keep track of which student the user currently has selected
listIndex = 0

#Runs the window

# def toggleStudent(n):
#     toggle = Label(root, text=studentList[n])
#     toggle.pack()

#Realised that we needed to update the buttons after they're removed so it was made into its own function instead of making up/down large functions
def update_button():
    global listIndex
    global buttons
    global StudentList
    global DockList
    for i in range(4):
        buttons[i].config({"text": DockList[i]})


#Working up function but methods are kind of messy and obviously not finalized since its using a test version of FILE I/O
def upKey(event):
    global listIndex
    global StudentList
    #global flags
    global DockList
    global remover
    current_student = DockList[listIndex]
    removed = DockList.pop(listIndex)
    remover += 1
    DockList.append(StudentList[remover])
    #flags[listIndex] += 1
    update_button()

#Not implemented yet
def downKey(event):
    global listIndex
    global buttons
    global StudentList
    global DockList
    global remover
    current_student = DockList[listIndex]
    removed = DockList.pop(listIndex)
    remover += 1
    DockList.append(StudentList[remover])
    update_button()


def leftKey(event): #update list Index and color slots so its consistent with each key press
    global listIndex
    global buttons
    if listIndex == 0:
        return
    buttons[listIndex].config({"background": "Blue"})
    buttons[listIndex].config({"foreground": "White"})
    listIndex -= 1
    buttons[listIndex].config({"background": "White"})
    buttons[listIndex].config({"foreground": "Black"})

def rightKey(event): #update list index until it hits the end of the list, keep coloring of buttons consistent with other key presses
    global listIndex
    global buttons
    if listIndex == 3:
        return
    buttons[listIndex].config({"background": "Blue"}) #configs will highlight selected button and change it back when user moves on from the button
    buttons[listIndex].config({"foreground": "White"})
    listIndex += 1
    buttons[listIndex].config({"background": "White"})
    buttons[listIndex].config({"foreground": "Black"})
'''
StudentList = []
flags = []
#opening our file then using for loop to grab information that we want current
#unsure how DuckID and email will fit into it but we can add more later
with open(os.path.join(sys.path[0], "Samplefile.txt"), "r") as f:
        f = f.readlines()
        for i in range (0, len(f)):
            studentclass = f[i].split()
            StudentList.append(studentclass[0] + ' ' + studentclass[1])
            flags.append(int(studentclass[len(f)]))
'''
#This is grabbing from roster file!! kewl :))
#Right now roster can only find from same directory that GUI.py is in, may need to fix that
StudentList = Roster()
DockList = []
for i in range(len(StudentList)):
    DockList.append(StudentList[i].first + ' ' + StudentList[i].last)
remover = 3
root = Tk()
root.geometry("900x100+300+850")
root.minsize(900,100)
root.maxsize(900,100)
root.title("Cold Call")
root.attributes("-topmost", True)

myLabel1 = Label(root, text= "Student Dock" , font=("Arial", 20))
myLabel1.grid(row = 0, column = 1, padx = 5, pady = 5)

##myLabel2 = Label(root, text=studentList[1], font=("Arial", 20))
##myLabel2.grid(row=0, column=1)

##myLabel3 = Label(root, text=studentList[2], font=("Arial", 20))
##myLabel3.grid(row=0, column=2)

##myLabel4 = Label(root, text=studentList[3], font=("Arial", 20))
##myLabel4.grid(row=0, column=3)

# from my understanding of the project we will only need 4 buttons as those are the students who will be displayed in the cold call

#Should change the background color here maybe? He specifies how the coloring should look a little bit on SRS
button0 = Label(root, text = DockList[0], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
button0.grid(row = 1, column = 1, padx = 5, pady = 5)

button1 = Label(root, text = DockList[1], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
button1.grid(row = 1, column = 2, padx = 5, pady = 5)

button2 = Label(root, text = DockList[2], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
button2.grid(row = 1, column = 3, padx = 5, pady = 5)

button3 = Label(root, text = DockList[3], bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
button3.grid(row = 1, column = 4, padx = 5, pady = 5)

buttons = [button0,button1,button2,button3]
#Right now the program has the first position highlighted but after reading SRS it should be dependent on whether the instructor presses left or right first, have to fix that
button0.config({"background": "White"})
button0.config({"foreground": "Black"})

# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "DA")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

# myLabel.pack()

# if key == Key.backspace:
#     exit()

#These functions will bind the functions to keyboard and is main control for user
root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)
root.bind("<Up>",upKey)
root.bind("<Down>",downKey)

root.mainloop()


"""
References:
https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV (Ttinker tutorial)
https://docs.python.org/3/library/tkinter.html
https://www.geeksforgeeks.org/python-tkinter-tutorial/
https://gitpress.io/u/1155/tkinter-example-arrow_keys
"""
