from tabulate import tabulate
import sys
import os
import csv

request = sys.argv[1]
menus = []

while True:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif request.endswith("csv") == False:
        sys.exit("Not a CSV file")
    else:
        break

try:
    with open(request, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            menus.append(line)

    print(tabulate(menus[1:], headers=menus[0], tablefmt="grid"))
    print(menus)
except FileNotFoundError:
    sys.exit("File does not exist")
