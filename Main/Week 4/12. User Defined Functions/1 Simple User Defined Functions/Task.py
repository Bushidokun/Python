def listen():
    print ("What sound did I hear?")
    whatSound = input()

    print ("That was a loud ", end="")
    print (whatSound, "!", sep="")

listen()