print ("Please enter a sequence")
sequence = input()

print("Please enter the character for the marker")
marker = input()

print ("The distance between the markers is ", end="")

dash = 0
for count in range(0, len(sequence), 1):
    if marker in sequence[count]:
        pass
    else:
        dash +=1

print (dash)