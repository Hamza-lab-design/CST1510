# FIXED: AttributeError - .strip() is a string method, but it was being called
# on a float. Strip the text first, then convert it to a number.

value_text = "87"
cleaned = value_text.strip()
value = float(cleaned)

print(value)
