def season(mounth):
    if mounth in [1,2,12]:
        return "зима"
    elif mounth in [3,4,5]:
        return "весна"
    elif mounth in [9,10,11]:
        return "осень"
    elif mounth in [6,7,8]:
        return "лето"
    number = input("ведите meciac")
    print(f"{mounth}")