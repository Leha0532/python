
def plus(x, y):
    return x + y
    
def minus(x, y):
    return x - y
    
def delenie(x,y):
    return x / y

def mul(x,y):
    return x,y

def input_number(input_phrase):
    x = input(input_phrase)
    if not x.isdigit():
        print("ВОДИ ЧИСЛА")
        return input_number(input_phrase)
    return int(x)


while True:
    x = input_number("ведите первое число")
    sign = input("ведите знак действие")
    y = input_number("ведите второе число")
    if sign == "+":
        result = plus(x,y)
        print(result)
    elif sign  == "-":
        result = minus(x,y)
        print(result)

