"""
Our algorithm for picking a cold deck queue

This file will import from a student class that will initialize student and Queue Objects

Author: Patrick Thomasma
Last modified: 01/14/2022
"""

from backend.objects import Student, Queue

def Roster():
    Roster = Queue()
    roster_file=open("roster.txt","r")
    for line in roster_file:
	student=line.strip()
    	Roster.enqueue(student)
    """Roster = Queue()
    Student1 = ....
    Student2 = ....
    Student3 = .....
    Student4 = ......
    Student5 = .......
    Roster.enqueue(student1)
    Roster.enqueue(student2)
    Roster.enqueue(student3)
    Roster.enqueue(student4)
    Roster.enqueue(student5)"""
    return Roster

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

"""def pickstudent(ondeck,roster):
    if deck > 4:
        "Error Handling"
        return 0

def pickstudent(ondeck, roster):
    new_roster=random.shuffle(roster)
    return new_roster[0]"""
