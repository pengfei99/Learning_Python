import logging
import time
from threading import Thread


# define a thread task
def thread_task(name: str):
    logging.info(f"Thread {name} : start")
    time.sleep(2)
    logging.info(f"Thread {name} : stop")


def main():
    ## main process that launches thread
    # set up logger
    log_format = "%(asctime)s: %(message)s"
    level = "INFO"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format,level=level, datefmt=date_format)

    # start the main process
    logging.info("Main    : before creating thread")

    # create thread
    logging.info("Main    : before running thread-1")
    thread1 = Thread(target=thread_task, args=("thread-1",))
    logging.info("Main    : before running thread-2")
    thread2 = Thread(target=thread_task, args=("thread-2",))

    # start thread
    thread1.start()
    thread2.start()

    logging.info("Main    : wait for the thread-1 to finish")
    # thread1.join()

    logging.info("Main    : wait for the thread-2 to finish")
    # thread2.join()
    # finish main process
    logging.info("Main    : all done")


if __name__ == "__main__":
    main()
