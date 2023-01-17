class Printer:
    def __init__(self, pid):
        self.name = "This is printer"
        self.id = pid

    def printMsg(self, msg):
        return f"Printer {self.id} prints: {msg}"