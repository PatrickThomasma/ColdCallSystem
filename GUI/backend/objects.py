"""
This file will initialize the student and Queue from an input file that has a list of Students and their ID numbers
Author: Patrick Thomasma, Kassandra Morando
Last modified: 01/25/2022
"""

class Student:
#All information from the roster file is stored here, some values will be 0 if its a new roster file but some of them will already have values if we're continuing from previous iteration
    def __init__(self,first,last,ID,email,phoneticSpelling,revealCode,LF,flags, times_called,flag_count, total_called):
        self.first = first
        self.last = last
        self.ID = ID
        self.email = email
        self.phonetic = phoneticSpelling
        self.reveal = revealCode
        self.LF = LF
        self.flags = flags
        self.times_called = times_called
        self.flag_count = flag_count
        self.total_called = total_called

    def student_display(self):
        return (self.first, self.last)

    def printstudent(self):
        print("Student:\t",self.first, self.last, "ID:\t", self.ID,"Email adress:\t",self.email,"Phonetic_spelling:\t",self.phonetic,"Reveal code:",self.reveal,"LF:",self.LF)



#Queue class will have us keep track of who is in queue and who is to be popped out next
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
                print("Queue at place", i, "has", end = "@")
                self.queue[i].printstudent()


'''
student1 = Student("Patrick", "Thomasma", 951623133, "pthomasm@uoregon.edu", "Pat-T-rick", [], 0)
student2 = Student("Athony", "Hornoff", 23131142, "noff@uoregon.edu", "hor-noff", [], 0)
student3 = Student("David", "Han", 95172932, "dhan@uoregon.edu", "Day-vid", [],0)
student4 = Student("Kassandra", "Morando", "95321421", "Kmorando@uoregon.edu", "Kass-an-dra", [],0)
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
'''
