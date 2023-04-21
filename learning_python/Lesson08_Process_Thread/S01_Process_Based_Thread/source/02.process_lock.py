import os
from multiprocessing import Process, Lock
import time
from random import random


# the function which the child process will run
def run_proc(lock, name, sleep_sec=0.5):
    # here we use a context to replace acuqire and release. it's equivalent to lock.acquire()... lock.release()
    with lock:
        print('Run child process %s (%s)...' % (name, os.getpid()))
        time.sleep(sleep_sec)
        print(f"{name} Finish sleeping")


def main():
    # create the shared lock
    lock = Lock()
    # create a number of processes with different sleep times
    processes = [Process(target=run_proc, args=(lock, i,)) for i in range(10)]
    # start the processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    finish_time = time.perf_counter()

    print(f"Program finished in {(finish_time - start_time):.3f} seconds")
