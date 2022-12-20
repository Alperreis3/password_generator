#Password Generator Project
import random

# Create 3 lists to hold letters, numbers and symbols for password generation

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get the user input for each list above

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty list

password_list = []

# add random choice from the letters to the password_list

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  
# add random choice from the symbols to the password_list

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# add random choice from the numbers to the password_list

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# print the password_list

print(password_list)

# Then we will randomly shuffle the list so it will generate more secure password.
random.shuffle(password_list)
print(password_list)

# This will show the password in a string.

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")