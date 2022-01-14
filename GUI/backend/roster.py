"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/14/2022
"""

from backend.objects import Student, Queue

def Roster():
    Roster = Queue()
    Student1 = ....
    Student2 = ....
    Student3 = .....
    Student4 = ......
    Student5 = .......
    Roster.enqueue(student1)
    Roster.enqueue(student2)
    Roster.enqueue(student3)
    Roster.enqueue(student4)
    Roster.enqueue(student5)
    return roster

def deck(roster):
    deck = Queue()
    for i in range(4):
        pickStudent(deck,roster)

    return deck

def pickstudent(ondeck,roster):
    if deck > 4:
        "Error Handling"
        return 0

