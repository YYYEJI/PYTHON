scores = [
    25, 32, 55, 0, 61,
    24, 89, 88, 53, 64,
    58, 80, 2, 4, 44,
    30, 6, 50, 37, 82,
    95, 22, 82, 86, 10,
    5, 70, 94, 27, 32,
    13, 63, 79, 1, 57,
    99, 55, 22, 87, 39,
    87, 17, 64, 63
]

new_score = input("Score? ")
### YOUR CODE STARTS HERE
# This line uses the sum function to add all the values in the list to the newly created variable.
total = sum(scores)

# This line adds up the scores entered by the user.
total += int(new_score)
# This line is averaging the scores.
average = total/45

# This line prints the average.
print("Average = ", average)

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This program calculates the average by adding the scores in the scores list and the scores enterd by the user.
Finally, this program prints the average.

### YOUR EXPLANATION ENDS HERE
"""