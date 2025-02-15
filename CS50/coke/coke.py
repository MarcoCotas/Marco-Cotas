def main():
    valid()


def valid():
    coke = 50
    print(f"Amount Due: {coke}")
    while coke > 0:
        coin = int(input("Insert Coin: "))

        if coin in (25, 10, 5):
            coke = coke - coin
            print(f"Amount Due: {coke}")
            if coke <= 0:
                print(f"Change Owed: {abs(coke)}")
            continue
        else:
            print(f"Amount Due: {coke}")


main()
