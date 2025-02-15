import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


font = random.choice(fonts)


if len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
    font = sys.argv[2]
elif len(sys.argv) != 1:
    print("Invalid usage")
    sys.exit(1)

figlet.setFont(font=font)

name = input("Input: ")
print(figlet.renderText(name))
