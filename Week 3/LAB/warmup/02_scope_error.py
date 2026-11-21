# FIXED: NameError - status only existed inside check(). Returning it, and
# storing what comes back, gets the value out of the function.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87, 100)

print(status)
