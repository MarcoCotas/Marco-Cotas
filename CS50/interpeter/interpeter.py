def main():
    expression = input("Expression: ")
    x, y, z = expression.split()
    final = conversor(x, y, z)
    print(f"{final:.1f}")


def conversor(x, y, z):
    x = int(x)
    z = int(z)

    if y == "+":
        return float(x + z)
    elif y == "*":
        return float(x * z)
    elif y == "-":
        return float(x - z)
    elif y == "/":
        return float(x / z)


main()
