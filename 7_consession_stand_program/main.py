menu = {
    "pizza": 3.00,
    "burger": 4.50,
    "hotdog": 2.50,
    "fries": 2.00,
    "nachos": 3.50,
    "popcorn": 1.75,
    "soda": 1.50,
    "water": 1.00,
    "icecream": 2.25,
    "sandwich": 3.25,
}

cart = []
total = 0 

print("------Menu------------------")
for key , value in menu.items() : # items return the key and the value in the dictionary seperately 
    print(f"{key:10} : {value:.2f}") 


while True : 
    food = input("Select an item (q to quit)  : ").lower()
    if food ==  "q" : 
        break
    elif menu.get(food) is not None : 
        cart.append(food)
    else:
        print("Item not found. Please choose a valid menu item.")

print("------------Your Order---------------")
for food in cart : 
    total += menu.get(food)
    print(food , end=" ")
print()
print(f"Your total is : ${total:.2f}")