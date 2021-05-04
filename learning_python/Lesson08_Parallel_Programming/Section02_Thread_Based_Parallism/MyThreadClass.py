import time
import os
from threading import Thread


# This class extends Thread class. It shows how to do inheritance in python OOP, which is the ability to
# define a new class as a modified version of an already existing class. The main advantage of
# inheritance is that you can add or override new methods to a class without having to change the
# original definition.
class MyThreadClass(Thread):
    # The init method is the constructor of the MyThreadClass
    def __init__(self, name, duration):
        # Call the constructor of its super class(Thread)
        Thread.__init__(self)
        # assign values to class parameter
        self.name = name
        self.duration = duration

    # The run method must be rewritten, which is the logic that the thread will run.
    def run(self):
        print("---> " + self.name + \
              " running, belonging to process ID " \
              + str(os.getpid()) + "\n")
        time.sleep(self.duration)
        print("---> " + self.name + " over\n")
