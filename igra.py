from random import randint

user_name = input("Вашe имя: ")


game_round = 0
while game_round <= 3:
    game_round +=1
    print(f"раунд №{game_round}")
    comp_num = randint(1, 300)
    attempt = 0
    while attempt <= 30:
        print("Я загадал число от 1 до 300, угадай его :)")
        user_num = input(user_name+", Ваш Вариант: ")
        if not user_num.isdigit():
            print(f"{user_name}, вы ввели не число")
            continue
        attempt += 1
        print(f"Попытка №{attempt}")
        user_num = int(user_num)
        if user_num == comp_num:
            print(f"{user_name}, Ты угадал число, молодец !\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
            break
        elif user_num > comp_num:
            print("Моё число меньше.")
        elif user_num < comp_num:
            print("Моё число больше")
        print()
        if attempt == 10:
            print("Все попытки истрачены")
            break