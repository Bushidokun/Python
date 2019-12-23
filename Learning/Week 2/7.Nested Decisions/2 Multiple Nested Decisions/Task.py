print ("Where should I look?")
response = input()

if response == "in the bedroom":
    print ("Where in the bedroom should I look?")
    bedroomWhere = input ()
    
    if bedroomWhere == "under the bed":
        print ("Found some shoes but no battery")
    else:
        print ("Found some mess but no battery.")
elif response == "in the bathroom":
    print ("Where in the bathroom should I look?")
    bathroomWhere = input()

    if bathroomWhere == "in the bathtub":
        print ("Found a rubber duck but no battery")
    else:
        print ("Found a wet surface but no battery")
elif response == "in the lab":
    print ("Where in the lab should I look?")
    labWhere = input()

    if labWhere == "on the table":
        print ("Yes! I found my battery!")
    else:
        print ("Found some tools but no battery.")
else:
    print ("I do not know where that is but I will keep looking.")