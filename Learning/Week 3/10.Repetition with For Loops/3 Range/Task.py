print ("What level of brightness is required?")
response = int(input())

print ("Adjusting brightness...")

for count in range (2, response + 1, 2):
    print ("\nBeep's brightness level:", "*" * count)
    print ("Bop's brightness level:", "*" * count)

print ("\nAdjustment complete!")