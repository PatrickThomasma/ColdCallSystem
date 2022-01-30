"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/25/2022
"""
#if you run this file first it will say no module named backend, just remove it for testing purposes since backend.objects is needed for the GUI.py file import
# from backend.objects import Student, Queue
from .objects import Student, Queue
# import objects
# from objects import Student, Queue

import os.path
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ..GUI

import random
from datetime import date
# import numpy as np
# from datascience import *

times_limit = 1
delimVar = ","

def Roster(exists):
    #Exists will choose difference between if a user has put a new roster file in or if there's already a config file from a previous use
    print("Does it exist?" ,exists)
    StudentList = []
    AddStudent=[]
    #function here will open file 
    #Have to change filename to a path maybe?
    if exists == False:
        # with open(os.path.join(sys.path[0], importAction()) , "r") as f:
        with open(os.path.join(sys.path[0], "Samplefile.csv") , "r") as f:
        #with open(os.path.join(sys.path[0], filename) , "r") as f:
            f = f.readlines()
            for line in f:
                #Appending each student and their info to a list
                split_line=line.strip().split(delimVar)
                AddStudent.append(split_line)
            #shuffling the list of student info
            random.shuffle(AddStudent)
            #This will add all the information into StudentList
            for i in range(0, len(AddStudent)):
                StudentList.append(Student(AddStudent[i][0],AddStudent[i][1],AddStudent[i][2],AddStudent[i][3],AddStudent[i][4],AddStudent[i][5],AddStudent[i][6], False , 0, 0, 0))

        #StudentList.sort(key = lambda x: x.last)
        #for i in range (0,len(StudentList)):
            #print(StudentList[i].first + " " + StudentList[i].last)
        #sys.exit()
        return StudentList
    #This will do the asame thing as the above code block except will search for the configuration file instead and process that
    if exists == True:
        full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"../config")
        #file_location = os.path.join(full_path, "config.txt")
        #print(file_location)
        with open(os.path.join(full_path, "config.txt"),  "r") as f:
            #print(f.readline())
            f = f.readlines()
            for line in f:
                split_line = line.strip().split()
                AddStudent.append(split_line)
            random.shuffle(AddStudent)
            for i in range(0, len(AddStudent)):
                StudentList.append(Student(AddStudent[i][0], AddStudent[i][1], AddStudent[i][2], AddStudent[i][3], AddStudent[i][4], AddStudent[i][5], AddStudent[i][6], False, int(AddStudent[i][7]), int(AddStudent[i][8]), int(AddStudent[i][9])))
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
    #random.shuffle(StudentList)
    global times_limit
    if (len(deckList) == 4): #When deck is full we just have to pop whatever index has been sent in then do the same as the for loop below
        current_student = deckList.pop(listIndex) #since deck is full we're going to pop whoever was called
        if (ind == 1):
            current_student.flag_count += 1 #Update the students flag then put them back into StudentList
            current_student.flags = True
#Update the current_student who has just been popped and update their information for the summary and any other information
        current_student.times_called += 1
        current_student.total_called += 1
        StudentList.append(current_student)
        for i in range (0, len(StudentList)):
#Loop through StudentList to find someone that doesn't have a flag and add them back into Deck
            #print("value of i " , len(deckList))
            if (StudentList[i].times_called < times_limit):
                deckList.append(StudentList[i])
                StudentList.pop(i)
                return deckList, StudentList
#When everyone who is not on deck has been called we will update the limit so now everyone has a chance of being called again and then append one of those students onto the deck
        times_limit += 1
        deckList.append(StudentList[0])
        StudentList.pop(0)
        return deckList,StudentList

#When everyone has been called hits times_limit we update times_limit so everyone now has
# an equal chance of being called again
# If everyone has been called then we just push the first person in the StudentList into deck and pop them out of StudentList
#Note: People on deck haven't been called as of yet 

    for i in range(0,4): #This will add people to our deck and add them to the back of the studentList
        #print(StudentList)
        deckList.append(StudentList[i])
        StudentList.pop(i)
    #This will return decklist into GUI for example 
    #deckList = [Patrick Thomasma, Kassandra morando, David han, briana vago]
    return deckList , StudentList

def save_roster(filepath, StudentList, deckList):

    global delimVar

    print(deckList)
    for i in range (0, len(deckList)):
        StudentList.append(deckList[i])
        #deckList.pop()
#Here we are saving three different information files, Log will be first and tell the user when the GUI was run and who was flagged during that instance
    StudentList.sort(key = lambda x: x.last)
    #The log file is saved into the config record, fullerpath will be for the summary review
    full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../config")
    fuller_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../records")
    completename = os.path.join(full_path , "log.txt")
    with open(completename , "a") as roster:
        for Student in StudentList:
            if Student.flags == True:
                output = "{} {} {}  ({})".format(" X " , Student.first, Student.last,Student.email)
                output += "\n"
                roster.write(output)
            else:
                output = "{} {} {} ({})".format("   ", Student.first, Student.last,Student.email)
                output += "\n"
                roster.write(output)
        roster.close()
    #start_file("SummaryPerformance.txt", 1)
    if not os.path.exists(fuller_path):
        os.mkdir(fuller_path)
#Here is the summary review which will be overwritten after every use and update the values for Students
    summaryname = os.path.join(fuller_path, filepath)
    with open(summaryname, "w") as summary:
        for Student in StudentList:
#Student will grab information from one index of StudentList then go into output file
            # output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(Student.times_called, Student.flag_count,Student.first,Student.last, Student.ID, Student.email, Student.phonetic, Student.reveal, date.today())
            output = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(Student.times_called, delimVar, Student.flag_count, delimVar, Student.first, delimVar, Student.last, delimVar, Student.ID, delimVar, Student.email, delimVar, Student.phonetic, delimVar, Student.reveal, delimVar, date.today())
            output += "\n"
            summary.write(output)
            
        #sys.exit("List is done")
        summary.close()
    configname = os.path.join(full_path, "config.txt")
#Configuration is the file we are searching for for when the instructor wants to use the program again with the same roster of students and it will keep track if the student was called during the last use
    with open(configname, "w") as config:
        for Student in StudentList:
#Since the time limit will be reset after everytime the program is used we will decrement everyone who has been called to 1 and everyone who hasn't been called yet to 0 
            if Student.times_called == times_limit:
                Student.times_called = 1
                print(Student.total_called)
            elif Student.times_called < times_limit:
                Student.times_called = 0
            output = "{} {} {} {} {} {} {} {} {} {}".format(Student.first, Student.last, Student.ID, Student.email, Student.phonetic, Student.reveal, Student.LF,Student.times_called, Student.flag_count, Student.total_called)
            output += "\n"
            config.write(output)
        config.close()
    return
    
        #We will save roster informaiton here with times called and how many times are student was flagged

'''TEST FILE CREATE HERE'''

def save_testRoster(filepath, StudentList, deckList):

    global delimVar

    print(deckList)
    for i in range (0, len(deckList)):
        StudentList.append(deckList[i])
        #deckList.pop()
#Here we are saving three different information files, Log will be first and tell the user when the GUI was run and who was flagged during that instance
    StudentList.sort(key = lambda x: x.last)
    #The log file is saved into the config record, fullerpath will be for the summary review
    full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../config")
    fuller_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../records")
    completename = os.path.join(full_path , "log.txt")
    with open(completename , "a") as roster:
        for Student in StudentList:
            if Student.flags == True:
                output = "{} {} {}  ({})".format(" X " , Student.first, Student.last,Student.email)
                output += "\n"
                roster.write(output)
            else:
                output = "{} {} {} ({})".format("   ", Student.first, Student.last,Student.email)
                output += "\n"
                roster.write(output)
        roster.close()
    #start_file("SummaryPerformance.txt", 1)
    if not os.path.exists(fuller_path):
        os.mkdir(fuller_path)
#Here is the summary review which will be overwritten after every use and update the values for Students
    summaryname = os.path.join(fuller_path, filepath)
    with open(summaryname, "w") as summary:
        for Student in StudentList:
#Student will grab information from one index of StudentList then go into output file
            # output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(Student.times_called, Student.flag_count,Student.first,Student.last, Student.ID, Student.email, Student.phonetic, Student.reveal, date.today())
            output = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(Student.times_called, delimVar, Student.flag_count, delimVar, Student.first, delimVar, Student.last, delimVar, Student.ID, delimVar, Student.email, delimVar, Student.phonetic, delimVar, Student.reveal, delimVar, date.today())
            output += "\n"
            summary.write(output)
            
        #sys.exit("List is done")
        summary.close()
    configname = os.path.join(full_path, "config_TEST.txt")
#Configuration is the file we are searching for for when the instructor wants to use the program again with the same roster of students and it will keep track if the student was called during the last use
    with open(configname, "w") as config:
        for Student in StudentList:
#Since the time limit will be reset after everytime the program is used we will decrement everyone who has been called to 1 and everyone who hasn't been called yet to 0 
            if Student.times_called == times_limit:
                Student.times_called = 1
                print(Student.total_called)
            elif Student.times_called < times_limit:
                Student.times_called = 0
            output = "{} {} {} {} {} {} {} {} {} {}".format(Student.first, Student.last, Student.ID, Student.email, Student.phonetic, Student.reveal, Student.LF,Student.times_called, Student.flag_count, Student.total_called)
            output += "\n"
            config.write(output)
        config.close()
    return


'''TEST FILE CREATE ENDS HERE'''


def start_file(filepath):
#When we start the file we will search if there's a log file and a config file, If there's a log its simple we just append to it, if there isn't a log file we will create the directory for it and just write into the new empty file
    full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../config")
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        file_location = os.path.join(full_path,'log.txt')
        with open(file_location, "a") as log:
            output = "----------------\nCold Call app opened on {}\n".format(date.today())
            log.write(output)
    else:
        file_location = os.path.join (full_path, 'log.txt')
        with open(file_location, "a") as log:
            output = "----------------\nCold Call app opened on {}\n".format(date.today())
            log.write(output)

    file_exists = os.path.exists("config/config.txt")
    #print(file_exists)
#If a config file exists we will return True to the front end so we know that there's already information stored and we will use that instead of the roster file that was given by the user
    if file_exists == True:
        #Roster(True)
        return True
    else:
        return False
    

    return
    #This will log the dates then information from save roster will come after

#def main():
#    StudentList = Roster() 
#    return

#if __name__ == "__main__":
#    main()
