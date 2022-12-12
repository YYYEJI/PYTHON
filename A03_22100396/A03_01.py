def read_test_data(filename):
    data = []
    with open(filename, "rt") as fin:
        lines = fin.read().strip().split("\n")
        for line in lines:
            row = line.split(" ")
            data.append(row)
    return data
    
def display_board(data):
    for row in data:
        print(" ".join(row))

# filename="test-data.txt"
# /Users/song-yeji/Desktop/p/A03_22100396/test-data.txt
tic_tac_toe = read_test_data(filename="/Users/song-yeji/Desktop/p/A03_22100396/test-data.txt")
print("== 3x3 Matrix (a list in a list) ==")
print(tic_tac_toe)
print()
print("== Tic-Tac-Toe Board ==")
display_board(tic_tac_toe)


### YOUR CODE STARTS HERE

# This line verifies that the first row of the matrix is filled with the same alphabet.
if(tic_tac_toe[0][0] == tic_tac_toe[0][1] and tic_tac_toe[0][0] == tic_tac_toe[0][2]):
    # If first row of the matrix is filled with x, output it as x.
    if(tic_tac_toe[0][0] == "X"):
        print("X won!")
    # If first row of the matrix is filled with o, output it as o.    
    else:
        print("O won!")
# This line verifies that the second row of the matrix is filled with the same alphabet.
elif(tic_tac_toe[1][0] == tic_tac_toe[1][1] and tic_tac_toe[0][1] == tic_tac_toe[1][2]):
    # If second row of the matrix is filled with x, output it as x.
    if(tic_tac_toe[1][0] == "X"):
        print("X won!")
    # If second row of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the third row of the matrix is filled with the same alphabet.
elif(tic_tac_toe[2][0] == tic_tac_toe[2][1] and tic_tac_toe[2][1] == tic_tac_toe[2][2]):
    # If third row of the matrix is filled with x, output it as x.
    if(tic_tac_toe[2][0] == "X"):
        print("X won!")
    # If third row of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the first column of the matrix is filled with the same alphabet.
elif(tic_tac_toe[0][0] == tic_tac_toe[1][0] and tic_tac_toe[1][0] == tic_tac_toe[2][0]):
    # If first column of the matrix is filled with x, output it as x.
    if(tic_tac_toe[0][0] == "X"):
        print("X won!")
    # If first column of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the second column of the matrix is filled with the same alphabet.
elif(tic_tac_toe[0][1] == tic_tac_toe[1][1] and tic_tac_toe[1][1] == tic_tac_toe[2][1]):
    # If second column of the matrix is filled with x, output it as x.
    if(tic_tac_toe[0][1] == "X"):
        print("X won!")
     # If second column of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the third column of the matrix is filled with the same alphabet.
elif(tic_tac_toe[0][2] == tic_tac_toe[1][2] and tic_tac_toe[1][2] == tic_tac_toe[2][2]):
    # If third column of the matrix is filled with x, output it as x.
    if(tic_tac_toe[0][2] == "X"):
        print("X won!")
     # If third column of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the right diagonal of the matrix is filled with the same alphabet.
elif(tic_tac_toe[0][0] == tic_tac_toe[1][1] and tic_tac_toe[1][1] == tic_tac_toe[2][2]):
    # If the diagonal of the matrix is filled with x, output it as x.
    if(tic_tac_toe[0][0] == "X"):
        print("X won!")
    # If the diagonal of the matrix is filled with o, output it as o.
    else:
        print("O won!")
# This line verifies that the left diagonal of the matrix is filled with the same alphabet.
elif(tic_tac_toe[2][0] == tic_tac_toe[1][1] and tic_tac_toe[1][1] == tic_tac_toe[2][0]):
    # If the diagonal of the matrix is filled with x, output it as x.
    if(tic_tac_toe[2][0] == "X"):
        print("X won!")
    # If the diagonal of the matrix is filled with o, output it as o.
    else:
        print("O won!")


### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE

This program is a game that wins if one line becomes a bingo regardless of the horizontal, vertical, or diagonal line.
There are x, o, and the output depends on who wins. If O wins, it outputs "O win!" and if x wins, it outputs "X win!" 


The given problem is shown below, and "X won!" is output because the left diagonal is filled with x.
O X X
O X O
X O X


### YOUR EXPLANATION ENDS HERE
"""