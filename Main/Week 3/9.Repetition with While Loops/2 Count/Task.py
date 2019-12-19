print ("How many live cables must I avoid?")
cablesLive = int(input())
cablesAvoided = 0

while (cablesLive > cablesAvoided):
    
    print ("Avoiding...", end="")
    cablesAvoided += 1
    print ("Done!", cablesAvoided, "live cables avoided")

print ("All live cables have been avoided.")