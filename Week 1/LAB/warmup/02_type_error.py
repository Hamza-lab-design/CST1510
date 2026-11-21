# FIXED: TypeError - input() always gives back text, and text + 1 is not allowed.
# Converting with float() first makes it a number.

value = float(input("Value: "))

print(value + 1)
