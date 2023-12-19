import random
from random import choice

for i in range(3):
    print(random.random())
    print(random.randint(10,20))


members = ["gio", "vato", "ano", "nika"]
leader = choice(members)
print(leader)


class Dise:
    def roll(self):
        random.randint(10, 20)
