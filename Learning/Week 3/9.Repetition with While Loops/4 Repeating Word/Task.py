print ("Please enter a phrase:")
phrase = input()
bops = 0

print ("Bop " * len(phrase))

while (len(phrase) > bops):
    print ("Bop ", end="")
    bops += 1

#two solutions