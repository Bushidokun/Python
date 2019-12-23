print ("Towards which direction should I paint (up, down, left or right)?")

direction = input()

if (direction == "up" or direction == "down"):
    #removes spaces between elements
    print ("I am painting in the ", direction, "ward direction!", sep='')
    #add(+) concatenates
    print ("I am painting in the", direction + "ward direction!",)
elif (direction == "left" or direction == "right"):
    print ("I am painting in the", direction, "direction!")
else:
    print ("I don't know that direction!")