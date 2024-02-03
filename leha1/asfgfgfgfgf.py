import random
health = 100
step = 1
coins = 0
while step <= 10:
    print (step)
    step += 1
    events = ["бои" , "находка" , "пропуск"]
    event = random.choice(events)
    if event == "бои":
        user_choises = input("убить или нет")
        if user_choises=="убить" :
            health=-35+
