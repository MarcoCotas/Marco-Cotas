def main():
    time = convert(input("What time is it ?"))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    if minutes.endswith("p.m."):
        minutes = float(minutes.removesuffix("p.m."))
        hours = float(hours) + 12

    elif minutes.endswith("a.m."):
        minutes = float(minutes.removesuffix("a.m."))
        hours = float(hours)

    else:
        minutes = float(minutes)
        hours = float(hours)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
