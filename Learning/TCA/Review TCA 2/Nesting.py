health = 100
print ("Your health is", health, "%. Escape is in progress...\n")

for action in range(5):
    print ("...Oh dear, who is that?")
    responseWho = str(input())

    if responseWho == "Smiler's Bot":
        health = health - 20
        print ("Time to jam out of here!")
    elif responseWho == "Hacker":
        health = health + 20
        print ("Yay! Better follow this one!")
    else:
        print ("Phew, just another emoji!")
    print()

print ("Escaped! Health is", health, "%.")