x = input("x = ")
y = input("y = ")
### YOUR CODE STARTS HERE

# Space to store one of the two numbers received
tmp = x
# Put the value of y in x to change the place of the value
x = y
# Since the value of x has changed, put the x value in tmp into y.
y = tmp

### YOUR CODE ENDS HERE
# Print the value of x and y.
print("## Swapped")
print("x =", x)
print("y =", y)

"""
### YOUR EXPLANATION STARTS HERE

If one value is put into another variable, the original value disappears, so a new variable is created.
Put the value of x in the newly created variable. This changed the value of x.
In the y variable, enter the vlaue of the newly created variable that contains the value of x.

Finally, prints the exchanged variable.

### YOUR EXPLANATION ENDS HERE
"""
