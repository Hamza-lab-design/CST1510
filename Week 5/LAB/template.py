"""
RECORD CHECK  -  my version
===========================

Name  :  Hamza Midani
Lane  :  AI / Data Science
Date  :  28 October 2026

Run it:   python template.py

Loads datasets from datasets.txt (name,rows_loaded,rows_expected) as Record
objects, prints a bordered report for each, and counts how many are OVER LIMIT.
"""



class Record:
    over_limit_count = 0

    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
       """Return OVER LIMIT, WARNING or OK from value and limit."""
       pct = self.value / self.limit * 100
       if pct >= 100:
          return "OVER LIMIT"
       elif pct >= 90:
          return "WARNING"
       else: 
           return "OK"


def load_records(path):
    """Read label,value,limit lines and return a list of Record objects."""
    records = []
    with open(path)as f:
       for line in f :
           line = line.strip()
           if line == "":
              continue
           label,value,limit = line.split(",")
           records.append(Record(label, float(value),float(limit)))

    return records

records = load_records("datasets.txt")



for record in records:
    result = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f" Rows loaded   : {record.value:>10.0f}")
    print(f" Rows expected : {record.limit:>10.0f}")
    print(f" Status        : {result:>10}") 
    print("=" * 34)
    if result == "OVER LIMIT":
       Record.over_limit_count += 1

    print()
print(f"{Record.over_limit_count} of {len(records)} records are OVER LIMIT")
