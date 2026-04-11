import random 
lowest_num = 1 
highest_num = 100 

isRunning = True
answer = random.randint(lowest_num , highest_num )
print(answer)
guessess = 0 

print("Python number guesing game is started")
print(f"Select the number between the {lowest_num} and the {highest_num}")

while isRunning : 
    guess = input("Enter the guess : ")
    if guess.isdigit() :
        guess = int(guess)
        guessess += 1
        if guess < lowest_num or guess > highest_num :
            print("Number is out of range ")
            print(f"Enter the valid numeber range :{lowest_num} to {highest_num}")
        elif guess < answer :
            print("Too low , Try again")
        elif guess > answer : 
            print("Too high , Try again")
        else : 
            print(f"Wow you are the winner ..The answer was the {answer}")
            print(f"The attemps that you get : {guessess}")
            isRunning = False

    else : 
        print("Invalid input")
        print(f"Select the number between {lowest_num} and the {highest_num}")