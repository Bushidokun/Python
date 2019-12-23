from functions import ASCII, leftAlign, rightAlign

print ("Enter a 5 digit number")
number = input()

print ("""Choose one of the following:
1) Display ASCII Triangle
2) Display Left Digits Triangle
3) Display Right Digits Triangle""")
display = input()
print()

if display == "1" or display == "Display ASCII Triangle" or display == "Triangle":
    ASCII(number)
elif display == "2" or display == "Display Left Digits Triangle" or display == "Left":
    leftAlign(number)
elif display == "3" or display == "Display Right Digits Triangle" or display == "Right":
    rightAlign(number)
else:
    print ("I can't do that.")