def display_ladder(steps):
    while (steps > 0):
        print ("|   |")
        print (" *** ")
        steps -= 1

def create_ladder():
    print ("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()