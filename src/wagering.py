import numpy as np

# Config (adjustable)
num_rolls = int(1e7)
odds = 6
play_cost = 10.00
seven_chance = 0.2

# Player selection odds setup
other_chance = (1-seven_chance)/10  # chance of a non-seven guess

poss_guesses = np.arange(2,13)
guess_probs = np.where(poss_guesses==7, seven_chance, other_chance)

# Calculations
guesses: np.ndarray = np.random.choice(     # player guesses (weighted with guess prob of sevens/others)
    poss_guesses,
    size=num_rolls,
    p=guess_probs
)
roll_sums: np.ndarray = sum( np.random.randint(     # sums of computed rolls 
    1, 7, size=(2,num_rolls)
))

profits = sum(np.where(guesses==roll_sums, -odds*play_cost, play_cost))
ppp = round(profits/num_rolls,5)                                        # profit per play
pct_ppp = (ppp/play_cost*100)                                           # ... as a pct of buy-in cost

# Results
print("\nAt a cost per play of ${:,.2f}:\n{}\n".format(play_cost, '*'*40))
print("Total profits in {:,} plays: ${:,.2f}".format(num_rolls, profits))
print("For every play, the house makes ${:,.2f} ({:.3f}% of each buy-in)".format(ppp, pct_ppp))