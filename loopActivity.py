#Q2
"""
for i in range(1,5):
    print("*" * i)
for i in range(5,0,-1):
    print("*" * i)
    """

"""
for i in range(1,101):
    for j in range(1,i):
        if(j%i==0):
            summ=summ+j
if(i==summ):
    print ("the number is perfect")
else:
    print ("the number is not perfect")
        """

#Q3: perfect number
number=int(input("enter a number: "))
summ=0
for i in range(1,number):
    if(number%i==0):
        summ=summ+i
        
if(number==summ):
    print ("the number is perfect")
else:
    print ("the number is not perfect")
    
summ=0
for i in range(1,101):
    for j in range(1,i):
        if(j%i==0):
            summ=summ+i
    if(summ==i):
        
        print (str(i)+" is perfect")
    else:
        print (str(i)+" is not perfect")

        
        
