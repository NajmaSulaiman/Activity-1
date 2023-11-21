#def main():
    
    
    
    
counter=[]
x=[1,2,3,4,5,6]
def countInputs(side):
    
    
    while(True):
        n=input("enter a number: ")
        if(n!="Q"):
            counter.append(int(n))
        else:
            #print(counter)
            break
    
    return counter
a=countInputs(counter)
print(a)
"""
one=a.count(1)
two=a.count(2)
three=a.count(3)
four=a.count(4)
five=a.count(5)
six=a.count(6)
print("number of 1: ",one)"""
for i in a:
    print(x,":",a.count(i))

   
#def printCounters(counter):
    
        
        
    
    
    
    
    
    
#main()   
    