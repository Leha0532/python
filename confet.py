s = 33
a = 0
b = 0
while s > 0:
    a = int(input("игрок 1,ведите число от 1 до 3:"))
    s = s - a
    print(f"на столе осталось {s} конфет")
    if s == 0:
        print("игрок1, you lose")
        break
    b = int(input("игрок 2,ведите число от 1 до 3:"))
    s = s - b
    print(f"на столе осталось {s} конфет")
    if s == 0:
        print("игрок2, you lose")