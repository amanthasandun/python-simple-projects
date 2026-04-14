 # Python creadit card validator
# step 1 (get the card number)
sum_even_digits = 0
sum_odd_digits = 0
total = 0

card_no  = input("Enter the creadit card no : ")
card_no = card_no.replace("-","")
card_no = card_no.replace(" " , "")
card_no = card_no[::-1]


# step 2 ( get the summation of the odd number)

for x in card_no[::2] : 
    sum_odd_digits += int(x)

# step 3 ( get the sum of the even numbers )

for x in card_no[1::2] : 
    x = int(x) * 2 
    if x >= 10 :
        sum_even_digits += (1+ (x % 10))
    else : 
        sum_even_digits += x
    
# step 4 ( get the total of the sum of odd degits and the sum of the even degits)

total = sum_odd_digits + sum_even_digits

# step 5 ( if total devisable by the 10 , it is valid number)

if total % 10 == 0 : 
    print("It is a valid number")
else : 
    print("It is invalid number ")