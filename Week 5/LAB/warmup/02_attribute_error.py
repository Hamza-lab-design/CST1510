# FIXED: AttributeError - __init__ stored the value as self.amount, so r.value
# did not exist. Storing it as self.value matches the name used later.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
