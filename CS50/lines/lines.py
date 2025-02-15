import sys
count = 0
file_name = sys.argv[1]



while True:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif file_name.endswith(".py") == False:
        sys.exit("Not a Python file")
    elif len(sys.argv) == 2 and file_name.endswith(".py") == True:
        break
    else:
        raise FileNotFoundError ("raise FileNotFoundError") and sys.exit

with open (file_name) as file:
    for line in file:
        stripedline = line.strip()
        if stripedline.startswith("#") or line.strip() == "":
            continue
        else:
            count += 1






print (count)

