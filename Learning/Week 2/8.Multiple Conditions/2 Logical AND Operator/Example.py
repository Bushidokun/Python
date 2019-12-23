#Retrieve size and weight from user
print("What size is the parcel?")
size = input()

print("What is weight of the parcel?")
weight = input()

# Identify and display the category
if ((size == "big") and (weight == "heavy")):
    print("This parcel will be expensive to deliver.")
else:
    print("This parcel will be inexpensive to deliver.")