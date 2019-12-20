print ("How many zones must I cross?")
zonesMany = int(input())

print ("Crossing zones...")

for crossed in range(zonesMany, 0, -1):
    print ("...crossed zone", crossed)

print ("Crossed all zones. Jumanji!")