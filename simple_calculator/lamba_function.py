opertor = input("Enter the operation that what you want to do (+ , - , / , *) : ")
num1 = float(input("Enter the first Number : ")) 
num2 = float(input("Enter the second number : "))

operations = {
    "+" : lambda x,y : x + y ,
    "-" : lambda x,y : x-y , 
    "/" : lambda x,y : x/y , 
    "*" : lambda x,y : x*y if y != 0 else "Error , devision by the zero"
}

func = operations.get(opertor)
if func : 
    result = func(num1 , num2)  # finally func is a lamda function .  so when we enter the values as in this way it aumatacally sign the parameters in the lamda funtion in the order 
else :
    result = f"{opertor} is not valid operator"

print(result)