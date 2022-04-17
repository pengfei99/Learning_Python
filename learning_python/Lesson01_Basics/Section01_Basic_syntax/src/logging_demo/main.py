import logging
import os

from learning_python.Lesson01_Basics.Section01_Basic_syntax.src.logging_demo.mod1 import Mod1
from learning_python.Lesson01_Basics.Section01_Basic_syntax.src.logging_demo.mod2 import show_mod1_id


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


def main():
    ## advance custom formatter logger config
    # handler = logging.StreamHandler()
    # formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
    # handler.setFormatter(formatter)
    # root = logging.getLogger()
    # root.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
    # root.addHandler(handler)

    ## simple logger config with default formater and handler
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    ## logic of your app, independent of the logger config
    mod1 = Mod1(88)
    show_mod1_id(mod1)
    mod1.id = 120
    show_mod1_id(mod1)
    try:
        exit(main())
    except Exception:
        logging.exception("Exception in main(): ")
        exit(1)


if __name__ == "__main__":
    main()
