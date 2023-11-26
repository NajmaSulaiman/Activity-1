def readFloat(n):
    result=[]
    for i in range(n): 
        num = float(input("Enter numbers  : "))
        result.append(num)
    return result

def multiply(ls, factor):
    for i in range(len(ls)):
        ls[i]=ls[i] * factor
    return ls

def print_reverse(ls):
    
    ls.reverse()
    return ls
    
        
def main():
    my_list= readFloat(4)
    print("list before factor: ",my_list)
    number =int(input("enter the factor: "))
    new_list=multiply(my_list, number)
    print("list after factor: ",new_list)
    final_list=print_reverse(new_list)
    print("list after reverse: ",final_list)
     
main()   
   

        
