import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

# print(f"chars : {chars}")
# print(f"keys : {key}")


# ENCRYPT

plain_text = input("Enter the message that should encrypt : ")
cipher_text = ""

for letter in plain_text :
    index  = chars.index(letter)  # get the letter index that where the letter is locate
    cipher_text  += key[index]

print(f"My original msg is : {plain_text}")
print(f"My encrypted msg is  : {cipher_text}")

# deCyrption

E_key = input("Enter the msg that should want to decrypt : ")
plain_text = ""

for letter in E_key :
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted msg : {E_key}")
print(f"The original msg is the  : {plain_text}")