import random
print ("это игра угадай число")
print ("Комьпьютер загадал число от 1 до 100 попробуй его угадать")
attempts = 3
secret_number = random.randint (1,100)
tries = 1
user_number = input("ведите число:")
user_number = int(user_number)
print(f"вы ввели {user_number}")
while attempts <= 0:
 if not user_number > secret_number:
    print(f"{user_number}; вы не величисло")
    continue
    tries += 1
    user_number = int(user_number)
    print("вы ввели больше чем у меня")
 elif user_number < secret_number:
    print("вы ввели меньше чем у меня")
 elif user_number == secret_number:
    print("ты угадал аоаоаоаоаоао")