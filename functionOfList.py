from typing import List

def revarse_list(my_list:List[int]):
    
    return max(my_list)

new_list=[1,7,6]
print(max(new_list))

def Reverse(lst:List[int]):
   new_lst = lst[::-1]
   return new_lst
 
 
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))


def add_fun(x:int,y:int)->int:
    return x+y

z=add_fun(4,6)
print(z)