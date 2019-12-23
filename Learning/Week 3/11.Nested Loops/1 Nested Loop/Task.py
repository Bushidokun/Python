print ("How many rows should I have?")
rows = int(input())

print ("How many columns should I have?")
columns = int(input())

print ("Here I go:")

for rowCount in range( 0, rows, 1):
    for columnCount in range( 0, columns, 1):
        print (":-) ", end="")
    print()

print("Done!")