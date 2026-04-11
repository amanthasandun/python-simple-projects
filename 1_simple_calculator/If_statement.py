operator = input("Enter the operator (+ , / , * , -) : ")
num1 = float(input("Enter the fiust numbet : "))
num2 = float(input ("Enter the second number : "))

if operator == "+" : 
    result = num1 + num2
elif operator == "-" : 
    result = num1-num2 
elif operator == '*' :
    result = num1*num2
elif operator == "/" : 
    result = num1 / num2

print(result)