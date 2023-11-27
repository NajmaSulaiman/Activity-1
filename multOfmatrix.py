matrix1 = [[1,2,3],
          [6,7,8]]

matrix2 = [[6,1],
          [2,10],
           [0,2]]


def mult_matrix(matrix1,matrix2):
    matrix3=[[0,0],[0,0]]
    
    for row in range(len(matrix1)):
        for column in range(len(matrix2[0])):
            for row2 in range(len(matrix2)):
                matrix3[row][column]+=matrix1[row][row2]*matrix2[row2][column]
    return matrix3

print(mult_matrix(matrix1,matrix2)) 
