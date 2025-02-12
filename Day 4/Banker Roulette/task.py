import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randomFriend = random.randint(0, len(friends) - 1)

print(friends[randomFriend])
print(random.choice(friends))
