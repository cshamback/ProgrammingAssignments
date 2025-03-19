class Task: 

    def __init__(self, p, s, e, n):
        self.pay = p
        self.start = s
        self.end = e
        self.name = n

    def __repr__(self):
        return f"Name: {self.name} Start time: {self.start} End time: {self.end} Pay: {self.pay}"