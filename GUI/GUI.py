"""
This will be the main GUI for students

Author: Patrick Thomasma, David Han, Geli Zhang
Last Modified: 01/27/2022

If on Linux Ubuntu use sudo apt-get install python3-tk for tkinter Module
If using mac terminal, pip3 --version, pip3 install --upgrade pip, pip3 install tk
"""
# from asyncore import file_dispatcher
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from os.path import exists
import time
import sys
from unittest import TestCase # for exit w esc
from backend.objects import *
from backend.roster import *
# import backend.objects
# import backend.roster

from shutil import copy2

# Test this list, then test sample file, then test through backened pull

# exRandomList = ["AA", "AB", "AC", "AD"]
#listIndex will keep track of which student the user currently has selected
file_error = -1
listIndex = 0

testCheck = 0

#Runs the window

# def toggleStudent(n):
#     toggle = Label(root, text=studentList[n])
#     toggle.pack()

#Realised that we needed to update the buttons after they're removed so it was made into its own function instead of making up/down large functions
def update_button():
    global buttons
    global DockList
    #Update whos in the queue for the users view on the next run
    for i in range(4):
        buttons[i].config({"text": DockList[i].first + ' ' + DockList[i].last})


# importedFileDir = None
# importedFileName = None
def importAction(event=None):
    '''Obtain a user-selected file for import'''
    root.withdraw()
    rosterFile = filedialog.askopenfilename()
    fileLoc = filedialog.askdirectory()
    filename = os.path.basename(rosterFile)
    if (rosterFile == 'Samplefile.csv'):
        if messabox.askokcancel("Test", "This will overwrite current Roster file, do you wish to proceed?"):
            copy2(rosterFile, fileLoc, follow_symlinks=True)
            root.deiconify()
    else:
        copy2(rosterFile, fileLoc, follow_symlinks=True)
        root.deiconify()

    # print("Selected: ", rosterFile)
    # importedFileDir = rosterFile
    # filename=os.path.basename(rosterFile)
    # # print("filename: ", filename)
    # immportedFileName = filename
    # # return filename
    # print(importedFileDir)
    # print(importedFileName)

# def exportAction(event = None):
#     '''Save current roster data to a new text file'''
#     newRosterFile = filedialog.askdirectory()
#     explamefileasdas.write(os.path.join(newRosterFile, 'test.txt'))

def testAction(event=None):
    '''Tests equal distribution of calls'''
    global StudentList
    global DockList
    
    global testCheck

    StudentList = Roster(False)

    if messagebox.askokcancel("Test", "Are you sure about that, output files might be overwritten?"):
        for n in range(0, 100):
            dockInd = random.randint(0, 3)
            isFlag = random.randint(0, 1)
            # DockList , StudentList = deck(StudentList, DockList, dockInd, isFlag)
            DockList , StudentList = deck(StudentList, DockList, dockInd, isFlag)
            #print(n)
            update_button()
    print("done")
    testCheck = 1
    on_closing()
    #have this make its own configs

#Working up function but methods are kind of messy and obviously not finalized since its using a test version of FILE I/O
def upKey(event):
    global StudentList
    global listIndex
    global DockList
    #With deck now full this function will instead remove the student, update flag, then return an update DockList and StudentList
    DockList , StudentList = deck(StudentList, DockList, listIndex , 1)
    #the next person's name will appear after a delay of 1s
    # time.sleep(1)
    update_button()

#Not implemented yet
def downKey(event):
    global listIndex
    global StudentList
    global DockList
    #Same as the upkey except the flags are not updated
    DockList, StudentList = deck(StudentList, DockList, listIndex, 0)
    #the next person's name will appear after a delay of 1s
    # time.sleep(1)
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

def exitWindow(event):
#This function is when the user clicks on the red X on the window, file_error is called into if there's not file in the directory and we will have the user restart so they can run the program again with the file hopefully in the location
    global StudentList
    global file_error
    global DockList
    if file_error == 1:
        root.destroy()
        sys.exit()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        save_roster("SummaryPerformance.txt", StudentList, DockList)
        root.destroy()
    #sys.exit()


