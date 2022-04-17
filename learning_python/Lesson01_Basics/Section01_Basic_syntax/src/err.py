def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


if __name__ == "__main__":
    main()
