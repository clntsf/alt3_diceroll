from numpy.random import randint
from collections import Counter

num_trials = int(input("num trials: "))
num_dice = int(input("num dice: "))

dice = Counter( sum( randint(1,7, size=(num_dice, num_trials)) ) )

hl="-"*10+"\n"
print(f"{hl}Results\n{hl}")
for (num,times) in dice.most_common():
    print(f"Sum of {num}: {round(times/num_trials*100, 2)}% chance")