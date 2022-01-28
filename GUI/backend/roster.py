"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/25/2022
"""
#if you run this file first it will say no module named backend, just remove it for testing purposes since backend.objects is needed for the GUI.py file import
from backend.objects import Student, Queue
import os
import sys
import random
from datetime import date
# import numpy as np
# from datascience import *

times_limit = 1

def Roster():
    StudentList = []
    AddStudent=[]
    #function here will open file 
    #Have to change filename to a path maybe?
    with open(os.path.join(sys.path[0], "Samplefile.txt") , "r") as f:
        f = f.readlines()
        for line in f:
            #Appending each student and their info to a list
            split_line=line.strip().split()
            AddStudent.append(split_line)
        #shuffling the list of student info
        random.shuffle(AddStudent)
        #This will add all the information into StudentList
        for i in range(0, len(AddStudent)):
            StudentList.append(Student(AddStudent[i][0],AddStudent[i][1],AddStudent[i][2],AddStudent[i][3],AddStudent[i][4],AddStudent[i][5],AddStudent[i][6],0 , 0))
    return StudentList

    # studentTable=Table.read_table("Samplefile.csv")
    # first= studentTable.column("First Name")
    # last= studentTable.column("Last Name")
    # uoID= studentTable.column("UO ID")
    # email= studentTable.column("Email")
    # phone= studentTable.column("Phoetic Spelling")
    # revealCode= studentTable.column("Reveal Code")
    # lf= studentTable.column("LF")

    # firstName=[]
    # lastName=[]
    # uo_id=[]
    # emailList=[]
    # phonetic=[]
    # rc=[]
    # lfList=[]

    # for i in range(0,len(first)):
    #     firstName.append(first[i])
    #     lastName.append(last[i])
    #     uo_id.append(uoID[i])
    #     emailList.append(email[i])
    #     phonetic.append(phone[i])
    #     rc.append(revealCode[i])
    #     lfList.append(lf[i])

    # StudentList=[]
    # for i in range(0,len(first)):
    #     StudentList.append(Student(firstName[i],lastName[i],uo_id[i],emailList[i],phonetic[i],rc[i],lfList[i],0 , 0))
    # return StudentList

def deck(StudentList, deckList, listIndex, ind):
    random.shuffle(StudentList)
    global times_limit
    if (len(deckList) == 4): #When deck is full we just have to pop whatever index has been sent in then do the same as the for loop below
        current_student = deckList.pop(listIndex) #since deck is full we're going to pop whoever was called
        if (ind == 1):
            current_student.flags += 1 #Update the students flag then put them back into StudentList
        current_student.times_called += 1
        StudentList.append(current_student)
        for i in range (0, len(StudentList)):
#Loop through StudentList to find someone that doesn't have a flag and add them back into Deck
            if (StudentList[i].times_called < times_limit):
                deckList.append(StudentList[i])
                StudentList.pop(i)
                return deckList, StudentList
#So right now once everyone has been called the program should shut down
#At this point instead of exiting its time to handle next iteration of program assuming its still being is use
       
        for j in range (len(StudentList)):
            print(StudentList[j].first + ' ' + StudentList[j].last + ': ' + str(StudentList[j].times_called))
        for k in deckList:
            print(k.first + ' ' + k.last + ' ' + str(k.times_called))

        save_roster("log.txt", StudentList)

    for i in range(0,4): #This will add people to our deck and add them to the back of the studentList
        deckList.append(StudentList[i])
        StudentList.pop(i)
    #This will return decklist into GUI for example 
    #deckList = [Patrick Thomasma, Kassandra morando, David han, briana vago]
    return deckList , StudentList

def save_roster(filepath, StudentList):
    with open(filepath, "a") as roster:
        for Student in StudentList:
            if Student.flags > 0:
                output = "{} {} {}  ({})".format("   " , Student.first, Student.last,Student.email)
            else:
                output = "{} {} {}  ({})".format(" X " , Student.first, Student.last, Student.email)
            output += "\n"
            roster.write(output)
        sys.exit("List is done")
        #We will save roster informaiton here with times called and how many times are student was flagged


def start_file(filepath):
    with open(filepath, "a") as log:
        output = "----------------\nCold Call app opened on {}\n".format(date.today())
        log.write(output)
    #This will log the dates then information from save roster will come after

#def main():
#    StudentList = Roster() 
#    return

#if __name__ == "__main__":
#    main()
