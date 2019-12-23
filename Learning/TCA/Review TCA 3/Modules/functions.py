def ASCII(number):
    for length in range(10):
        if length + 1 == 9:
            print ("*", number, "*")
        else:
            print ("*" * (length + 1))

def leftAlign(number):
    for length in range (len(number)):
        for pos in range (length + 1):
            print (number[pos], end="")
        print()

def rightAlign(number):
    for length in range (len(number)):
        print ( " " * (len(number) - (length + 1)), end="")
        for pos in range (length + 1):
            print (number[pos], end="")
        print ()