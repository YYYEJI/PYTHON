search = input("?")

### YOUR CODE STARTS HERE

# This line divides the string(search) by colon.
search = search.split(":")
# This line puts the last value in the search list into the verse variable.
verse = search.pop()
# This line puts the first value of index 0 in the search list in the tmp_1 variable.
tmp_1 = search[0]
# This line only places the third character in the string in the tmp_1 in the tmp_2 variable.
tmp_2 = tmp_1[0] + tmp_1[1] + tmp_1[2]
# This line clears the characters from index 0 to 3 from the string in tmp_1.
tmp_1 = tmp_1[3:]
# This line divides the string(tml_1) by white space.
tmp_1 = tmp_1.split(" ")
# This line puts the last value in the tmp_1 list into the chapter variable.
chapter = tmp_1.pop()
# This line combines tmp_2 and the string of index 0th in the list tmp_1.
book = tmp_2 + tmp_1[0]


### YOUR CODE ENDS HERE

print("Book =", book)
print("Chapter =", chapter)
print("Verse =", verse)

"""
### YOUR EXPLANATION STARTS HERE

This is a program that puts the Bible entered by the user into each variable.

### YOUR EXPLANATION ENDS HERE
"""



