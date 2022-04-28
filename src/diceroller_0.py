from random import randint
from collections import Counter
from time import sleep, time

print("\nWelcome to the diceroll program! here you can choose a number of 6-sided dice to roll, and how many times to roll.")
print("The program will then sum each of these rolls and display the probability of the possible sums occurring by number\n")
sleep(0.5)

num_dice = int(input("Number of dice to roll: ")); sleep(0.2)
dicerolls = int(input("Number of dice-rolls: ")); sleep(0.2)
disp_by_prob = ( input("Display possible sums by decreasing probability? (y/n): ").lower() == "y" )

t0 = time()
sums = [ sum([
    randint(1,6) for d in range(num_dice)
    ]) for r in range(dicerolls)
]
sum_counter = Counter(sums)

if disp_by_prob: prob = sum_counter.most_common()
else: prob = sorted(sum_counter.items(), key = lambda n:n[0])

el = time()-t0
sleep( max(0, 0.5-el) )

print(f"\n\t\tResults: \n{'-'*40}\n")
for (k,v) in prob:
    print(f"Sum of {k}: {v} rolls ({round(100*v/dicerolls,3)}% chance)")