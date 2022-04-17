import logging

my_logger = logging.getLogger(__name__)


def show_mod1_id(mod1):

    if 0 < mod1.id < 100:
        print(f"input Mod1 instance id: {mod1.id}")
        my_logger.info(f"input Mod1 instance id: {mod1.id}")
    else:
        my_logger.error(f"input Mod1 instance id: {mod1.id} is out of range")
        raise ValueError(f"input Mod1 instance id: {mod1.id} is out of range")

