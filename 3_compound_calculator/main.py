principle = 0 
rate = 0 
time = 0

while principle <= 0 : 
    principle = float(input("Enter the principle amount : "))
    if principle <= 0 : 
        print("principle cant be less than or equal to the zero ")

while rate <= 0 : 
    rate = float(input("Enter the interest rate : "))
    if rate <= 0 : 
        print("principle cant be less than or equal to the zero ")

while True : 
    time = float(input("Enter the time in the years : "))
    if time <= 0 : 
        print("principle cant be less than or equal to the zero ")
    else :
        break
total = principle * pow((1 + rate / 100 ) , time)
print(f"Balance after {time}  Years / s : ${total:.2f}")