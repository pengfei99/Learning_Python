import logging
from concurrent.futures import ThreadPoolExecutor
import time


def thread_task(tid: int):
    name = f"thread-{tid}"
    logging.info(f"Thread {name} : start")
    time.sleep(2)
    logging.info(f"Thread {name} : stop")
    return tid


def run_with_map(max_worker: int):
    with ThreadPoolExecutor(max_workers=max_worker) as pe:
        for future in pe.map(thread_task, range(10)):
            print(future.result(timeout=5))


def run_with_submit(max_worker: int):
    # the max worker numbers defines the max thread number in the pool
    with ThreadPoolExecutor(max_workers=max_worker) as pe:
        for i in range(10):
            future = pe.submit(thread_task, i)
            print(future.result(timeout=5))


def main():
    log_format = "%(asctime)s: %(message)s"
    log_level = "INFO"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format, level=log_level, datefmt=date_format)
    logging.info("Start main process")
    # run_with_map(2)
    run_with_submit(2)
    logging.info("All done")


if __name__ == "__main__":
    main()
