def under(responseWord):
    print (responseWord)
    print ("*" * len(responseWord))
    return 

def over(responseWord):
    print ("*" * len(responseWord))
    print (responseWord)
    return

def both(responseWord):
    print ("*" * len(responseWord))
    print (responseWord)
    print ("*" * len(responseWord))
    return

def grid(responseWord):
    print ("What size grid?")
    gridSize = int(input())

    for rows in range(gridSize+1):
        for wordColumn in range(gridSize):
            if rows == 0:
                print()
            elif wordColumn < gridSize-1:
                print (responseWord, " | ", end="")
            else:
                print (responseWord)
        for lineColumn in range(gridSize):
            print ("*" * len(responseWord), "   ", end="")
        print()
    return