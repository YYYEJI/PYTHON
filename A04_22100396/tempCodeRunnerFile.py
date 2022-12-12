in range(2):
    # j approaches the column.
    for j in range(2):
        # This line adds the numbers in the same row, column of matirx_A and matrix_B to matrix_C.
        matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j]
### YOUR CODE ENDS HERE

print(matrix_C)
