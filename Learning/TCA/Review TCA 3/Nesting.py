print ("Welcome to the Planet of the Apes...")
humanTotal = 0
apeTotal = 0

for loop in range(7):
    print ("...be ye human or be ye ape?")
    userBe = input()

    if userBe == "Human":
        humanTotal += 1
        print ("I did not start this war. But I will finish it.")
    elif userBe == "Ape":
        apeTotal += 1
        print ("Apes together strong!")
    else:
        print ("This is not your fight.")

print ("Total human encountered:", humanTotal)
print ("Total apes encountered", apeTotal)