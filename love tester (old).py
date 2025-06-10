import random
import time
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText("LOVE TESTER"))

print("\nThis love tester is completely randomly generated. It does not aim to determine your love life, and you should not use it as such.")
start = input("Start? (Y/N) ").lower()


def tester():
    name1 = input("Enter a name: ")
    name2 = input("Now enter another name: ")
    lovePercent = random.randint(0,100)

    print("Compatibility between", name1, "and", name2, ":", lovePercent, "%")
    


if "y" in start:
    tester()
else:
    exit()






