# Ask user for the type of book

print("What type of book is this?")
book_type = input()

# Determine if the book is an adventure book

if (book_type == "adventure"):
    print("\nI love", book_type, "books!")
elif (book_type == "horror"):
    print("\nI hate", book_type, "books.")
else:
    print("\nI like", book_type, "books!")

# Display message

print("\nFinished reading book.")