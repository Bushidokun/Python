from functions import box, lowerCase, UPPERCase, mirrored, repeat

print ("""Choose one of the following:
1) Display in a Box
2) Display in Lower-case
3) Display in Upper-case
4) Display Mirrored
5) Repeat""")

response = str(input())
print()

print ("Please enter word")
word = input()
print()

if (response  == "5" or response == "Repeat"):
    print ("Repeat how many times?")
    count = int(input())
    print()
    repeat(word, count)
elif (response == "1" or response == "Display in a Box"):
    box(word)
elif (response == "2" or response == "Display in Lower-case"):
    lowerCase(word)
elif (response == "3" or response == "Display in Upper-case"):
    UPPERCase(word)
elif (response == "4" or response == "Display Mirrored"):
    mirrored(word)
else:
    print ("I can't do that.")

#1) Display in a Box – display the word in an ascii art box
#2) Display Lower-case – display the word in lower-case e.g. hello
#3) Display Upper-case – display the word in upper-case e.g. HELLO
#4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
#5) Repeat– ask the user how many times to display the word and 
# then display the word that many times alternating between uppercase and lower-case.