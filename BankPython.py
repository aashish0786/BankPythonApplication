import time
data={1001:{
        "name":"Aashish",
        "balance":40000,
        "password":"0000"},
    1002:{
        "name":"vivek",
        "balance":4000000,
        "password":"vivek"}}

def signup():
    name=input("Enter your name:\n").title()
    password=input('Enter your password: ')
    initialbalance=int(input("How much initial bank you want to add: "))
    ac=1000+(len(data))+1
    print(f"Note down your account number and save it for future use:\n{ac}")
    data[ac]={"name":name,"balance":initialbalance,"password":password}
    msg="signing up"
    for i in range(10):
        msg=msg+"."
        print(f"{msg}\r",end="")
        time.sleep(.1)
    print("\n")
    login()

def goodbye():
    print("\tThanks for using bank application\n\t\tBYE BYE")

def login():
    tempac=int(input("Enter your account number:\n"))
    if tempac in data:
        temppd=input("Enter your password:\n")
        if temppd==data[tempac]["password"]:
            msg="logging in"
            for i in range(10):
                msg=msg+"."
                print(f"{msg}\r",end="")
                time.sleep(.1)
            print("\n")
            dashboard(tempac)
        else:
            print("User password is incorrect please try again")
            bank_application_menu()
    else:
        print("User account not found")
        bank_application_menu()
    #return tempac

def dashboard(tempac):
    print("Welcome to dashboard of your bank:")
    choice=int(input("1.credit\n2.debit\n3.checkbalance\n4.logout\nPlease write the name of option :)\n"))
    if choice==1:
        creditbal=int(input("Enter the amount\n"))
        data[tempac]["balance"]+=creditbal
        print(f"Your account has been credited ruppess:{creditbal}")
        print(f'Your total balance is:{data[tempac]["balance"]}')
        dashboard(tempac)
    elif choice==2:
        debitbal=int(input("Enter the amount\n"))
        data[tempac]["balance"]-=debitbal
        print(f"Your account has been debited ruppess:{debitbal}")
        print(f'Your total balance is:{data[tempac]["balance"]}')
        dashboard(tempac)
    elif choice==3:
        print(f'Your total balance is:{data[tempac]["balance"]}')
        dashboard(tempac)
    elif choice==4:
        print("Thank you for using our services")
        msg="loging out"
        for i in range(10):
            msg=msg+"."
            print(f"{msg}\r",end="")
            time.sleep(.1)
        print("\n")
        bank_application_menu()
    else:
        print("Invalid input try again")
        dashboard(tempac)

def bank_application_menu():
    print("______WELCOME TO PYTHON BANK______\nPlease choose option from below\n1.login\n2.signup\n3.exit\n___________________________________")
    userip=(int(input("(please type the number)\n")))
    if userip==1:
        login()
    elif userip==2:
        signup()
    elif userip==3:
        goodbye()
    else:
        print("Try again")
        bank_application_menu()
bank_application_menu()