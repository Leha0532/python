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

