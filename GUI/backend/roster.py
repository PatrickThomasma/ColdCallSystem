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
            #deck.enqueue(AddStudent[i][0]+' '+AddStudent[i][1])
    return StudentList

def deck(StudentList, deckList, listIndex):
    random.shuffle(StudentList)
    counter = 0
    for i in range (0, len(StudentList)):
        counter += 1
        print(StudentList[i].first + ' ' + StudentList[i].last + ' Counter: ' + str(counter))
    if (len(deckList) == 4): #When deck is full we just have to pop whatever index has been sent in then do the same as the for loop below
        current_student = deckList.pop(listIndex) #since deck is full we're going to pop whoever was called
        current_student.flags += 1
        StudentList.append(current_student)
        print("Length", len(StudentList))
        print("Student who is popped then back in: ", current_student.first , " " , current_student.flags)
        #StudentList.append(current_student) #Then add them back into studentList
        for i in range (0, len(StudentList)):
#Loop through StudentList to find someone that doesn't have a flag and add them back into Deck
            if (StudentList[i].flags < 1):
                #print(StudentList[i].first + ' ' + StudentList[i].last + ' ' + str(StudentList[i].flags))
                deckList.append(StudentList[i])
                StudentList.pop(i)
                #print(StudentList[i].first + ' ' + StudentList[i].last + ' ' + str(StudentList[i].flags))
                return deckList, StudentList
#So right now once everyone has been called the program should shut down
#At this point instead of exiting its time to handle next iteration of program assuming its still being is use
        for j in range (0, len(StudentList)):
            print(StudentList[j].flags)
        sys.exit("List is complete")
    for i in range(0,4): #This will add people to our deck and add them to the back of the studentList
        deckList.append(StudentList[i])
        StudentList.pop(i)
    #This will return decklist into GUI for example 
    #deckList = [Patrick Thomasma, Kassandra morando, David han, briana vago]
    return deckList , StudentList

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

#def main():
#    StudentList = Roster() 
#    return

#if __name__ == "__main__":
#    main()
