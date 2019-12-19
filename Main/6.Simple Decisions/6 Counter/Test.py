print ("how many numbers you want?")
numbers = int(input())
array = []
x=0
y=0
while numbers > 0:
    x += 1
    print("input number", x)
    number = int(input())
    
    array.append(number)
    numbers -=1

print(array[0])
while x >0:
    
    if (array[y] % 2 == 0):
        print ("even")
    else:
        print ("odd")
    
    y+=1
    x-=1

print(array[0])


