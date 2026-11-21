"""
RECORD CHECK  -  my version
===========================

Name  :  Hamza Midani
Lane  :  AI / Data Science
Date  :  15 November 2026

Run it:   python template.py

Reads messy survey responses from survey_lines.txt, cleans each one into a
dict, and flags the responses whose values cannot be trusted.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy raw survey line into a dict of survey, rating and age."""
    line = raw_line.strip().lower()
    survey_part, rest = line.split(",", 1)
    record = {"survey": survey_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record


def status_of(rating, age):
    """Return FLAGGED if the rating is not 1-5 or the age is not 16-100, otherwise OK."""
    if (rating < 1) or (rating > 5) or (age < 16) or (age > 100):
        return "FLAGGED"
    return "OK"


def load_lines(path):
    """Read the raw lines from a text file, skipping blank lines."""
    lines = []
    with open(path) as file:
        for line in file:
            if line.strip() != "":
                lines.append(line.rstrip("\n"))
    return lines


# ====================================================================== INPUT
raw_records = load_lines("survey_lines.txt")


# =============================================================== PROCESS + OUTPUT
total = 0
flagged = 0
unreadable = 0

for raw_record in raw_records:
    total += 1
    try:
        record = parse_line(raw_record)
    except ValueError:
        # e.g. rating=n/a gives
        #   ValueError: could not convert string to float: 'n/a'
        unreadable += 1
        print(f"Could not parse: [{raw_record}]")
        continue

    status = status_of(record["rating"], record["age"])
    if status == "FLAGGED":
        flagged += 1
    print(f"{record}  ->  {status}")

print(f"\n{total} records: {flagged} flagged, {unreadable} could not be parsed.")
