# FIXED: ValueError (could not convert string to float) - "unknown" is not a
# number. try/except lets the program report that value instead of crashing.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    try:
        print(key, float(value))
    except ValueError:
        print(key, "is not a number:", value)
