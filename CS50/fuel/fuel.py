def main():
    value = get_value()
    x = value[0]
    z = value[1]
    if (x/z)*100 <= 1:
        print ("E")
    elif (x/z)*100 >= 99:
        print ("F")
    else:
        print (f"{(x/z)*100:.0f}%")

def get_value():

    while True:
        try:
            fraction = (input("Fraction: "))
            x, z= fraction.split("/")

            x = int(x)
            z = int(z)
            
            if x > z:
                continue
            return (x,z)


        except (ValueError, ZeroDivisionError):
            pass
main()

