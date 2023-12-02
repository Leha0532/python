import random
inventory =[]
def gaw():
    print("гавгавгавгавагавгавагавгавагавгаваа")
 
def robot_forward():
    print("робот идёт")
        
def robot_back():
    print("робот назад")

def robot_BleBo():
    print("робот идёт влево")
        
def robot_B_prawo():
    print("робот идёт вправо")
    
def robot_scan():
    
    items = ["ветка", "бутылка", "железо", "дерево", "медвед", "алмаз", "комп", "ЯДЕРНЫЙ ДВИГАТЕЛЬ", "землю",]
    item = random.choice(items)
    print(f"робот нашел {item}")
    return item
    
def robotpickup(item):
    global inventory
    inventory.append(item)
    
def check_inventory():
    for index, item in enumerate(inventory, start=1):
        print(f"{index}. {item}")
        
def craft():
    recept1 = ["ветка", "ветка"] # дерево
    recept2 = ["алмаз", "ветка"] # алмазная_палка
    recepts = [recept1, recept2]
    recept_names = ["дерево", "алмазная_палка"]
    print("Доступны следующие рецепты:")
    for index, recept in enumerate(recept_names, start=1):
        print(f"{index}. {recept}")
    choice = input("выбери что хачешь крафтить:")
    if not choice.isdigit():
        print("водить числа ")
        return None
    choice = int(choice) - 1
    if choice not in range(0, len(recept_names)):
        print("вы вели не тот намер")
        return None
    choice_recept = recept_names[choice]
    print(f" вы выбрали крафтить {choice_recept}") 
    ingredients = recepts[choice]
    print(f"Ингридиенты: {ingredients}")
    for item in inventory:
        if item in ingredients:
            print(f"унитчтожение: {item}")
            inventory.remove(item)
            ingredients.remove(item)
    if not ingredients:
        inventory.append(choice_recept)
        print(f"В инвентар добав {choice_recept}")
    else:
        print("не хватает ингрд")
    

    
while True:
    key = input("ведите клав:")
    if key == "w":
        robot_forward()
    elif key == "s":
        robot_back()
    elif key == "a":
        robot_BleBo()
    elif key == "d":
        robot_B_prawo()
    elif key == "f":
        item = robot_scan()
        robotpickup(item)
        print(inventory)
    elif key == "e":
        print(inventory)
    elif key == "c":
        craft()
