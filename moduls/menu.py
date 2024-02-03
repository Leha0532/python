from constant import *
from cost import *



def choise_pizza():
    print("pizza dream")
    print("menu pizza")
    for number, pizza in enumerate(PIZZA):
        print(f"{number+1}. {pizza} - {COST[number]}")
        
    while True:
        order = int(input("choise pizza: "))
        order -= 1
        
        print(f"pizza {PIZZA[order]} add in korzina")
        
        flag = input("hotite prodolzhit?")
        if flag == "net":
            print("ti Bisel iz menu")
            break
        
choise_pizza