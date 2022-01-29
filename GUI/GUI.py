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
import sys # for exit w esc
from backend.objects import *
from backend.roster import *
# import backend.objects
# import backend.roster

# Test this list, then test sample file, then test through backened pull

# exRandomList = ["AA", "AB", "AC", "AD"]
#listIndex will keep track of which student the user currently has selected
file_error = -1
listIndex = 0

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

def importAction(event=None):
    '''Obtain a user-selected file for import'''
    rosterFile = filedialog.askopenfilename()
    print("Selected: ", rosterFile)
    filename=os.path.basename(rosterFile)
    print("filename: ", filename)
    return filename

# def exportAction(event = None):
#     '''Save current roster data to a new text file'''
#     newRosterFile = filedialog.askdirectory()
#     explamefileasdas.write(os.path.join(newRosterFile, 'test.txt'))

def testAction(event=None):
    '''Tests equal distribution of calls'''
    global StudentList
    global DockList
    for n in range(0, 100):
        dockInd = random.randint(0, 3)
        isFlag = random.randint(0, 1)
        DockList , StudentList = deck(StudentList, DockList, dockInd, isFlag)
        print(n)
        update_button()
    print("done")

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
    global StudentList
    global file_error
    global DockList
    if file_error == 1:
        root.destroy()
        sys.exit()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
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
root.geometry("900x100+300+850")
root.minsize(900,100)
root.maxsize(900,100)


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
    command=root.destroy,
)
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

file_exists = os.path.exists("Samplefile.txt")
file_exists2 = os.path.exists("/records/config.txt")
if (file_exists == False and file_exists2 == False):
    file_error = 1
    lbl1 = Label(root, text = "No roster file found please import file type of .xlsx into this directory and restart program", font = ("Arial",15))
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.bind('<Escape>', exitWindow)
    root.mainloop()

else:


    #This is grabbing from roster file!! kewl :))
    #Right now roster can only find from same directory that GUI.py is in, may need to fix that
    #StudentList is now a list that contains a bunch of objects with all the information about a particular student
    Check = start_file("log.txt")
    if  Check == True:
        #print("hello")
        StudentList = Roster(True)
    else:
        StudentList = Roster(False)

    #This will save the date the program is run into
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
