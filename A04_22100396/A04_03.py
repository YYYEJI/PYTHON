success = False

### YOUR CODE STARTS HERE

# This line sets the password to compare it with the password entered by the user.
password = "2CO8:21"

# This line declares a variable to limit the number of user inputs.
i = 0

# This line iterates the while statement 3 times.
while i<3:
    # This line receives a password from the user.
    user_p = input("Enter your password: ")
    # This line checks if it is a valid password.
    if(user_p == password):
        # This line replaces the success variable with true if the password is valid.
        success = True
        # This line ends the while statement when the password is valid.
        break
    # This line increases the number of i variables by one each time it is entered by the user.
    i = i+1


### YOUR CODE ENDS HERE

if success:
    print("Access granted!")
else:
    print("Your account is locked.")

"""
### YOUR EXPLANATION STARTS HERE
This is a program that checks whether the password entered by the user is valid.
### YOUR EXPLANATION ENDS HERE
"""    