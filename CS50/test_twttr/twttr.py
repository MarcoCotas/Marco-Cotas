def main():
    s = input("Input: ")
    print(shorten(s))

def shorten(word):
    result = ""
    for c in word:
        if c not in "aeiouAEIOU":
            result += c
    return result

if __name__ == "__main__":
    main()
