wish_list = []

while True:
    print("1. Добавить желание")
    print("2. Удалить желание")
    print("3. Показать список желаний")
    print("4. Выход")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        wish = input("Введите желание: ")
        wish_list.append(wish)
        print("Желание добавлено")

    elif choice == 2:
        if len(wish_list) == 0:
            print("Список желаний пуст")
        else:
            print("Список желаний:")
            for i in range(len(wish_list)):
                print(str(i+1) + ". " + wish_list[i])
            index = int(input("Введите номер желания, которое нужно удалить: "))
            if index <= len(wish_list):
                del wish_list[index-1]
                print("Желание удалено")
            else:
                print("Неправильный номер желания")

    elif choice == 3:
        if len(wish_list) == 0:
            print("Список желаний пуст")
        else:
            print("Список желаний:")
            for i in range(len(wish_list)):
                print(str(i+1) + ". " + wish_list[i])

    elif choice == 4:
        break

    else:
        print("Неправильный выбор")