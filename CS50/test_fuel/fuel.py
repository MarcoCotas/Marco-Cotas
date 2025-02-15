def main():
    fraction = input("Fraction: ")
    value = convert(fraction)
    final = gauge(value)
    print(final)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        return (x / y) * 100 
    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
