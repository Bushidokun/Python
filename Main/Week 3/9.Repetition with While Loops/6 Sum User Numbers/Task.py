print ("How many numbers should I sum up?")
numbers = []
pos = 1 
size = int(input())
total = 0

while (size >= pos):
    print ("Please enter number", pos, "of", size)
    value = int(input())
    numbers.append(value)

    pos += 1
    total = total + value

print ("The answer is", total)
