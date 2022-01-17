"""
This will be the main GUI for students

Author: Patrick Thomasma
Last Modified: 01/14/2022

If on Linux Ubuntu use sudo apt-get install python3-tk for tkinter Module
"""
from tkinter import *


#Runs the window
root = Tk()
#This is the stuff that stuff will appear on?
MyLabel = Label (root, text = "Hello World!")
MyLabel.pack()


root.mainloop()


"""
References:
https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV (Ttinker tutorial)
https://docs.python.org/3/library/tkinter.html
https://www.geeksforgeeks.org/python-tkinter-tutorial/
