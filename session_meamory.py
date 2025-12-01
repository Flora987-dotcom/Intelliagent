class SessionMemory:

    def __init__(self):
        self.history = []

    def save_input(self, data):
        self.history.append({"user": data})

    def save_output(self, data):
        self.history.append({"agent": data})
