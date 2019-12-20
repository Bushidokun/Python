def box(word):
    print ("**"+("*"*len(word)))
    print ("|" + word + "|")
    print ("**"+("*"*len(word)))

def lowerCase(word):
    print(word.lower())

def UPPERCase(word):
    print(word.upper())

def mirrored(word):
    for pos in range( len(word) - 1, -1, -1):
        print ( word[pos], end="")
        
    print ()

def repeat(word, count):
    while (count > 0):
        if count % 2 == 1:
            lowerCase(word)
        else:
            UPPERCase(word)
        count -=1