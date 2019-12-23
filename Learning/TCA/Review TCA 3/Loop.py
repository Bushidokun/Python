print ("How many heroes must we gather?")
howMany = int(input())

print ("Gathering heroes...")

for gathered in range(howMany):
    print ("...found hero", gathered + 1)

print ("...all heroes have been gathered")