import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import os


class LogManager:
    DEFAULT_LOG_LEVEL = "DEBUG"  # better to have too much log than not enough
    LOG_PROPAGATE = False
    LOG_FORMAT = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
    ENABLE_FILE_HANDLER = False
    LOG_FILE_PATH = "~/app_log"

    def __init__(self, logger_name: str):
        self.logger_name = logger_name
        self.enable_file_handler = os.environ.get("ENABLE_FILE_HANDLER", LogManager.ENABLE_FILE_HANDLER)
        self.log_propagate = os.environ.get("LOG_PROPAGATE", LogManager.LOG_PROPAGATE)
        self.log_file_path = os.environ.get("LOG_FILE_PATH", LogManager.LOG_FILE_PATH)
        self.formatter = logging.Formatter(os.environ.get("LOG_FORMAT", LogManager.LOG_FORMAT))

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        Path(self.log_file_path).mkdir(parents=True, exist_ok=True)
        file_handler = TimedRotatingFileHandler(f"{self.log_file_path}/app.log", when='midnight')
        file_handler.setFormatter(self.formatter)
        return file_handler

    def get_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(os.environ.get("LOGLEVEL", LogManager.DEFAULT_LOG_LEVEL))
        logger.addHandler(self.get_console_handler())
        if self.enable_file_handler:
            logger.addHandler(self.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = self.log_propagate
        return logger
