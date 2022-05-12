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

### Making Changes

Version 1 (see *[src/diceroller_0.py](https://raw.githubusercontent.com/ctsf1/alt3/master/src/diceroller_0.py)*) - Main program and control flow created

Version 2 (see *[src/diceroller_1.py](https://raw.githubusercontent.com/ctsf1/alt3/master/src/diceroller_1.py)*) - Wrapped the various components in functions for clarity

Version 3 (Current) (see *[src/diceroller.py](https://raw.githubusercontent.com/ctsf1/alt3/master/src/diceroller.py)*) - switched to using *numpy.random.randint* for calculating dicerolls, as it allows for the calculation of all the rolls at once, and is faster than looping through manually

Version 3.5 - Added idealized percentages to the display by way of [src/prob_calc.py](https://raw.githubusercontent.com/ctsf1/alt3/master/src/prob_calc.py)

### Conclusions

 - An initially daunting problem is made much more simple by designing and implementing the bare-bones of the algorithm and fleshing it out as we go
 - By using Python's existing support for modules we can refactor our code to accelerate it by many tens/hundreds of times compared to a naïve implementation
 - While a program's performance is ultimately its most important aspect, it is incredibly difficult for others to understand it, take inspiration from it or maintain it if it is not made readable by following clean coding habits