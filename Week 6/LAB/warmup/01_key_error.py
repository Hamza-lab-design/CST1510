# FIXED: KeyError - the column is "value", not "Value" (names are case-sensitive).

import pandas as pd

df = pd.DataFrame({"label": ["R-001", "R-002"], "value": [87, 120], "limit": [100, 100]})

print(df["value"])
