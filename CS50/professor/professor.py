import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0
        answered_correctly = False

        while attempts < 3 and not answered_correctly:
            try:
                user_input = input(f"{x} + {y} = ")
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    score += 1
                    answered_correctly = True
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if not answered_correctly:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input in [1, 2, 3]:
                return level_input
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level. Level must be 1, 2, or 3.")


if __name__ == "__main__":
    main()
