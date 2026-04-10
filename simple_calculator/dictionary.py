operator = input("Enter the operator (+ , / , * , -) : ")
num1 = float(input("Enter the fiust numbet : "))
num2 = float(input ("Enter the second number : "))

operations = {
    "+" : num1 + num2 ,
    "-" : num1 - num2 , 
    "*" : num1 * num2 , 
    "/" : num1 / num2
}
 
result = operations.get(operator , "invalid operator")  # dictionary.get(key, default_value)
print(result)                                           # key → the key you are looking for
                                                        # default_value → what to return if the key is NOT found