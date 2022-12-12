from E01_01 import load_data
lines = load_data()

### YOUR CODE STARTS HERE
# This line checks the values in the lines list one by one.
for chap in lines:
    # This line verifies that the chap variable contains the string "Pe1|4|7|".
    if "Pe1|4|7|" in chap:
            # If this chap variable contains the "Pe1|4|7|" string, it puts the string of chpa variable into the chapter variable.
            # And then this line divides the found text by "|".
            chapter = chap.split("|")
            # This line contains only text in text variables and then removes the front and back spaces from the text.
            text = chapter[3].strip()
            # And this lins stops the For statement.
            break



# This line prints a text on the screen.
print(text)



## YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This program finds and prints a string containing "Pe1|4|7|".

### YOUR EXPLANATION ENDS HERE
"""