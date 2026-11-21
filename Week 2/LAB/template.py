"""
RECORD CHECK  -  my version
===========================

Name  :  Hamza Midani
Lane  :  AI / Data Science
Date  :  October 2026

Run it:   python template.py

Checks as many datasets as you like in one run: how many rows loaded against
how many were expected. Type quit as the dataset name to stop.
"""

over_count = 0

while True:
    # ===================================================================== INPUT
    label = input("Dataset name (type quit to stop): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    # =================================================================== PROCESS
    difference = value - limit
    percent = value / limit * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ==================================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  {'Rows loaded':<14}: {value:>10.2f}")
    print(f"  {'Rows expected':<14}: {limit:>10.2f}")
    print(f"  {'Difference':<14}: {difference:>+10.2f}")
    print(f"  {'Percent':<14}: {percent:>10.2f} %")
    print(f"  {'Status':<14}: {status:>10}")
    print("=" * 34)
    print()

print(f"{over_count} dataset(s) came back OVER LIMIT")
