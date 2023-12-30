def sign_up():
    login = input("login bedi")
    password1 = input("pridymai parol")
    password2 = input("bedide eoe jlby hfp")
    if password1 == password2:
        write_to_file("logins.txt",login+"\n")
        write_to_file("passwords.txt",password1+"\n")
        print(f"polzodatel {login} zaregal")
    else:
        print("paroli ne poxozi")
    
def write_to_file():
    with open("text.txt",mode="a",encoding="utf-8") as file:
        file.write()
    
while True:
    print("programa ymeett")
    print("1 - zaregatcia")
    print("2 - dieti iz programi")
    action = input("bedide nomer")
    if action == "1":
        sign_up()
    if action == "2":
        print("spacibo")
        break
    input("nazmi enter xtobi prodoldit")