import threading
import time
from learning_python.Lesson08_Parallel_Programming.Section02_Thread_Based_Parallism.MyThreadClass import MyThreadClass
from random import randint

"############################# 2.1 Defining a thread ####################################################"

"""
The Python threading module provides a Thread class that is used to run processes and functions in a different thread:

class threading.Thread(group=None,
                       target=None,
                       name=None,
                       args=(),
                       kwargs={})

Here are the parameters of the Thread class:
- group : This is the group value, which should be None ; this is reserved for future implementations.
- target : This is the function that is to be executed when you start a thread activity.
- name : This is the name of the thread; by default, a unique name of the form of Thread-N is assigned to it.
- args : This is the tuple of arguments that are to be passed to a target.
- kwargs : This is the dictionary of keyword arguments that are to be used for the target function.

"""


def my_func(thread_number: str):
    return print("my_func() called by thread No-{}".format(thread_number))


def exp1_defining_thread():
    # empty list for hosting created thread
    my_thread_list = []
    for i in range(10):
        # create a new thread by using class Thread of package threading
        t = threading.Thread(target=my_func, args=(i,))
        # register thread to the list
        my_thread_list.append(t)
        # start a thread
        t.start()
        # make the calling(main->exp1) thread wait the thread to finish, otherwise, main can finish before child thread.
        t.join()


"############################# 2.2 Determine the current thread ####################################################"


def func_a():
    # get the name of thread which calls this function
    name = threading.currentThread().getName()
    print(name + str("--> starting"))
    time.sleep(2)
    print(name + str("--> ending"))


def func_b():
    name = threading.currentThread().getName()
    print(name + str("--> starting"))
    time.sleep(2)
    print(name + str("--> ending"))


def func_c():
    name = threading.currentThread().getName()
    print(name + str("--> starting"))
    time.sleep(2)
    print(name + str("--> ending"))


def exp2_get_current_thread_name():
    # create three thread, each one calls a function. start the threads, and wait them to finish
    t1 = threading.Thread(target=func_a, name="func_a")
    t2 = threading.Thread(target=func_b, name="func_b")
    t3 = threading.Thread(target=func_c, name="func_c")
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


"############################# 2.3 Define a thread subclass ####################################################"

""" 
We have defined a subclass of thread in MyThreadClass.py. You can find the details in that file. Here, we just call
them to create new MyThreadClass instance 
"""


def exp3_defining_thread_subclass():
    start_time = time.time()
    my_thread_list = []
    for i in range(10):
        # create a thread by using my custom thread class which is a subclass of threading.Thread
        t = MyThreadClass("Thread #{}".format(i), randint(1, 10))
        my_thread_list.append(t)
        t.start()
    # need to do join in another loop, otherwise, the second thread has to wait first thread to finish to start
    for t in my_thread_list:
        t.join()
    # End
    print("End")
    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


def main():
    # run example 1
    # exp1_defining_thread()

    # run example 2
    # exp2_get_current_thread_name()

    # run example 3
    exp3_defining_thread_subclass()


if __name__ == "__main__":
    main()
