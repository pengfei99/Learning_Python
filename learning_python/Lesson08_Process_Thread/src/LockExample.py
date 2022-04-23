import concurrent.futures
import logging
import threading
import time


class FakeDB:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # in this version we use method acquire(), release() to control the lock
    def update_v1(self, name):
        logging.info("Thread %s: starting update", name)
        self._lock.acquire()
        logging.info(f"Thread {name} acquired lock")
        local_val = self.value
        logging.info(f"Thread {name} has init db value {local_val}")
        local_val += 1
        time.sleep(0.1)
        self.value = local_val
        self._lock.release()
        logging.debug(f"Thread {name} released lock")
        logging.info(f"Thread {name} output value {self.value} to db ")
        logging.info("Thread %s: finishing update", name)

    # in this version we use context to control the lock automatically
    def update_v2(self, name):
        logging.info("Thread %s: starting update", name)
        # when we start the context with lock, the lock is acquired automatically
        with self._lock:
            logging.info(f"Thread {name} acquired lock")
            local_val = self.value
            logging.info(f"Thread {name} has init db value {local_val}")
            local_val += 1
            time.sleep(0.1)
            self.value = local_val
            # when the process exit the lock context block, the lock is released automatically
        logging.debug(f"Thread {name} released lock")
        logging.info(f"Thread {name} output value {self.value} to db ")
        logging.info("Thread %s: finishing update", name)


def main():
    log_format = "%(asctime)s: %(message)s"
    log_level = "DEBUG"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format, level=log_level, datefmt=date_format)

    db = FakeDB()
    logging.info("Testing update. Starting value is %d.", db.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pe:
        for i in range(2):
            # use v1
            # pe.submit(db.update_v1, i)

            # use v2
            pe.submit(db.update_v2, i)
    logging.info("Testing update. Ending value is %d.", db.value)


if __name__ == "__main__":
    main()
