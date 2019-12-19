print ("Please enter a number ")
number = int(input())
total = 1

while (number > 0 ):
    total = total * number
    number -= 1

print ("The factorial is", total)