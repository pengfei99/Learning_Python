import logging

my_logger = logging.getLogger(__name__)


class Mod1:
    def __init__(self, id):
        self.__id = id
        my_logger.debug(f"Create instance of Mod1 with {id}")

    @property
    def id(self):
        my_logger.debug(f"Mod1 getter is called, return {self.__id}")
        return self.__id

    @id.setter
    def id(self, id):
        my_logger.debug(f"Mod1 setter is called, update value from {self.__id} to {id}")
        self.__id = id

