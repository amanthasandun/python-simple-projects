# Python baniking app 
def show_balance ():
    print(f"Your balance is {balance:.2f}")

def deposite () : 
    amount = int(input("Enter a amount that you going to deposite : "))
    if amount < 0 : 
        print("Thats not a valid amount ...")
        return 0
    else :
        return amount 

def withdraw() : 
    amount = float(input("Enter the amount that going to wothdraw? : "))
    if amount > balance : 
        print("In sufficient balance........!")
        return 0 
    elif amount < 0 :
        print("Amount must be greater that the 0 ")
        return 0 
    else : 
        return amount


balance = 0 

is_running = True

while is_running : 
    print("------------------Banking System -----------------")
    print("1 . Show balance")
    print("2 . deposite the balance")
    print("3 . withdraw the balance")
    print("4. Exit")

    choise = input("Enter your choice : ")
    if choise == "1" : 
        show_balance()
    elif choise == "2" : 
        balance += deposite()
    elif choise == "3" : 
        balance -= withdraw()
    elif choise == "4" : 
        is_running = False
    else : 
        print("Enter the valid choice...")
print("Thankyou and have you nice day......!!!!!!")