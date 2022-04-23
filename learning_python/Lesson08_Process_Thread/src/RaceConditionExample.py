import concurrent.futures
import logging
import time


class FakeDB:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_val = self.value
        logging.info(f"Thread {name} has init db value {local_val}")
        local_val += 1
        time.sleep(0.1)
        self.value = local_val
        logging.info(f"Thread {name} output value {self.value} to db ")
        logging.info("Thread %s: finishing update", name)


def main():
    log_format = "%(asctime)s: %(message)s"
    log_level = "INFO"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format, level=log_level, datefmt=date_format)

    db = FakeDB()
    logging.info("Testing update. Starting value is %d.", db.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pe:
        for i in range(2):
            pe.submit(db.update, i)
    logging.info("Testing update. Ending value is %d.", db.value)


if __name__ == "__main__":
    main()
