from E01_01 import load_data
lines = load_data()
### YOUR CODE STARTS HERE
# This line creates a new Bible list.
bible = []

# This line checks the values in the lines list one by one.
for line in lines:
    # This line removes the front and back spaces from the string contained in the chapter variable.
    chapter = line.strip()
    # This line divides the string by "|".
    chapter = line.split("|")
    # This line stores the split string as a tuple.
    b = (chapter[0] , chapter[1], chapter[2], chapter[3])
    # This line adds the created tuples to the Bible list.
    bible.append(b)


#  found_text variable to hold the found text.
found_text = ""
# This line iterates until the last index of the bible list.
for find_text in range(len(bible)):
    # This line find a book of 2 Peter.
    if(bible[find_text][0]!="Pe2"):
        # This line pass this for loop.
        continue
    # This line find a chapter 1.
    if(bible[find_text][1]!="1"):
        # This line pass this for loop.
        continue
    # This line find a verse 10.
    if(bible[find_text][2]!="10"):
        # This line pass this for loop.
        continue
    # This line puts the text in the found_text variable if it find 2 Peter 1:10.
    found_text = bible[find_text][3].strip()
    # This line stop this for loop.
    break

# This line prints the found text on the screen.
print(found_text)


### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This program saves a single string divided by name of book, chapter number, verse number, text.

### YOUR EXPLANATION ENDS HERE
"""