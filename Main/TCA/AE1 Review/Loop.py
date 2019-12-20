print ("How many miles must I travel before I reach the secret base?")

distance = int(input())

print ("I will count the miles...")

for milesLeft in range(distance, 0, -1):
    print ("I have", milesLeft, "miles to go before I reach the base.")

print ("""\nI have arrived at the secret headquarters of the MIB!
It is time to sneak in.""")