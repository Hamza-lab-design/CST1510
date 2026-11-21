# FIXED: TypeError (missing 1 required positional argument) - status_of needs
# two arguments. Giving warning_at a default value lets it be called with one.

def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95))
