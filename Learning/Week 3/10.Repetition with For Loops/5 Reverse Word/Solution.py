print ("What phrase do you see?")
phrase = input()

print ("\nReversing...\nThe phrase is")

#array starts from 0
for pos in range(len(phrase) - 1, -1, -1):
    print (phrase[pos], end="")

print()