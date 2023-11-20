"""v="abaacb"
mark=0
x=input("enter your choice: ")
for i in range(len(x)):
    if( x[i]==v[i]):
        mark+=1
    
       
        
    
print(mark,"out of ",len(x))

"""

v="abaacb"
mark=6
x=input("enter your choice: ")
for i in range(len(x)):
    if( x[i]!=v[i]):
        mark-=1
    
       
        
    
print(mark,"out of ",len(x))




