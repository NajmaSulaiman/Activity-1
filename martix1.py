matrix1 = [[2,5,1],
          [4,9,0],
          [11,6,7]]

matrix2 = [[5,5,1],
          [5,8,1],
          [9,2,6]]


#print(matrix[1][1])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j]*2,end=" ")
    print()
        

counter=0


for i in range(len(matrix)):
    for j in range(len(matrix)):
        if(matrix[i][j]==0 ):
            counter+=1
print("number of 0 in matrix: ",counter)

  
size=int(input("enter the size "))
for i in range(size):
    for j in range(size):   
        if(i==j):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
    
    
size=int(input("enter the size "))
for i in range(size):
    for j in range(size):   
        if(i<=j):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
    
    

    

            
                
            
            
            
        


    
    

    

            
                
            
            
            
        


        