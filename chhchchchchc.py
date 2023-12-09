
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


while True
x = input("ведите первое число")
if not x.isdigit():
    print ("водить числа")
    continue
x = int(x)

sign = input("ведите знак действие")
y = input("ведите второе число")
if not y.isdigit():
    print("водить числа")
    continue
y = int(y)
if sign == "+":
    result = plus(x,y)
    print(result)
elif sign  == "-":
    result = minus(x,y)
    print(result)
elif sign == ""
