#Password Generator Project

# Below are all the keys that can be used to create a password.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

'''
If you want game to randomly decide the number of entry's

nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

'''

# Creating inputs depending on what the user wants.
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

empty = []
for i in range(nr_letters):
    empty.append(random.choice(letters))
for i in range(nr_symbols):
    empty.append(random.choice(symbols))
for i in range(nr_numbers):
    empty.append(random.choice(numbers))


# Note: There are many ways of doing this but the following are two different ways
# total = "".join(empty)
# for j in range(len(total)):
#     rand = random.choice(total)
#     print(rand, end= "")

random.shuffle(empty)
print("".join(empty))
