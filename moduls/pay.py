from cost import *
import random

def pay():
    money = random.choice(["da", "net"])
    if money == "da":
        print("Bi oplatili")
    else:
        print("вам не хватило денeg")