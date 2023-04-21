import os
from multiprocessing import Process
import time


# the function which the child process will run
def run_proc(name, sleep_sec=0.5):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(sleep_sec)
    print(f"{name} Finish sleeping")


def main():
    # main(parent) process that creates child process
    print('Parent process %s.' % os.getpid())
    # create child process, two important parameter, target specify the function that the child process will run,
    # args is the parameter of the function running in child process
    p1 = Process(target=run_proc, args=('Process1', 2))
    p2 = Process(target=run_proc, args=('Process2', 1))
    p3 = Process(target=run_proc, args=('Process3',))
    print('start child processes')
    # Start the child process
    p1.start()
    p2.start()
    p3.start()
    # tell main process to wait child process termination before running the rest of the code in main process.
    p1.join()
    p2.join()
    p3.join()
    print('Child processes end.')


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    finish_time = time.perf_counter()

    print(f"Program finished in {(finish_time - start_time):.3f} seconds")