while True:
    try:
        number = int(input("Whats your number: "))
        factorial = 1
        for i in range(factorial, number +1):
            sum= factorial * i
            factorial = sum

    except ValueError:
        print("Please insert a valid number!" )

    print (f"The factorial of {number} is {factorial}")
