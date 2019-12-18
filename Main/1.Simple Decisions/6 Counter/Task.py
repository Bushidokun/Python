print ("how many numbers you want?")
numbers = int(input())
array = []

while numbers > 0:
    x = 1
    print("input number", x)
    number = int(input())
    x += 1
    array.append(number)
    numbers -=1

while x >1:
    y = 0
    if (array[y] % 2 == 0):
        print ("The second number is the smallest!")
    else:
        print ("They are equal!")
    
    y+=1
    x-=1


