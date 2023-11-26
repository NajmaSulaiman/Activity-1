matrix1 = [[2,5,1],
          [4,9,0],
          [11,6,7]]

matrix2 = [[5,5,1],
          [5,8,1],
          [9,2,6]]

def sum_matrix(matrix1,matrix2):
    matrix3=[]
    
    for row in range(len(matrix1)):
        rows=[]
        for column in range(len(matrix1)):
            rows.append(matrix1[row][column]+matrix2[row][column])
            
        matrix3.append(rows)
    print(matrix3)

sum_matrix(matrix1,matrix2)

        
    
        