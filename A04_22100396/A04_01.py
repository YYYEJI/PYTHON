books = [
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
    "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
    "Habakkuk", "Zephaniah", "Haggai", "Micah", "Zechariah", "Malachi"
]

unique = []
### YOUR CODE STARTS HERE

# This line uses a for statement for duplicate checks.
for book in books:
    # This line puts the values in the books list one by one in the unique list, but it doesn't if it's already.
    if book not in unique:
        # If the value is not in the unique list, append the element in unique list.
        unique.append(book)
        

    

### YOUR CODE ENDS HERE
print(unique)

"""
### YOUR EXPLANATION STARTS HERE

It is a program that prints values except for duplicate values in the books list in a unique list.

### YOUR EXPLANATION ENDS HERE
"""