def on_closing():
#This is when the user clicks the escape button and it will close the same way as the exitWindow
    global StudentList
    global file_error
    global DockList

    global testCheck

    if file_error == 1:
        root.destroy()
        sys.exit()

    print("Testcheck flag: ", testCheck)
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        if testCheck == 1:
            save_testRoster("SummaryPerformance_TEST.txt", StudentList, DockList)
        else:
            save_roster("SummaryPerformance.txt", StudentList, DockList)
        root.destroy()

def flag(event): 
    global listIndex
    global StudentList
    global DockList
    #Same as Up function but just different Keys
    DockList, StudentList = deck(StudentList,DockList, listIndex, 1)
    update_button()

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

root = Tk()
# root.geometry("900x100+300+850")
root.geometry("900x110+300+0")
root.minsize(900,110)
root.maxsize(900,110)


'''Menu Setup'''
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(
    label='Import Roster',
    command=lambda:importAction(),
)

file_menu.add_command(
    label='Test',
    command=lambda:testAction(),
)
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    # command=root.destroy,
    command=lambda:on_closing(),
)   
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

file_exists = os.path.exists("Samplefile.txt")
file_exists2 = os.path.exists("/config/config.txt")
if (file_exists == False and file_exists2 == False):
#If the program is not able to find a roster file in the directories than we will inform the user about it and give them a chance to import a file and restart the program 
    file_error = 1
    lbl1 = Label(root, text = "No roster file found please import file type of .csv into this directory and restart program", font = ("Arial",15))
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)
#GUI will stop here and user will have to exit program and restart to use a roster file

    root.bind('<Escape>', exitWindow)
    root.mainloop()

else:


    #We will go into start_file and check if a config file is there or not
    Check = start_file("log.txt")
    if  Check == True:
#If there is a config file then we run roster using that file
        #print("hello")
        StudentList = Roster(True)
    else:
#if not then we will use whatever roster file we were given
        StudentList = Roster(False)

    print(file_exists2)

    if file_exists2 == True:
        if os.path.getmtime("Samplefile.csv") > os.path.getmtime("config/config.txt"):
            print("Check")
            StudentList = []
            StudentList = Roster(False)

#Initialize first instance of DockList
    DockList = []
    #Calling deck function in roster.py to get people into cold call system and to remove from front of StudentList and append back into that list
    DockList , StudentList = deck(StudentList, DockList, 0 , 0)


    root.title("Cold Call")
    root.attributes("-topmost", True)
    #All of the root functions here setup the window
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
    button0 = Label(root, text = DockList[0].first + ' ' + DockList[0].last, bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
    button0.grid(row = 1, column = 1, padx = 5, pady = 5)

    button1 = Label(root, text = DockList[1].first + ' ' + DockList[1].last, bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
    button1.grid(row = 1, column = 2, padx = 5, pady = 5)

    button2 = Label(root, text = DockList[2].first + ' ' + DockList[2].last, bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
    button2.grid(row = 1, column = 3, padx = 5, pady = 5)

    button3 = Label(root, text = DockList[3].first + ' ' + DockList[3].last, bg = "Blue", fg = "white", padx = 30, relief = RAISED, width = 10, font = ("Arial",12))
    button3.grid(row = 1, column = 4, padx = 5, pady = 5)
    #All of these will be buttons for the deck
    buttons = [button0,button1,button2,button3]
    #Right now the program has the first position highlighted but after reading SRS it should be dependent on whether the instructor presses left or right first, have to fix that
    button0.config({"background": "White"})
    button0.config({"foreground": "Black"})

# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "DA")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

# myLabel.pack()

#These functions will bind the functions to keyboard and is main control for user
    root.bind("<Left>",leftKey)
    root.bind("<Right>",rightKey)
    root.bind("<Up>",upKey)
    root.bind("<Down>",downKey)
    root.bind("<Q>",flag)
    root.bind("<W>",flag)
    root.bind("<E>",flag)
    root.bind("<R>",flag)
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.bind('<Escape>', exitWindow)
    root.mainloop()


"""
References:
https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV (Ttinker tutorial)
https://docs.python.org/3/library/tkinter.html
https://www.geeksforgeeks.org/python-tkinter-tutorial/
https://gitpress.io/u/1155/tkinter-example-arrow_keys
https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter
"""
