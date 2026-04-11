import random

options = ("rock" , "paper" , "scissor")
running = True

while running : 
    player = None
    comp = random.choice(options)

    while player not in options : 
        player = input("Enter the choice (rock , paper , scissor ) : ")

    print(f"Players Choice is : {player}")
    print(f"Computer choise is : {comp}")

    if player == comp : 
        print('It s a tie')
    elif player == "scissor" and comp == "rock" : 
        print("WoW , You are the winner")
    elif player == "rock" and comp == "paper": 
        print("WoW , You are the winner...")
    elif player == "paper" and comp  == "rock" : 
        print(" WoW  , You are the winner ")
    else : 
        print("ooop , You are the loser")
    play_again = input("Do you want to play again (y/n) : ").lower()

    if not play_again == "y": 
        running = False

print("Thanks for the playing....")
