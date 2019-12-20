from functions import under, over, both, grid

print ("Enter a word")
responseWord = input()

print (""" Choose an option:
1) Under
2) Over
3) Both
4) Grid""")
responseOption = input()

if responseOption == "1" or responseOption == "Under":
    under(responseWord)
elif responseOption == "2" or responseOption == "Over":
    over(responseWord)
elif responseOption == "3" or responseOption == "Both":
    both(responseWord)
elif responseOption == "4" or responseOption == "Grid":
    grid(responseWord)
else:
    print ("I can't do that.")