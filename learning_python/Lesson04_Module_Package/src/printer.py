class Printer:
    """
    This class is a demo class for testing inspect module
    """

    def __init__(self, name):
        """
        The constructor of the printer
        :param name: the name of the printer
        :type name:
        """
        self.__name = name

    def print_message(self, message):
        """
        This method print the attribute message of the object
        :param message: the message to print
        :type message: str
        :return: None
        :rtype:
        """
        # some comments
        print(f"printer {self.__name} print message {message}")
