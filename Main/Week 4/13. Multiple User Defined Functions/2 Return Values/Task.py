def sum_weights(BeepWeight, BopWeight):
    totalWeight = BeepWeight + BopWeight
    return totalWeight

def calc_avg_weight(BeepWeight, BopWeight):
    averageWeight = totalWeight / 2
    return averageWeight

def run():
    print ("What is the weight of Beep?")
    BeepWeight = int(input())
    return BeepWeight

    print ("What is the weight of Bop?")
    BopWeight = int(input())
    return BopWeight

    print ("What would you like to calculate (sum or average)?")
    calculate = input()
    
    if calculate == "sum":
        print ("The sum of Beep and Bop's weight is", sum_weights())
    elif calculate == "average":
        print ("The average of Beep and Bop's weight is", calc_avg_weight())
    else:
        print ("I can't do that.")

    

run()