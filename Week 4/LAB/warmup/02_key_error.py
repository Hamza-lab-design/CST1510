# FIXED: KeyError - the dict has no "status" key. .get() returns a default
# instead of crashing when a key is missing.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record.get("status", "no status yet"))
