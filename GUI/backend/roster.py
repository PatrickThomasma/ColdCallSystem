"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/14/2022
"""
#if you run this file first it will say no module named backend, just remove it for testing purposes since backend.objects is needed for the GUI.py file import
from backend.objects import Student, Queue
import os
import sys
import random
from datetime import date

def Roster():
    deck = Queue()
    StudentList = []
    AddStudent=[]
    #function here will open file 
    with open(os.path.join(sys.path[0], "Samplefile.txt") , "r") as f:
        f = f.readlines()
        for line in f:
            #Appending each student and their info to a list
            split_line=line.strip().split()
            AddStudent.append(split_line)
        #shuffling the list of student info
        random.shuffle(AddStudent)
        for i in range(0, len(AddStudent)):
            StudentList.append(Student(AddStudent[i][0],AddStudent[i][1],AddStudent[i][2],AddStudent[i][3],AddStudent[i][4],AddStudent[i][5],AddStudent[i][6],0))
            deck.enqueue(AddStudent[i][0]+' '+AddStudent[i][1])
    return StudentList

def deck(roster):
    for i in range(4):
        deck.enqueue(new_roster[i])
    return deck

def save_roster(filepath, Student, flagged):
    with open(filepath, "a") as roster:
        output = "{} {} ({}) was called {} times.".format(Student.first, Student.last,Student.email, Student.times_called)
        if flagged:
            output += "Student was also flagged a total of {} times".format(student.flag)
        output += "\n"
        log.write(output)
        #We will save roster informaiton here with times called and how many times are student was flagged


def start_file(filepath):
    with open(filepath, "a") as log:
        output = "----------------\nCold Call app opened on {}\n".format(date.today())
        log.write(output)
    #This will log the dates then information from save roster will come after

def main():
    StudentList = Roster() 
    return

if __name__ == "__main__":
    main()
