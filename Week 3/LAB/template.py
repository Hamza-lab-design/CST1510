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

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered report for a dataset."""
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


# ============================================================ INPUT/PROCESS/OUTPUT
over_count = 0

while True:
    label = input("Dataset name (type quit to stop): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1

print(f"\n{over_count} dataset(s) came back OVER LIMIT")
