def isFusionShot(slugType1, slugType2):
    if slugType1 == slugType2:
        return True
    else:
        return False

def isDefectiveShot(slugType1, slugType2):
    if isFusionShot(slugType1, slugType2) is False and slugType1 == "Infurnus" and  slugType2 == "AquaBeek" or slugType1 == "AquaBeek" and slugType2 == "Infurnus":
        return True
    else:
        return False

def run():
    print ("What is the first slug type?")
    slugType1 = input()
    print ("What is the second slug type?")
    slugType2 = input()

    print ("fusion or defective?")
    shotType = input()

    if shotType == "fusion":
        if isFusionShot(slugType1, slugType2) is True:
            print ("True")
        elif isFusionShot(slugType1, slugType2) is False:
            print ("False")
        else:
            print ("What")
    elif shotType == "defective":
        if isDefectiveShot(slugType1, slugType2) is True:
            print ("True")
        elif isDefectiveShot(slugType1, slugType2) is False:
            print ("False")
        else:
            print ("What")
    else:
        print ("Invalid selection. Please try again.")

run()