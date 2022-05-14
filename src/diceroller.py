from numpy.random import randint
from collections import Counter
from time import sleep, time
from prob_calc import get_sum_freq_list

def display_welcome_msg() -> None:
    print("\nWelcome to the diceroll program! here you can choose a number of 6-sided dice to roll, and how many times to roll.")
    print("The program will then sum each of these rolls and display the probability of the possible sums occurring by number")

def get_diceroll_counter(num_rolls: int, num_dice: int):
    rolls = randint(1,7,size=(num_dice,num_rolls))
    return Counter(sum(rolls))

def display_probabilities(disp_by_prob: bool, counter: Counter, num_rolls: int, ideals: dict[int, float] | None):

    if disp_by_prob:                    # sort by occurrence (desc.)
        prob = counter.most_common()
    else:                               # sort by first item (result number)
        prob = sorted(counter.items(), key = lambda n:n[0])

    # formatting the output
    lj1 = len(str( max(counter.keys()) )) + 7
    lj2 = len(str( max(counter.values()) )) + 6

    print(f"\n\t\tResults: \n{'-'*40}\n")
    for (k,v) in prob:
        # print(f"Sum {k} | Rolls {v} | pct {100*v/num_rolls}% | ideal % {ideals[k]}")
        ideal_str = f" / {ideals[k]}% ideal)" if ideals != None else ")"
        cols = [
            f"Sum of {k}".ljust(lj1),
            f"{v} rolls".ljust(lj2),
            f"({ round(100*v/num_rolls,3) }% chance" + ideal_str
        ]
        print(" | ".join(cols))

def main():

    display_welcome_msg()                                           # printing welcome message
    sleep(0.3)

    num_dice = int(input("\nNumber of dice to roll: ")); sleep(0.2)   # getting user inputs
    num_rolls = int(input("Number of dice-rolls: ")); sleep(0.2)
    disp_by_prob = ( input("Display possible sums by decreasing probability (y) or by result number (n): ").lower() == "y" )

    disp_ideal = ( input("Display ideal probabilities alongside simulated? (y/n): ").lower() == "y" )   # getting idealized values
    ideal_vals = dict(get_sum_freq_list(num_dice, 6)) if disp_ideal else None

    t0 = time()
    sum_counter = get_diceroll_counter(num_rolls, num_dice)         # getting the counter

    el = time()-t0          # shortening sleep by the runtime of get_diceroll_counter() to standardize wait time
    sleep( max(0, 0.3-el) )

    display_probabilities(disp_by_prob, sum_counter, num_rolls, ideal_vals)     # print the probability display readout

if __name__ == "__main__":
    main()