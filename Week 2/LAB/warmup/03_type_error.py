# FIXED: TypeError - input() gives back text, and text cannot be compared
# with a number using >. Converting with float() first fixes it.

limit = 20
value = float(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
