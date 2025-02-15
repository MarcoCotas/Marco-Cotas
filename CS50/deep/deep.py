def main():
    answear = genious(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    print(answear)


def genious(answear):
    if answear.strip().lower() in ["42", "forty-two", "forty two"]:
        return "Yes"
    else:
        return "No"

main()
