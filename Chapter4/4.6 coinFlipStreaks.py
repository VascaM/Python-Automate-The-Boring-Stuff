import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    
    # Creates a list of 100 H or T values.
    flips = []
    for i in range(100):
        if random.randint(0,1):
            flips.append('H')   # If condition is considered True(1). add 'H' to the 'flips' list
        else:
            flips.append('T')   # If condition is considered False(0). add 'T' to the 'flips' list

    # Checks if there is a streak of 6 'H' or 'T' in a row.
    for i in range(100 - 6): # We need 6 consecutive throws, but if there are fewer than 6 throws left to check, we can't have a streak of 6
        if flips[i] == flips[i+1] == flips[i+2] == flips[i+3] == flips[i+4] == flips[i+5]:
            numberOfStreaks += 1
            break # We only count one streak per 100 flips.

chance_percentage = (numberOfStreaks / 10000) * 100
print('Chance of streak:', int(chance_percentage), '%')

