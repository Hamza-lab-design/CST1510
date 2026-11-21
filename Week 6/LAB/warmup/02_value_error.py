# FIXED: ValueError - "label" had 3 values but "value" had only 2.
# Every column needs the same number of values, so a third value was added.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
})

print(df)
