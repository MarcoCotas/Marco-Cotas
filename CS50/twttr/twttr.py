


def main():
    word = input ("Input: ")
    c = shorten(word)
    print(c, end="")
    


def shorten(word):
    for c in word:
        if c not in ("AEIOUaeiou"):
            return c
    return c


if __name__ == "__main__":
    main()
