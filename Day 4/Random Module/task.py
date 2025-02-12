import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

random_heads_or_tails = random.randint(1, 2)
if random_heads_or_tails == 1:
    print("Tails")
else:
    print("Heads")