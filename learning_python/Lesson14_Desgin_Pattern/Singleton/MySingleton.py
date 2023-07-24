import threading


class MySingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class UserSession(metaclass=MySingletonMeta):
    def __init__(self, lastName: str, firstName: str):
        # we will use full name to show that the singleton really works
        self.fullName = f"{firstName} {lastName}"
        self.connection = self.connect()

    def connect(self):
        # activate user session
        print(f"User {self.fullName} has connected.")
        return True


# this function can help us to test the singleton class in a multi thread env
def createUserSession(firstName, lastName):
    session = UserSession(firstName, lastName)
    print(session.fullName)


def main():
    # createUserSession("toto", "Liu")
    # createUserSession("t1t1", "Liu")

    sessionThread1 = threading.Thread(target=createUserSession, args=("toto", "liu"))
    sessionThread2 = threading.Thread(target=createUserSession, args=("titi", "liu"))
    sessionThread1.start()
    sessionThread2.start()


if __name__ == "__main__":
    main()
