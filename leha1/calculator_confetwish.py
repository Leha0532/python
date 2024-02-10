import calculator
import confet
import wish
import leha1.login_pass as login_pass

access =False
while True:
    if not access:
        print("programa ymeett")
        print("1 - zaregatcia")
        print("2 doiti in programy")
        print("3 - dieti iz programi")
        action = input("bedide nomer")
        if action == "1":
            login_pass.sign_up()
        elif action =="2":
            access =  login_pass.sign_in()
        elif action == "3":
            print("spacibo")
            break
    elif access:
        print("menu")
        print("1 - calculator")
        print("2 - wish")
        print("3 - confet")
        print("4 - login")
        print("5 - pass")
        action = input("bedide nomer")
        if action == "1":
            calculator.main()
        if action == "2":
            wish.main()           
        if action == "3":
            confet.main()
    input("nazmi enter i prodolzi")
    if action == "4":
            login_pass.open()
    if action == "5":
            login_pass.open() 