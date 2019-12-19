print ("How many mountains should I display?")
number = int(input())

print ("Displaying...")

for count in range(number):
    print("""
      __
     /  \\_
    /^    \\
   /  ^    \\_
 _/ ^ ^      ^\\
/  ^      ^    \\
""")
    print("      __")
    print("     /  \_")
    print("    /^    \\")
    print("   /  ^     \_")
    print(" _/ ^ ^      ^\ ")
    print("/  ^       ^   \ ")

print ("Done!")