# FIXED: ValueError (too many values to unpack) - "note=server=east" has two
# "=" signs, so split("=") gave 3 pieces for 2 variables. Splitting only at
# the first "=" (maxsplit of 1) gives exactly 2 pieces.

piece = "note=server=east"
key, value = piece.split("=", 1)

print(key, value)
