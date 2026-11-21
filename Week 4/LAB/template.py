"""
RECORD CHECK  -  my version
===========================

Name  :  Hamza Midani
Lane  :  AI / Data Science
Date  :  October 2026

Run it:   python template.py

Loads datasets from records.txt (name,rows_loaded,rows_expected), checks each
one, prints a report line, and writes the statuses to dataset_results.txt.
"""
# ===== FUNCTIONS =====
def check_record(value,limit):
    """Return the difference, percent and status for one value against its limit."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference,percent,status



  
def print_report(label,value,limit,difference,percent,status):
    """Print one formatted report line for a record."""
    print(f"{label}: {value}/{limit}  ({percent:.1f}%, diff {difference:+d}) - {status}")
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open (path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label,value,limit = line.split(",")
            records.append({"label": label, "value": int(value),"limit": int(limit)})
    return records

def write_results(path,results):
    """Write one label,status line per record to a new file."""
    with open(path,"w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")



# ==== STORE ====
try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("could not find records.txt - starting with an empty list.")
    records = []


# ===== PROCESS + OUTPUT =====
results = []
over_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"],record["limit"], difference,percent,status)
    results.append ((record["label"], status))
    if status == "OVER LIMIT":
        over_count += 1

print(f"{over_count} record(s) OVER LIMIT")
write_results("dataset_results.txt", results)
