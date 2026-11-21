# FIXED: NameError - status() is a method, so it must be called on an object:
# r.status(), not status() on its own.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())
