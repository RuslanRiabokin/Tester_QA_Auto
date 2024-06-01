
try:
    fail = open("tekst8.txt")
except FileNotFoundError:
    print("No file")