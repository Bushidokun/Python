# Ask user for numbers
print ("How many numbers do you want?")
numbers = int(input())

# Build an array containing all numbers
array = []
Size = 0
Pos = 0
while numbers > 0:
    Size += 1
    print("Enter number", Size)
    number = int(input())

    array.append(number)
    numbers -=1

# Determine which numbers are even and which are odd
oddNumbers = 0
evenNumbers = 0
while Size > 0:
    if (array[Pos] % 2 == 1):
        oddNumbers += 1
    else:
        evenNumbers += 1
    Size -= 1
    Pos += 1

# Display result
print ("Odd numbers =", oddNumbers,"\nEven Numbers =", evenNumbers)