email = input("Enter your email : ")
index = email.index("@") # this return that where is the @ is locate in 
print(index)

userName = email[:index]
domain = email[index + 1:]

print(f"Your usernae is the {userName} and your Domain is the {domain}")