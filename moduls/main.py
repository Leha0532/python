#from menu import choise.pizza
#from order import
#from cost import 
#from pay import
#from check import give.check

from menu import choise_pizza
from cost import show_cost
from pay import pay
import time

def start():
    choise_pizza()
    time.sleep(2)
    show_cost()
    time.sleep(3)
    pay()

start()