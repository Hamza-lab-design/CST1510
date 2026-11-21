# FIXED: TypeError - "value" held numbers stored as text ("87"), so it could
# not be divided. Converting the column to int first makes the maths work.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

df["value"] = df["value"].astype(int)
df["percent"] = (df["value"] / df["limit"]) * 100

print(df)
