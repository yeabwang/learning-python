import random

class Dice:
    def roll(self):
        i = random.randint(1,6)
        j = random.randint(1,6)     
        return i,j
    
person1 = Dice()

print(person1.roll())