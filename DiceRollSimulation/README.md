# Dice Simulation Using Monte Carlo Method

## Overview

This project simulates rolling a six-sided die 1000 times using a computer program.  
Instead of physically rolling a die, a Random Number Generator (RNG) is used to generate random numbers between 0 and 1.

These numbers are then mapped into intervals that represent the six faces of a die.

The program records how many times each face appears and calculates the percentage occurrence.

---

# Objective of the Assignment

The purpose of this assignment is to introduce the concepts of:

- Simulation and Modelling
- Random Number Generation
- Probability
- Monte Carlo Simulation

---

# What is Simulation?

Simulation is the process of **imitating a real-world system using a computer model**.

Instead of performing an experiment in real life, we create a digital version of the system and observe how it behaves.

Example:

Real Life | Simulation
--- | ---
Rolling a dice | Computer generates random numbers
Spread of disease | Epidemic simulation models
Traffic flow | Traffic simulation software
Stock market | Financial simulations

Simulation allows us to study systems that are expensive, dangerous, or time-consuming to test in real life.

---

# What is Modelling?

A model is a **simplified representation of a real-world system**.

Example:

A die has 6 possible outcomes.

So we model it by dividing the probability range (0–1) into six equal parts.

Each interval represents one face of the die.

---

# Random Number Generator (RNG)

A Random Number Generator produces numbers between **0 and 1**.

Example outputs:

0.12  
0.76  
0.45  
0.03  
0.89  

These numbers are used to simulate random events.

---

# Mapping Random Numbers to Dice Faces

The range 0 to 1 is divided into six equal intervals.

| Random Number Range | Dice Face |
|---|---|
| 0 – 0.1667 | 1 |
| 0.1667 – 0.3333 | 2 |
| 0.3333 – 0.5000 | 3 |
| 0.5000 – 0.6667 | 4 |
| 0.6667 – 0.8333 | 5 |
| 0.8333 – 1.000 | 6 |

Each interval represents an equal probability of **1/6**.

---

# Monte Carlo Simulation

Monte Carlo Simulation is a technique that uses **random sampling to estimate the behaviour of a system**.

Instead of solving problems mathematically, we run many random experiments and observe the results.

Example uses:

- Disease spread modelling
- Financial risk analysis
- Weather prediction
- Engineering reliability testing
- Artificial Intelligence simulations

In this assignment, the Monte Carlo method is used to simulate rolling a die **1000 times**.

---

# Law of Large Numbers

The Law of Large Numbers states that:

> As the number of experiments increases, the experimental probability approaches the theoretical probability.

For a fair die:

Theoretical probability of each face:

1/6 ≈ 16.67%

As the number of rolls increases, the results will get closer to this value.

---

# Program Logic

The simulation works as follows:

1. Generate a random number between 0 and 1
2. Determine which interval the number falls into
3. Assign the corresponding dice face
4. Repeat the experiment 1000 times
5. Count the frequency of each face
6. Calculate the percentage occurrence

---

# Output

The program produces a table showing:

- Dice face
- Frequency (number of times it appeared)
- Percentage occurrence

Example:

Face | Frequency | Percentage
--- | --- | ---
1 | 170 | 17.0%
2 | 160 | 16.0%
3 | 168 | 16.8%
4 | 165 | 16.5%
5 | 167 | 16.7%
6 | 170 | 17.0%

Total rolls = 1000

---

# Conclusion

This simulation demonstrates how computers can model random processes using probability and random number generation.

It also shows that as the number of simulations increases, the results approach the theoretical probability values.