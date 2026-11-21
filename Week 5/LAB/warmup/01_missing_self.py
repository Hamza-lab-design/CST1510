# FIXED: TypeError (takes 1 positional argument but 2 were given) - every method
# needs self as its first parameter, because Python passes the object in
# automatically.

class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
