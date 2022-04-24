import logging
import random
from threading import Lock, Thread

SENTINEL = object()


class Pipeline:
    def __init__(self):
        self.message = 0
        self._producer_lock = Lock()
        self._consumer_lock = Lock()
        # by default lock for consumer
        # This is the state you want to start in. The producer is allowed to add a new message,
        # but the consumer needs to wait until a message is present.
        self._consumer_lock.acquire()

    # when get message is called, pipeline is empty, lock consumer, so consumer will not read empty data
    # unlock producer. So producer can put data to pipeline.
    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self._consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self._producer_lock.release()
        logging.debug("%s:setlock released", name)
        return self.message

    # When set_message is called, pipeline is full. lock producer, so producer will not overwrite unread data
    # unlock consumer, so consumer can read data from pipeline
    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self._producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self._consumer_lock.release()
        logging.debug("%s:getlock released", name)


def producer(tid, pipeline):
    name = f"producer-{tid}"
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer %s got message: %s", name, message)
        pipeline.set_message(message, name)

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, name)


def consumer(tid, pipeline):
    name = f"consumer-{tid}"
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message(name)
        if message is not SENTINEL:
            logging.info("Consumer %s storing message: %s", name, message)


def main():
    log_format = "%(asctime)s: %(message)s"
    log_level = "DEBUG"
    date_format = "%H:%M:%S"
    logging.basicConfig(format=log_format, level=log_level, datefmt=date_format)
    logging.info("Start main process")
    pipeline = Pipeline()
    p1 = Thread(target=producer, args=(1, pipeline))
    c1 = Thread(target=consumer, args=(1, pipeline))

    p1.start()
    c1.start()

    p1.join()
    c1.join()

    logging.info("All done")


if __name__ == "__main__":
    main()
