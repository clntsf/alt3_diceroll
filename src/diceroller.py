from random import randint
from collections import Counter
from time import sleep, time

def display_welcome_msg() -> None:
    print("\nWelcome to the diceroll program! here you can choose a number of 6-sided dice to roll, and how many times to roll.")
    print("The program will then sum each of these rolls and display the probability of the possible sums occurring by number\n")


def get_diceroll_counter(num_rolls: int, num_dice: int):
    sums = [ sum([
        randint(1,6) for d in range(num_dice)
        ]) for r in range(num_rolls)
    ]
    return Counter(sums)


def display_probabilities(disp_by_prob: bool, counter: Counter, num_rolls: int):

    if disp_by_prob:                    # sort by occurrence (desc.)
        prob = counter.most_common()
    else:                               # sort by first item (result number)
        prob = sorted(counter.items(), key = lambda n:n[0])

    print(f"\n\t\tResults: \n{'-'*40}\n")
    for (k,v) in prob:
        print(f"Sum of {k}: {v} rolls ({round(100*v/num_rolls,3)}% chance)")


def main():

    display_welcome_msg()                                           # printing welcome message
    sleep(0.5)

    num_dice = int(input("Number of dice to roll: ")); sleep(0.2)   # getting user inputs
    num_rolls = int(input("Number of dice-rolls: ")); sleep(0.2)
    disp_by_prob = ( input("Display possible sums by decreasing probability? (y/n): ").lower() == "y" )

    t0 = time()
    sum_counter = get_diceroll_counter(num_rolls, num_dice)         # getting the counter

    el = time()-t0          # shortening sleep by the runtime of get_diceroll_counter() to standardize wait time
    sleep( max(0, 0.5-el) )

    display_probabilities(disp_by_prob, sum_counter, num_rolls)     # print the probability display readout


if __name__ == "__main__":
    main()