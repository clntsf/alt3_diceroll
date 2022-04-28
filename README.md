# Dice-rolling Probability Simulator
#### *by Colin Simon-Fellowes*
---

### Prompt

Simulating two dice work approximate the odds of the sum of the dice adding up to the numbers 2-12

Make the code flexible so it can handle more than two dice

### General Process

Roll all dice n times, and each time
 - roll each dice and sum the results
 - add this result to a list of previous results

display statistics based on the items in this list

### Useful modules / functions / objects

*collections.Counter* - for getting occurence statistics from a list of numbers
*time.sleep* - to sleep the process for small durations, just for looks
*random.randint* - to generate random integers in the range [1,6] for the dicerolls

---

### Algorithm / Pseudocode

1. get input from user:
    - number of dice to roll each go
    - number of total rolls to perform
    - Whether to display diceroll statistics by descending probability or by ascending result number (i.e. 2-12)

2. Perform and record the dicerolls (for loop)
 - sums = []
 - for i=0 -> i=(# of dice rolls)
    - sum = 0
    - for j=0 -> j=(# dice to roll)
        - get a random number one to 6
        - add to sum

    - add sum to sums

3. display the statistics
 - turn sums into a *collections.Counter* object
 - display by desc. probability or by result number based on user's choice

