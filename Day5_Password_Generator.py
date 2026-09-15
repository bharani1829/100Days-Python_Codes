# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '|', '>', '<']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


nm_letters = int(input("How many letters do you want in your password: "))
nm_numbers = int(input("How many numbers do you want in your password: "))
nm_symbols = int(input("How many symbols do you want in your password: "))


# Easy Version

# password = ""

# for passw in range(0, nm_letters):
#     password += random.choice(letters)

# for passw in range(0, nm_numbers):
#     password += random.choice(numbers)    # in this Version We generated password but it is in order 4-2-2

# for passw in range(0, nm_symbols):
#     password += random.choice(symbols)

# print(password)


# Hard Version

password1 = []   # I used a list because it has a shuffle function to shuffle the password

for passw in range(0, nm_letters):
    password1.append(random.choice(letters))

for passw in range(0, nm_numbers):
    password1.append(random.choice(numbers))

for passw in range(0, nm_symbols):
    password1.append(random.choice(symbols))


print(password1)   # We generated a random password, but it is in order


random.shuffle(password1)

print(password1)   # I shuffled the password, but it is still in list format


password2 = ""

for i in password1:   # I used a for loop to convert the password from list format to string format
    password2 += i

print(password2)
