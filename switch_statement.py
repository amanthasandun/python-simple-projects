opertor = input("Enter the operation that what you want to do (+ , - , / , *) : ")
num1 = float(input("Enter the first Number : ")) 
num2 = float(input("Enter the second number : "))

match opertor : 
    case "+" : 
        result = num1 + num2 
    case "-" :
        result = num1 - num2
    case "/" : 
        result = num1 / num2
    case "*" : 
        result = num1 * num2 

print(result)
