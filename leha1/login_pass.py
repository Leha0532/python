def write_to_file(filename, text):
    with open("text.txt",mode="a",encoding="utf-8") as file:
        file.write(text)
        
def read_list(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        text = file.read().split("\n")
        return text

def sign_up():
    login = input("login beds")
    password1 = input("pridymai parol")
    password2 = input("bedide eoe jlby hfp")
    if password1 == password2:
        write_to_file("logins.txt",login+"\n")
        write_to_file("passwords.txt",password1+"\n")
        print(f"polzodatel {login} zaregal")
    else:
        print("paroli ne poxozi")
        
    import file1 
        
def sign_in():
    login = input("Bedite login")
    password = input("bedite parol")
    login_list = read_list("logins.txt")
    password_list = read_list("password.txt")
    if login in login_list:
        login_str = login_list.index(login)
        True_password = password_list[login_str]
        if password == True_password:
            print("yra ti zachel")
            return True
        else:
            print("parol inocorect")
            return False