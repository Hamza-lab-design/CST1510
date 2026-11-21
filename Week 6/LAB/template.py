"""
RECORD CHECK  -  my version
===========================

Name  :  Hamza Midani
Lane  :  AI / Data Science
Date  :  15 November 2026

Run it:   python template.py

Reads datasets.csv (dataset, rows_loaded, rows_expected), works out what
percent of the expected rows each dataset actually loaded, gives each one a
status, and reports the result. Over 100% means more rows arrived than
expected, which usually points to duplicates.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("datasets.csv")


# ================================================================= PROCESS
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
# Threshold: the full table with the percent column
print("All datasets:")
print(df)

# Typical: only the rows that are not OK, with a boolean filter (no loop)
not_ok = df[df["status"] != "OK"]
print(f"\nDatasets needing attention ({len(not_ok)} of {len(df)}):")
print(not_ok)

# Excellent: count per status, save the full report, save one bar chart
counts = df.groupby("status")["dataset"].count()
print("\nCount per status:")
print(counts)

df.to_csv("datasets_report.csv", index=False)
print("\nSaved datasets_report.csv")

counts.plot(kind="bar")
plt.title("Datasets per status")
plt.ylabel("Number of datasets")
plt.tight_layout()
plt.savefig("datasets_status.png")
print("Saved datasets_status.png")
