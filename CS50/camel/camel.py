def main():
    s = input("camelCase: ").replace(" ", "")
    print ("snake_case: ", end="")
    for c in s:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")
    print()


main()
