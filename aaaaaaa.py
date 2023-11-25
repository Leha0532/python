


print("это список желаний")
name = input("как вас зовут ")
wishlist = []

while True:
    print("меню")
    print("1- добавить желание")
    action = input(f"что хотите сделать {name}")
    if action == "1":
        wish = input(f"{name},какое желание хотите добавить:")
        if wish not in wishlist:
            wishlist.append(wish)

    if action == "2":
        for i, wish in enumerate(wishlist, start = 1):
            print(f"(i). {wish}")
    