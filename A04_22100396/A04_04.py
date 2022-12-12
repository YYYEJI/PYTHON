records = [["John", 90, 80, 79], ["Daniel", 84, 99, 91], ["Isaiah", 95, 80, 72]]
transcripts = {}
### YOUR CODE STARTS HERE

# This line identifies row by row through the for statement.
for i in range(3):
    # This line puts the name in Key in the transcripts dictionary, and value stores the average of student scores.
    # And this line adds up the student's score and divides it by three to get the average.
    transcripts[records[i][0]] = (records[i][1]+records[i][2]+records[i][3])/3.0


### YOUR CODE ENDS HERE
for name, avg in transcripts.items():
    print(f"{name}'s average = {avg:.2f}")
    
"""
### YOUR EXPLANATION STARTS HERE

This is a program that stores and outputs the average of students' names and scores in a transcripts dictionary related to a row.

### YOUR EXPLANATION ENDS HERE
"""    