score1 = input("Score 1= ")
score2 = input("Score 2= ")
score3 = input("Score 3= ")
score4 = input("Score 4= ")
### YOUR CODE STARTS HERE

# This line save the entered score in list.
score_list = [int(score1), int(score2), int(score3), int(score4)]
# This line sorts the small values in the list.
score_list.sort()

# This line adds up the values of the scores except the smallest number.
total = score_list[1] + score_list[2] + score_list[3]

# This line prints average of total score.
print(total/3)

### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This is the program that takes the average except the smallest number entered.
and this program prints average of scores.

### YOUR EXPLANATION ENDS HERE
"""