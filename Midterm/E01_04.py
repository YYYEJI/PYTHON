from E01_01 import load_data
lines = load_data()
### YOUR CODE STARTS HERE
# This line creates a new Bible dictionary.
bible = {}

# This line checks the values in the lines list one by one.
for line in lines:
    # This line removes the front and back spaces from the string contained in the chapter variable.
    chapter = line.strip()
    # This line divides the string by "|".
    chapter = line.split("|")
    # This line stores the split string as a tuple except for Bible text.
    b = (chapter[0] , chapter[1], chapter[2])
    # This line puts text in the key value of the dictionary containing name of book, chapter number and verse number.
    bible[b] = chapter[3].strip()

# This line print the text of 1 Peter 4:13 on the screen.
print(bible[('Pe1', '4', '13')])


### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This program was created to find Bible verses easily. 
If you enter the name of book, chapter number, verse number as a key in advance and enter the name of book, chapter number and verse number as a key value, the Bible text is printed.

### YOUR EXPLANATION ENDS HERE
"""