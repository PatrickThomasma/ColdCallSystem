"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/14/2022
"""

from objects import Student, Queue , Roster
import os
import sys

def Roster():
    deck = Queue()
    StudentList = []
    with open(os.path.join(sys.path[0], "Samplefile.txt") , "r") as f:
        f = f.readlines()
        for i in range (0 , len(f)):
            #StudentList.append(f)
            studentclass = f[i].split()
            StudentList.append(Student(studentclass[0],studentclass[1],studentclass[2],studentclass[3],studentclass[4],studentclass[5],studentclass[6]))
            deck.enqueue(studentclass[0] + ' ' + studentclass[1])

    print(StudentList[0].printstudent())

def deck(roster):
    deck = Queue()
    new_roster=random.shuffle(roster)
    if new_roster==roster:
        new_roster=random.shuffle(new_roster)
    for i in range(4):
        deck.enqueue(new_roster[i])
    return deck

def save_roster():
    #Saves the order of roster when application is closed
    pass

def summary_file():
    #See how many times people paricipated,etc.
    pass

def main():
    Roster()
    return

if __name__ == "__main__":
    main()
