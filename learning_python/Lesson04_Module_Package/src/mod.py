good_word = "Eat an apple a day, keep the doctor away"
num_list = [100, 200, 300,400,500]


def addition(x, y):
    return x + y


class Printer:
    def __init__(self, name):
        self.__name = name

    def print_message(self, message):
        print(f"printer {self.__name} print message {message}")


def main():
    print(good_word)

    print(num_list)

    print(addition(2, 6))

    my_printer = Printer("laser printer")
    my_printer.print_message("hello world")


if __name__ == "__main__":
    main()
