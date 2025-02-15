import sys
import csv

before = sys.argv[1]
after = sys.argv[2]
students = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >3:
    sys.exit("Too many command-line arguments")
try:
    with open(before) as rf:
        rf = csv.DictReader(rf)
        for row in rf:
            full_name = row["name"]
            house = row["house"]
            last_name, first_name = full_name.split(", ")
            students.append({"first": first_name, "last": last_name, "house": house})
    with open(after, 'w', newline='', encoding="utf-8") as wf:
            fieldnames = ["first", "last", "house"]
            final = csv.DictWriter(wf, fieldnames=fieldnames)

            final.writeheader()
            final.writerows(students) 

except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")




