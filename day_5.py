#easy level
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['$','#','^','*','@','!','+','-','&']
print("welcome to the password generator ")
p_letter = int(input("how many letters would you like in password?\n"))
p_num = int(input("how many number would you like in password?\n"))
p_sym = int(input("how many symbols would you like in password?\n"))
password = ""
for char in range(1, p_letter + 1):
    random_char = random.choice(letters)
    password += random_char
for num in range(1, p_num + 1):
    random_num = random.choice(numbers)
    password += random_num
for num in range(1, p_sym + 1):
    random_sym = random.choice(symbols)
    password += random_sym
print(password)

#hard level
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['$','#','^','*','@','!','+','-','&']
print("welcome to the password generator ")
p_letter = int(input("how many letters would you like in password?\n"))
p_num = int(input("how many number would you like in password?\n"))
p_sym = int(input("how many symbols would you like in password?\n"))
password = []
for char in range(1, p_letter + 1):
    random_char = random.choice(letters)
    password += random_char
for num in range(1, p_num + 1):
    random_num = random.choice(numbers)
    password += random_num
for num in range(1, p_sym + 1):
    random_sym = random.choice(symbols)
    password += random_sym
print(password)
p = ""
random.shuffle(password)
for char in password:
    p += char
print(f"your password is {p}")



