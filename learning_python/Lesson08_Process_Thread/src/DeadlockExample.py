import logging
import time
from threading import Thread, Lock


class fake_db:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def get_val(self):
        return self.value

    def set_val(self, val: int):
        self._lock.acquire()
        # second acquire create a deadlock
        # self._lock.acquire()
        self.value = val
        self._lock.release()


def task(tid: int, db: fake_db):
    thread_name = f"thread-{tid}"
    logging.info(f"start {thread_name}")
    time.sleep(1)
    db.set_val(tid)
    logging.info(f"thread {thread_name} set db value to {db.get_val()} ")
    logging.info(f"stop {thread_name}")


def main():
    log_format = "%(asctime)s: %(message)s"
    log_level = "DEBUG"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format, level=log_level, datefmt=date_format)
    logging.info("Start main process")
    db = fake_db()
    t1 = Thread(target=task, args=(1, db))
    t1.start()
    t2 = Thread(target=task, args=(2, db))
    t2.start()

    t1.join()
    t2.join()
    logging.info("All done")


if __name__ == "__main__":
    main()
