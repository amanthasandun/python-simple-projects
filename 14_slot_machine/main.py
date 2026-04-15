# Python slot machine 
import random

def spin_row (): 
    symbols = ["🍒" , "❤️" ,"🔥", "💡" ,"🚌"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row) : 
    print("*********************************************")
    print(" | ".join(row))
    print("*********************************************")

def get_payout( row , bet) :
    if row[0] == row[1] == row[2] :
        if row[0] == "🍒" :
            return bet * 10
        elif row[0] == "❤️" :
            return bet * 20
        elif row[0] == "🔥" :
            return bet * 30
        elif row[0] == "💡" :
            return bet * 40
        elif row[0] == "🚌" :
            return bet * 50
    else : 
        return 0

def main() : 
    balance = 100 
    print("*******************************************************") 
    print("Welcome to the python slots.............")
    print(" Symbols : 🍒 ❤️ 🔥 💡 🚌 ")
    print("*******************************************************")

    while balance > 0 : 
        print(f"Your current balance is : ${balance}")

        bet = input("Place your bet amount : ")

        if not bet.isdigit() : 
            print("Place a valid bet amount ")
            continue 

        bet = int(bet)

        if bet > balance : 
            print("insufficinet funcds")
            continue
        
        if bet <= 0 : 
            print( " bet must be greater than the zeerooo ...... ")
            continue 
        
        balance -= bet

        row = spin_row()
        print("Spinning.....!!!!")
        print_row(row)

        payout = get_payout(row , bet)
        if payout > 0 :
            balance += payout
            print(f"You won and Your new balance is {payout}")
             
        else :
            print("Sorry you loss the bet ")
            balance -= payout

        print(f"Your new balance is {balance}")
        


if __name__ == "__main__" : 
    main()