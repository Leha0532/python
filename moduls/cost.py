from constant import *
from order import *

def show_cost():
    global user_pizza, user_cost
    print(f"Bi zakazali pizza in enumirate")
    for number, pizza in enumerate(user_pizza):
        print(f"(number+1), {PIZZA} - {user_cost[number]}")
        
    print("obsia cost zakaza")
    summa = sum(user_cost)
    print(summa)