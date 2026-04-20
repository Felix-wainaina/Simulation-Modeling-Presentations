# Import the random module
# This module allows Python to generate random numbers
import random


# Create a list to store the frequency of each dice face
# Index 0 -> Face 1
# Index 1 -> Face 2
# Index 2 -> Face 3
# Index 3 -> Face 4
# Index 4 -> Face 5
# Index 5 -> Face 6
count = [0, 0, 0, 0, 0, 0]


# Total number of dice rolls in the simulation
rolls = 1000


# Loop that repeats the experiment 1000 times
for i in range(rolls):

    # Generate a random number between 0 and 1
    r = random.random()

    # Convert the random number into a dice face
    # Each interval represents one face of the die
    
    if r < 1/6:
        # Random number is between 0 and 0.1667
        # This corresponds to face 1
        count[0] += 1

    elif r < 2/6:
        # Random number between 0.1667 and 0.3333
        # Corresponds to face 2
        count[1] += 1

    elif r < 3/6:
        # Random number between 0.3333 and 0.5
        # Corresponds to face 3
        count[2] += 1

    elif r < 4/6:
        # Random number between 0.5 and 0.6667
        # Corresponds to face 4
        count[3] += 1

    elif r < 5/6:
        # Random number between 0.6667 and 0.8333
        # Corresponds to face 5
        count[4] += 1

    else:
        # Random number between 0.8333 and 1
        # Corresponds to face 6
        count[5] += 1


# Print the table header
print("Face\tFrequency\tPercentage")


# Loop through each face to display results
for i in range(6):

    # Get frequency for that face
    freq = count[i]

    # Calculate percentage
    percent = (freq / rolls) * 100

    # Print results in table format
    print(i+1, "\t", freq, "\t\t", round(percent, 1))