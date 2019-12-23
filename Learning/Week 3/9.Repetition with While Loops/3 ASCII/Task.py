print ("How many bars should be charged?")
chargeRequest = int(input())
charged = 0

while (chargeRequest > charged):
    print ("Charging:", end="")
    charged += 1
    print ("█" * charged)

print ("The battery is fully charged.")