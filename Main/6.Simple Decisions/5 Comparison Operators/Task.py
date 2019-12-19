print ("Please enter the first number.")
firstnumber = int(input())

print ("Please enter the second number.")
secondnumber = int(input())

if (firstnumber > secondnumber):
    print ("The second number is the smallest!")
elif (firstnumber < secondnumber):
    print ("The first number is the smallest!")
else:
    print ("They are equal!")