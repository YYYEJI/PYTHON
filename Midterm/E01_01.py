def load_data():
    # I changed the location of the file.
    # /Users/song-yeji/Desktop/p/midterm/peter.txt
    with open("peter.txt", "rt") as fin:
        data = fin.read()
    
    ### YOUR CODE STARTS HERE
    # This line divides the string by "~\n".
    lines = data.split("~\n")
    # I pop one because there is a blank value at the end of the lines list index.
    lines.pop()
    # This line returns the result.
    return lines
    ### YOUR CODE ENDS HERE



lines = load_data()