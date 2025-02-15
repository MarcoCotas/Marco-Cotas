import inflect
import sys

p = inflect.engine()
list_of_names = []


while True:
    try:
        name = input("Name: ")
        list_of_names.append(name)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(list_of_names)}")
        sys.exit()
