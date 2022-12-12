matrix_A = [
    [1,2],
    [3,4]
]

matrix_B = [
    [5,6],
    [7,8]
]

matrix_C = [
    [None,None],
    [None,None]
]

### YOUR CODE STARTS HERE

# This line approaches the columns and rows of metrics using nested loop.
# i approaches the row.
for i in range(2):
    # j approaches the column.
    for j in range(2):
        # This line adds the numbers in the same row, column of matirx_A and matrix_B to matrix_C.
        matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j]
### YOUR CODE ENDS HERE

print(matrix_C)

"""
### YOUR EXPLANATION STARTS HERE

This program outputs the sum of metrics.

### YOUR EXPLANATION ENDS HERE
"""