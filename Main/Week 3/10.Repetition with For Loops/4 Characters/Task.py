print ("What strange markings do you see?")
symbol = input()

print ("Identifying...")

for index in range( 0, len(symbol), 1):
    print ("index", index, ":", symbol[index])

print ("Done!")