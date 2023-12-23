# file = open("text.txt", mode="w")
# file.write("скоро новый год")
# file.write("скоро год")
# file.close()

# file = open("text.txt",mode="w",encoding="UTF-8")
# file.write("времяяяяяяяяяяяяяяяя")
# file.close()

# with open("text.txt",mode="a",encoding="UTF-8") as file:
#     file.write("0000")
    
# with open("text.txt",mode="r",encoding="UTF-8") as file:
#     text = file.read()
#     print(text)

import random
def file_write500():
    with open("text.txt",mode="w",encoding="UTF-8") as file:
        for i in range(1,90):
            file.write("ччччhhhhhggfdsaasdfghjkl;'dfghjkl;чч")

def get_one_word(filename):
    with open(filename,mode="r",encoding="UTF-8") as file:
        text = file.read().split("\n")
        return random.choice(text)

pril = get_one_word("pric.txt")
name = get_one_word("animals.txt")
print(f"you name {pril} {name}")
    

    
    
