### YOUR CODE STARTS HERE
# This list is a list where characters in bible-3letter.txt will be stored.
shortName = []
# This list is a list where characters in bible-fullname.txt will be stored.
longName = []

# This line opens the bible-3letter.txt.
file_s = open("/Users/song-yeji/Desktop/p/A09_22100396/bible-3letter.txt", "rt")

# Use a while statement where the conditional statement is true
while True:
    # Read the contents of the file one line at a time
    f = file_s.readline()
    # If it doesn't read,
    if f == '':
        # End the while statement.
        break
    # Add read content to the shortName list one by one.
    shortName.append(f.strip())

# This line removes the wrong content from the shortName list.
shortName.remove("Ahh")

# This line closes the file.
file_s.close

# This line opens the bible-fullname.txt.
file_l = open("/Users/song-yeji/Desktop/p/A09_22100396/bible-fullname.txt", "rt")
# Use a while statement where the conditional statement is true
while True:
    # Read the contents of the file one line at a time
    f = file_l.readline()
    # If it doesn't read,
    if f == '':
        # End the while statement.
        break
    # Add read content to the longName list one by one.
    longName.append(f.strip())


# This line removes the wrong content from the longName list.
file_l.close()

# This line makes a full2abbrev dictionary.
full2abbrev = {}
# This line makes a abbrev2full dictionary.
abbrev2full = {}

# This line rotates for for statement as many times as the list.
for i in range(len(longName)):
    # In this dictionary, the value of loneName becomes the key and the value of shortName becomes the value.
    full2abbrev[longName[i]] = shortName[i]
     # In this dictionary, the value of shortName becomes the key and the value of longName becomes the value.
    abbrev2full[shortName[i]] = longName[i]


### YOUR CODE ENDS HERE

print(full2abbrev["Genesis"])
print(full2abbrev["Matthew"])
print(full2abbrev["1 Peter"])
print(full2abbrev["Isaiah"])

print(abbrev2full["Exo"])
print(abbrev2full["Rom"])

"""
### YOUR EXPLANATION STARTS HERE
The program reads two files, stores each data in a list, and then re-creates them into two dictionaries.
Finally, output the value according to the key value.

Then the name of the summarized Bible is printed out as the full name, and the full name of the Bible is printed out as the name of the summarized Bible.
### YOUR EXPLANATION ENDS HERE
"""


