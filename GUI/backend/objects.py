"""
This file will initialize the student and Queue from an input file that has a list of Students and their ID numbers

Author: Patrick Thomasma
Last modified: 01/16/2022
"""

class Student:
    def __init__(self,first,last,ID,email,phoneticSpelling,revealCode,LF):
        self.first = first
        self.last = last
        self.ID = ID
        self.email = email
        self.phonetic = phoneticSpelling
        self.reveal = revealCode
        self.LF = LF

    def printstudent(self):
        print("Student:",self.first, self.last, "ID:", self.ID)


class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def enqueue(self , newstudent):
        #This will enqueue our students into the queue
        self.queue.append(newstudent)
        self.length += 1
    def dequeue(self):
        #This will remove a student from the queue
        if self.length > 0:
            element = self.queue.pop(0)
            self.length -= 1
            return element
    def isEmpty(self):
        #This will check if our Queue has any students
        if self.length == 0:
            return True
        return False

    def printQueue(self):
        #This will be our printing method for our queue/debugging
        if len(self.queue) == 0:
            print ("Queue Empty")
        else:
            print("Queue length is ", self.length)
            for i in range(self.length):
                print("Queue at place", i, "has", end = " ")
                self.queue[i].printstudent()



student1 = Student("Patrick", "Thomasma", 951623133, "pthomasm@uoregon.edu", "Pat-T-rick", [], 0)
student2 = Student("Athony", "Hornoff", 23131142, "noff@uoregon.edu", "hor-noff", [], 0)
student3 = Student("David", "Han", 95172932, "dhan@uoregon.edu", "Day-vid", [],0)
student4 = Student("Kassandra", "Morano", "95321421", "Kmoranda@uoregon.edu", "Kass-an-dra", [],0)

test = Queue()
test.enqueue(student1)
test.enqueue(student2)
test.enqueue(student3)
test.enqueue(student4)

test.printQueue()
pop = test.dequeue()
pop.printstudent()
test.enqueue(pop)
test.printQueue()

