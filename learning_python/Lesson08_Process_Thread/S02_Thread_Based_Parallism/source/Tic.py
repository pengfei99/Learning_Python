import os
import time
from threading import Thread


class TicToc(Thread):
    def __init__(self, name, duration, tic, thread_lock):
        # Call the constructor of its super class(Thread)
        Thread.__init__(self)
        # assign values to class parameter
        self.name = name
        self.duration = duration
        self.thread_lock = thread_lock
        self.tic = tic

    def run(self) -> None:
        while True:
            # if tic true then wait until toc complete.
            if self.tic:
                time.sleep(1)
            # if tic is false acquire the lock and start the thread
            else:
                self.thread_lock.acquire()
            print("---> " + self.name + \
                  " running, belonging to process ID " \
                  + str(os.getpid()) + "\n")
            time.sleep(self.duration)
            print("Clock " + self.name + "\n")
            # After the thread finish, Release the Lock
            self.thread_lock.release()
