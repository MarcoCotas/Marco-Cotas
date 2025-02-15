import random
import sys


def main():
    n = get_number()
    number = random.randint(1, n)
    get_result(number)


def get_number():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n

        except ValueError:
            continue


def get_result(n):
    while True:

        try:
            guess = int(input("Guess: "))
            if guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue


main()
