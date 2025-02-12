import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Solutions
# ---------------------------
# Solution 1
# password = []
#
# for number in range(1, nr_letters + 1):
#     password.append(letters[random.randint(0, len(letters) - 1)])
# for number in range(1, nr_symbols + 1):
#     password.append(symbols[random.randint(0, len(symbols) - 1)])
# for number in range(1, nr_numbers + 1):
#     password.append(numbers[random.randint(0, len(numbers) - 1)])
#
# scrambled_characters_to_add = nr_letters + nr_symbols + nr_numbers
# scrambled_password = ""
#
# for number in range(1, scrambled_characters_to_add + 1):
#     random_index = random.randint(0, scrambled_characters_to_add - 1)
#     scrambled_password += password[random_index]
#     password.remove(password[random_index])
#     scrambled_characters_to_add -= 1
#
# print(scrambled_password)

# Solution 2
# password_list = []
#
# for number in range(1, nr_letters + 1):
#     password_list.append(letters[random.randint(0, len(letters) - 1)])
# for number in range(1, nr_symbols + 1):
#     password_list.append(symbols[random.randint(0, len(symbols) - 1)])
# for number in range(1, nr_numbers + 1):
#     password_list.append(numbers[random.randint(0, len(numbers) - 1)])
#
# random.shuffle(password_list)
#
# password = ""
# for character in password_list:
#     password += character
#
# print(f"Your password is: {password}")

# Solution 3
password_list = []

for number in range(nr_letters):
    password_list.append(letters[random.randint(0, len(letters) - 1)])
for number in range(nr_symbols):
    password_list.append(symbols[random.randint(0, len(symbols) - 1)])
for number in range(nr_numbers):
    password_list.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(password_list)

password = ""
for character in password_list:
    password += character

print(f"Your password is: {password}")

# Testing
# -----------------------------------
# indices = [0, 1, 2, 3, 4]
# alphabet = ["a", "b", "c", "d", "e"]
# indices_count = len(indices)
#
# for number in indices:
#     random_index = random.randint(0, indices_count - 1)
#     print(alphabet[random_index])
#     alphabet.remove(alphabet[random_index])
#     indices_count -= 1
