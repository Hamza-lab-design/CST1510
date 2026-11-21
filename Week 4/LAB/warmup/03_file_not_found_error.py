# FIXED: FileNotFoundError - the file did not exist where the program looked.
# try / except FileNotFoundError prints a clear message instead of crashing.

try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("records.txt not found - check the file name and the folder you are in.")
