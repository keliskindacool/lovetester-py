# UPDATE 2025-10-06: this code finally, FINALLY works. it took me THREE years to fix it (which i am not proud of), it kinda sucks with how many goddamn "else ifs" there are, but
# god i'm gonna take my victories where i can get em. the real kicker? THE FIX WAS SIMPLE AS MOTHERFUCK.



import random
import time

print("WELCOME TO THE LOVE TESTER (figlet is fucking broken. this is the best i've got.)")

print("\nThis love tester is completely randomly generated. It does not aim to determine your love life, and you should not use it as such.")
start = input("Start? (Y/N) ").lower()


def tester():
    name1 = input("Enter a name: ")
    name2 = input("Now enter another name: ")
    lovePercent = random.randint(0,100)

    print(f"Compatibility between {name1} and {name2}: {lovePercent}%")

    if lovePercent < 5:
        print("Yeah... that's not gonna work, is it?")
    elif lovePercent < 15:
        print("You two have to work out some serious issues before anything can get rolling.")
    elif lovePercent < 25:
        print("I mean, there's hope... but not much.")
    elif lovePercent < 40:
        print("Sparks are beginning to fly.")
    elif lovePercent < 50:
        print("A real 'will they won't they' situation!")
    elif lovePercent < 70:
        print("There's a lotta chemistry here! This could work!")
    elif lovePercent < 85:
        print("I'm really liking the look of this. You two are great together!")
    elif lovePercent < 95:
        print("Whew, off the charts, baby!")
    elif lovePercent <= 100:
        print("Why are you still sitting here? Get off your chair and ask them out!")
    else:
        print("Why are you recieving this message?") # yeah i dunno. you're not meant to see this. if you do then clearly something's wrong.


    
if "y" in start:
    tester()
else:
    exit()





