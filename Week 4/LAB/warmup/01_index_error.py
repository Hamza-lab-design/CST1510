# FIXED: IndexError - a 3-item list has positions 0, 1 and 2, so [3] does not
# exist. [-1] (or [2]) is the last item.

labels = ["R-001", "R-002", "R-003"]

print(labels[-1])
